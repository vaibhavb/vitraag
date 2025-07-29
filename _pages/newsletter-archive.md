---
layout: default
title: "Newsletter Archive - The Weekly Vitraag Digest"
permalink: /newsletter/archive/
---

<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Source+Serif+Pro:wght@400;600;700&display=swap');
    
    .archive-container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 3rem 2rem;
        font-family: 'Source Serif Pro', Georgia, serif;
    }
    
    .archive-header {
        text-align: center;
        margin-bottom: 4rem;
        border-bottom: 3px solid #000;
        padding-bottom: 3rem;
    }
    
    .archive-header h1 {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #000;
        margin-bottom: 1rem;
    }
    
    .archive-description {
        font-size: 1.2rem;
        color: #666;
        max-width: 600px;
        margin: 0 auto 2rem;
        line-height: 1.6;
    }
    
    .archive-actions {
        margin: 2rem 0;
    }
    
    .btn {
        display: inline-block;
        padding: 0.8rem 1.5rem;
        margin: 0.5rem;
        border: 2px solid #000;
        text-decoration: none;
        color: #000;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    
    .btn:hover {
        background: #000;
        color: #fff;
    }
    
    .btn-primary {
        background: #000;
        color: #fff;
    }
    
    .btn-primary:hover {
        background: #333;
    }
    
    .search-box {
        max-width: 400px;
        margin: 2rem auto;
        position: relative;
    }
    
    .search-input {
        width: 100%;
        padding: 1rem;
        border: 2px solid #000;
        font-size: 1rem;
        font-family: inherit;
    }
    
    .search-input:focus {
        outline: none;
        background: #f8f8f8;
    }
    
    .archive-stats {
        background: #f8f8f8;
        border: 2px solid #000;
        padding: 2rem;
        margin: 3rem 0;
        text-align: center;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 2rem;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        display: block;
        margin-bottom: 0.5rem;
        color: #000;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .year-section {
        margin: 4rem 0;
    }
    
    .year-header {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #000;
        color: #000;
    }
    
    .months-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
    }
    
    .month-section {
        border: 2px solid #000;
        background: #fff;
    }
    
    .month-header {
        background: #000;
        color: #fff;
        padding: 1rem;
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-align: center;
    }
    
    .month-issues {
        padding: 1.5rem;
    }
    
    .issue-item {
        padding: 1rem 0;
        border-bottom: 1px solid #eee;
    }
    
    .issue-item:last-child {
        border-bottom: none;
    }
    
    .issue-title {
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .issue-title a {
        text-decoration: none;
        color: #000;
        font-size: 1.1rem;
    }
    
    .issue-title a:hover {
        color: #0066cc;
    }
    
    .issue-meta {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    
    .issue-summary {
        color: #444;
        line-height: 1.6;
        font-size: 0.95rem;
    }
    
    .no-results {
        text-align: center;
        padding: 3rem;
        color: #666;
        font-style: italic;
    }
    
    .back-to-top {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        background: #000;
        color: #fff;
        border: none;
        padding: 1rem;
        cursor: pointer;
        border-radius: 50%;
        display: none;
        transition: all 0.3s ease;
    }
    
    .back-to-top:hover {
        background: #333;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .archive-container {
            padding: 2rem 1rem;
        }
        
        .archive-header h1 {
            font-size: 2rem;
            letter-spacing: 1px;
        }
        
        .months-grid {
            grid-template-columns: 1fr;
        }
        
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .btn {
            display: block;
            margin: 0.5rem 0;
            text-align: center;
        }
    }
</style>

<div class="archive-container">
    <header class="archive-header">
        <h1>Newsletter Archive</h1>
        <div class="archive-description">
            Explore my complete collection of Weekly Vitraag Digest issues. 
            Each edition features carefully curated stories from across the technology landscape.
        </div>
        
        <div class="archive-actions">
            <a href="/newsletter" class="btn">📧 Newsletter Home</a>
            <a href="/newsletter.xml" class="btn btn-primary">📡 Subscribe RSS</a>
        </div>
        
        <div class="search-box">
            <input type="text" class="search-input" id="search-input" placeholder="Search newsletters...">
        </div>
    </header>

    {% assign newsletters = site.newsletters | default: empty | sort: 'date' | reverse %}
    {% if newsletters.size > 0 %}
    
    <section class="archive-stats">
        <h2 style="font-family: 'Playfair Display', serif; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 2rem;">Archive Statistics</h2>
        <div class="stats-grid">
            <div class="stat-item">
                <span class="stat-number">{{ newsletters.size }}</span>
                <span class="stat-label">Issues Published</span>
            </div>
            <div class="stat-item">
                {% assign total_stories = 0 %}
                {% if newsletters %}
                    {% for newsletter in newsletters %}
                        {% assign total_stories = total_stories | plus: newsletter.total_stories %}
                    {% endfor %}
                {% endif %}
                <span class="stat-number">{{ total_stories }}</span>
                <span class="stat-label">Stories Curated</span>
            </div>
            <div class="stat-item">
                {% assign avg_stories = total_stories | divided_by: newsletters.size %}
                <span class="stat-number">{{ avg_stories }}</span>
                <span class="stat-label">Avg Stories/Issue</span>
            </div>
            <div class="stat-item">
                {% assign first_newsletter = newsletters | last %}
                {% assign weeks_published = newsletters.size %}
                <span class="stat-number">{{ weeks_published }}</span>
                <span class="stat-label">Weeks Published</span>
            </div>
        </div>
    </section>

    {% assign newsletters_by_year = newsletters | group_by_exp: "newsletter", "newsletter.date | date: '%Y'" %}
    
    {% for year_group in newsletters_by_year %}
    <section class="year-section">
        <h2 class="year-header">{{ year_group.name }}</h2>
        
        {% assign newsletters_by_month = year_group.items | group_by_exp: "newsletter", "newsletter.date | date: '%B'" %}
        
        <div class="months-grid">
            {% for month_group in newsletters_by_month %}
            <div class="month-section searchable-section">
                <div class="month-header">{{ month_group.name }}</div>
                <div class="month-issues">
                    {% for newsletter in month_group.items %}
                    <div class="issue-item searchable-item" 
                         data-search="{{ newsletter.title | downcase }} {{ newsletter.date }} {{ newsletter.total_stories }} stories issue {{ newsletter.issue_number }}">
                        <div class="issue-title">
                            <a href="{{ newsletter.url }}">Issue #{{ newsletter.issue_number }}</a>
                        </div>
                        <div class="issue-meta">
                            {{ newsletter.date | date: "%B %d, %Y" }} • {{ newsletter.total_stories }} stories
                        </div>
                        <div class="issue-summary">
                            {% if newsletter.security_count > 0 %}{{ newsletter.security_count }} security • {% endif %}
                            {% if newsletter.ai_count > 0 %}{{ newsletter.ai_count }} AI • {% endif %}
                            {% if newsletter.health_count > 0 %}{{ newsletter.health_count }} health • {% endif %}
                            {% if newsletter.pm_count > 0 %}{{ newsletter.pm_count }} product • {% endif %}
                            {% if newsletter.finance_count > 0 %}{{ newsletter.finance_count }} finance{% endif %}
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}
        </div>
    </section>
    {% endfor %}
    
    <div class="no-results" id="no-results" style="display: none;">
        <h3>No newsletters found</h3>
        <p>Try adjusting your search terms or <a href="#" onclick="clearSearch()">clear the search</a>.</p>
    </div>
    
    {% else %}
    <section class="no-results">
        <h3>No newsletters available yet</h3>
        <p>Check back soon for our first edition of The Weekly Tech Digest!</p>
        <a href="/newsletter" class="btn">← Back to Newsletter Home</a>
    </section>
    {% endif %}
</div>

<button class="back-to-top" id="back-to-top" onclick="scrollToTop()">↑</button>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const searchableItems = document.querySelectorAll('.searchable-item');
    const searchableSections = document.querySelectorAll('.searchable-section');
    const noResults = document.getElementById('no-results');
    const backToTop = document.getElementById('back-to-top');
    
    // Search functionality
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase().trim();
        
        if (searchTerm === '') {
            // Show all items and sections
            searchableItems.forEach(item => {
                item.style.display = 'block';
            });
            searchableSections.forEach(section => {
                section.style.display = 'block';
            });
            noResults.style.display = 'none';
        } else {
            let hasResults = false;
            
            // Hide all sections first
            searchableSections.forEach(section => {
                section.style.display = 'none';
            });
            
            // Check each item
            searchableItems.forEach(item => {
                const searchData = item.getAttribute('data-search');
                if (searchData && searchData.includes(searchTerm)) {
                    item.style.display = 'block';
                    // Show the parent section
                    const parentSection = item.closest('.searchable-section');
                    if (parentSection) {
                        parentSection.style.display = 'block';
                    }
                    hasResults = true;
                } else {
                    item.style.display = 'none';
                }
            });
            
            // Show/hide no results message
            noResults.style.display = hasResults ? 'none' : 'block';
        }
    });
    
    // Back to top functionality
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTop.style.display = 'block';
        } else {
            backToTop.style.display = 'none';
        }
    });
});

function clearSearch() {
    document.getElementById('search-input').value = '';
    document.getElementById('search-input').dispatchEvent(new Event('input'));
}

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Focus search on '/' key
    if (e.key === '/' && !e.ctrlKey && !e.metaKey) {
        e.preventDefault();
        document.getElementById('search-input').focus();
    }
    
    // Clear search on Escape
    if (e.key === 'Escape') {
        clearSearch();
        document.getElementById('search-input').blur();
    }
});
</script>