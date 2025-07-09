#!/usr/bin/env python3
"""
News Updater - Phase 3: File Operations
Handles YAML generation and file updates for weekly news workflow
"""

import json
import yaml
import argparse
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

class NewsFileUpdater:
    def __init__(self, data_dir: str = "_data"):
        self.data_dir = Path(data_dir)
        self.backup_suffix = f".backup-{datetime.now().strftime('%Y-%m-%d')}"
        
    def create_backup(self, file_path: Path) -> bool:
        """Create backup of existing file"""
        if file_path.exists():
            backup_path = file_path.with_suffix(f"{file_path.suffix}{self.backup_suffix}")
            try:
                shutil.copy2(file_path, backup_path)
                print(f"   ✅ Created backup: {backup_path.name}")
                return True
            except Exception as e:
                print(f"   ❌ Error creating backup: {e}")
                return False
        return True
    
    def read_existing_yaml(self, file_path: Path) -> List[Dict]:
        """Read existing YAML file content"""
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return yaml.safe_load(f) or []
            except Exception as e:
                print(f"   ⚠️  Error reading {file_path}: {e}")
                return []
        return []
    
    def generate_yaml_entry(self, target_date: str, items: List[Dict]) -> Dict:
        """Generate YAML entry for given date and items"""
        return {
            "date": target_date,
            "news-items": items
        }
    
    def update_yaml_file(self, file_path: Path, new_entry: Dict) -> tuple[bool, str]:
        """Update YAML file by merging items for same date or prepending new entry"""
        try:
            # Read existing content
            existing_data = self.read_existing_yaml(file_path)
            
            target_date = str(new_entry.get('date'))
            new_items = new_entry.get('news-items', [])
            
            # Check if target_date already exists
            date_found = False
            added_items = 0
            
            for entry in existing_data:
                existing_date = str(entry.get('date'))
                if existing_date == target_date:
                    # Merge items while avoiding duplicates
                    existing_items = entry.get('news-items', [])
                    existing_links = {item.get('link') for item in existing_items}
                    
                    # Add new items that don't have duplicate links
                    for new_item in new_items:
                        if new_item.get('link') not in existing_links:
                            existing_items.append(new_item)
                            added_items += 1
                    
                    entry['news-items'] = existing_items
                    date_found = True
                    break
            
            # If date not found, prepend new entry
            if not date_found:
                updated_data = [new_entry] + existing_data
                added_items = len(new_items)
                status = f"new date"
            else:
                updated_data = existing_data
                status = f"merged {added_items} items"
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                yaml.dump(updated_data, f, default_flow_style=False, 
                         allow_unicode=True, sort_keys=False, indent=2)
            
            return True, status
            
        except Exception as e:
            print(f"   ❌ Error updating {file_path}: {e}")
            return False, "error"
    
    def validate_input_data(self, data: Dict) -> bool:
        """Validate input JSON structure"""
        required_fields = ['target_date', 'categories', 'summary']
        
        for field in required_fields:
            if field not in data:
                print(f"❌ Missing required field: {field}")
                return False
        
        if not isinstance(data['categories'], dict):
            print("❌ 'categories' must be a dictionary")
            return False
        
        for category, content in data['categories'].items():
            if 'items' not in content:
                print(f"❌ Missing 'items' in category: {category}")
                return False
            
            for item in content['items']:
                if 'desc' not in item or 'link' not in item:
                    print(f"❌ Invalid item structure in {category}: {item}")
                    return False
        
        return True
    
    def process_updates(self, input_file: str) -> bool:
        """Process news updates from JSON input"""
        # Load input data
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ Error loading input file: {e}")
            return False
        
        # Validate input
        if not self.validate_input_data(data):
            return False
        
        print(f"📅 Processing updates for: {data['target_date']}")
        print(f"📊 Total items: {data['summary']['total_items']}")
        
        # Create backups
        print("\n💾 Creating backups...")
        backup_success = True
        for category in data['categories'].keys():
            file_path = self.data_dir / f"{category}.yml"
            if not self.create_backup(file_path):
                backup_success = False
        
        if not backup_success:
            print("❌ Backup creation failed, aborting updates")
            return False
        
        # Update files
        print("\n🔄 Updating YAML files...")
        success_count = 0
        total_items = 0
        
        for category, content in data['categories'].items():
            if not content['items']:
                continue
                
            file_path = self.data_dir / f"{category}.yml"
            new_entry = self.generate_yaml_entry(data['target_date'], content['items'])
            
            success, status = self.update_yaml_file(file_path, new_entry)
            if success:
                item_count = len(content['items'])
                print(f"   ✅ Updated {category}.yml ({item_count} items - {status})")
                success_count += 1
                total_items += item_count
            else:
                print(f"   ❌ Failed to update {category}.yml")
        
        # Summary
        print(f"\n📊 UPDATE SUMMARY:")
        print(f"{'='*50}")
        print(f"Target date: {data['target_date']}")
        print(f"Categories processed: {len(data['categories'])}")
        print(f"Files updated: {success_count}")
        print(f"Total items added: {total_items}")
        print(f"Backup suffix: {self.backup_suffix}")
        
        categories_with_items = [c for c in data['categories'].values() if c['items']]
        if success_count == len(categories_with_items):
            print(f"\n🎉 All updates completed successfully!")
            
            # Clean up backup files after successful updates
            updated_categories = [category for category, content in data['categories'].items() if content['items']]
            cleanup_success = self.cleanup_backups(updated_categories)
            
            if cleanup_success:
                print(f"✅ Cleanup completed successfully!")
            else:
                print(f"⚠️  Some backup files could not be cleaned (updates still successful)")
            
            return True
        else:
            print(f"\n⚠️  Some updates failed. Check individual file results above.")
            print(f"   📝 Backup files preserved for recovery")
            return False
    
    def cleanup_backups(self, categories: List[str]) -> bool:
        """Remove backup files after successful updates"""
        print("\n🧹 Cleaning up backup files...")
        cleanup_success = True
        cleaned_count = 0
        
        for category in categories:
            file_path = self.data_dir / f"{category}.yml"
            backup_path = file_path.with_suffix(f"{file_path.suffix}{self.backup_suffix}")
            
            if backup_path.exists():
                try:
                    backup_path.unlink()
                    print(f"   ✅ Removed backup: {backup_path.name}")
                    cleaned_count += 1
                except Exception as e:
                    print(f"   ⚠️  Error removing backup {backup_path.name}: {e}")
                    cleanup_success = False
        
        if cleaned_count > 0:
            print(f"   📊 Cleaned {cleaned_count} backup files")
        else:
            print("   📊 No backup files to clean")
        
        return cleanup_success
    
    def restore_from_backup(self, category: str) -> bool:
        """Restore file from backup"""
        file_path = self.data_dir / f"{category}.yml"
        backup_path = file_path.with_suffix(f"{file_path.suffix}{self.backup_suffix}")
        
        if backup_path.exists():
            try:
                shutil.copy2(backup_path, file_path)
                print(f"✅ Restored {category}.yml from backup")
                return True
            except Exception as e:
                print(f"❌ Error restoring {category}.yml: {e}")
                return False
        else:
            print(f"❌ Backup not found: {backup_path}")
            return False

def main():
    parser = argparse.ArgumentParser(description='Update news YAML files from JSON input')
    parser.add_argument('--input', required=True, help='Input JSON file from Claude processing')
    parser.add_argument('--data-dir', default='_data', help='Directory containing YAML files')
    parser.add_argument('--restore', help='Restore category from backup (e.g., security-news)')
    
    args = parser.parse_args()
    
    updater = NewsFileUpdater(args.data_dir)
    
    if args.restore:
        # Restore mode
        if updater.restore_from_backup(args.restore):
            print(f"✅ Restore completed for {args.restore}")
        else:
            print(f"❌ Restore failed for {args.restore}")
    else:
        # Update mode
        if updater.process_updates(args.input):
            print(f"\n🚀 News update workflow completed successfully!")
        else:
            print(f"\n❌ News update workflow failed!")

if __name__ == "__main__":
    main()