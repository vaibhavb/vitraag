---
layout: default
title: bookmarks
permalink: /bookmarks
---
<div class="my-container">
    <header class="header">
        <h1 class="page-title">My Bookmarks</h1>
    </header>
    <div id="search-container">
        <input type="text" id="search-input" placeholder="Search bookmarks...">
    </div>
    <div class="content">
        <aside class="sidebar">
            <div id="tag-cloud"></div>
        </aside>
        <main class="main">
            <div id="tag-stats" class="tag-stats"></div>
            <div id="bookmarks-container"></div>
        </main>
    </div>
</div>

<script>
    // Load bookmarks from JSON file
    fetch('/assets/data/bookmarks.json')
        .then(response => response.json())
        .then(bookmarks => {
            const container = document.getElementById('bookmarks-container');
            const searchInput = document.getElementById('search-input');
            const tagCloud = document.getElementById('tag-cloud');
            const tagStats = document.getElementById('tag-stats');
            
            // Parse tags from titles and update bookmarks
            const tagCounts = {};
            bookmarks.forEach(bookmark => {
                const parsedTags = bookmark.title.match(/#[\w-]+/g) || [];
                bookmark.tags = parsedTags.map(tag => tag.substring(1));
                bookmark.tags.forEach(tag => {
                    tagCounts[tag] = (tagCounts[tag] || 0) + 1;
                });
                
                // Remove tags from the displayed title
                bookmark.displayTitle = bookmark.title.replace(/#[\w-]+/g, '').trim();
            });

            // Function to generate a color based on a string
            function stringToColor(str) {
                let hash = 0;
                for (let i = 0; i < str.length; i++) {
                    hash = str.charCodeAt(i) + ((hash << 5) - hash);
                }
                const hue = hash % 360;
                return `hsl(${hue}, 70%, 60%)`;
            }

            // Function to calculate font size based on tag count
            function calculateFontSize(count, minCount, maxCount) {
                const minSize = 0.8;
                const maxSize = 1.5;
                return minSize + (count - minCount) * (maxSize - minSize) / (maxCount - minCount);
            }

            // Get min and max tag counts
            const minCount = Math.min(...Object.values(tagCounts));
            const maxCount = Math.max(...Object.values(tagCounts));
            
            // Create tag cloud
            Object.entries(tagCounts).sort((a, b) => b[1] - a[1]).forEach(([tag, count]) => {
                const tagElement = document.createElement('span');
                tagElement.classList.add('tag');
                tagElement.textContent = `#${tag}`;
                tagElement.addEventListener('click', () => filterBookmarksByTag(tag));
                
                // Apply color and font size
                const color = stringToColor(tag);
                const fontSize = calculateFontSize(count, minCount, maxCount);
                tagElement.style.backgroundColor = color;
                tagElement.style.fontSize = `${fontSize}em`;
                
                tagCloud.appendChild(tagElement);
            });
            
            // Update tag stats
            updateTagStats();
            
            // Function to render bookmarks
            function renderBookmarks(bookmarks) {
                container.innerHTML = '';
                const groupedBookmarks = groupByWeek(bookmarks);
                
                // Sort weeks in descending order
                const sortedWeeks = Object.keys(groupedBookmarks).sort((a, b) => b.localeCompare(a));
                
                sortedWeeks.forEach(week => {
                    const links = groupedBookmarks[week];
                    const weekElement = document.createElement('div');
                    const weekDate = getWeekStartDate(links[0].date);
                    weekElement.innerHTML = `<h2>Week ${week} (${weekDate}) - ${links.length} bookmark${links.length !== 1 ? 's' : ''}</h2>`;
                    const ulElement = document.createElement('ul');
                    
                    // Sort links within each week by date (most recent first)
                    links.sort((a, b) => b.date.localeCompare(a.date));
                    
                    links.forEach(link => {
                        const liElement = document.createElement('li');
                        const tagSpans = link.tags.map(tag => {
                            const color = stringToColor(tag);
                            return `<span class="tag" style="background-color: ${color}">#${tag}</span>`;
                        }).join(' ');
                        // Format date to be more readable
                        const formattedDate = new Date(link.date).toLocaleDateString('en-US', {
                            year: 'numeric',
                            month: 'short',
                            day: 'numeric'
                        });
                        liElement.innerHTML = `
                            <span class="date">${formattedDate}</span>
                            <a href="${link.url}" target="_blank">${link.displayTitle}</a>
                            <div class="tags">${tagSpans}</div>
                        `;
                        ulElement.appendChild(liElement);
                    });
                    
                    weekElement.appendChild(ulElement);
                    container.appendChild(weekElement);
                });
            }
            
            // Group bookmarks by week
            function groupByWeek(bookmarks) {
                const grouped = {};
                bookmarks.forEach(bookmark => {
                    const date = new Date(bookmark.date);
                    const week = getWeekNumber(date);
                    if (!grouped[week]) grouped[week] = [];
                    grouped[week].push(bookmark);
                });
                return grouped;
            }
            
            // Get week number
            function getWeekNumber(date) {
                const d = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
                const dayNum = d.getUTCDay() || 7;
                d.setUTCDate(d.getUTCDate() + 4 - dayNum);
                const yearStart = new Date(Date.UTC(d.getUTCFullYear(),0,1));
                return d.getUTCFullYear() + '-W' + Math.ceil((((d - yearStart) / 86400000) + 1)/7).toString().padStart(2, '0');
            }
            
            // Get week start date
            function getWeekStartDate(dateString) {
                const date = new Date(dateString);
                const day = date.getDay();
                const diff = date.getDate() - day + (day === 0 ? -6 : 1);
                const weekStart = new Date(date.setDate(diff));
                return weekStart.toISOString().split('T')[0];
            }
            
            // Initial render
            renderBookmarks(bookmarks);
            
            // Search functionality
            function filterBookmarks() {
                const searchTerm = searchInput.value.toLowerCase();
                const filteredBookmarks = bookmarks.filter(bookmark => 
                    bookmark.displayTitle.toLowerCase().includes(searchTerm) ||
                    bookmark.url.toLowerCase().includes(searchTerm) ||
                    bookmark.tags.some(tag => tag.toLowerCase().includes(searchTerm))
                );
                renderBookmarks(filteredBookmarks);
                updateTagStats(filteredBookmarks);
            }
            
            // Tag filter functionality
            function filterBookmarksByTag(tag) {
                const filteredBookmarks = bookmarks.filter(bookmark => 
                    bookmark.tags.includes(tag)
                );
                renderBookmarks(filteredBookmarks);
                updateTagStats(filteredBookmarks);
                // Highlight selected tag
                document.querySelectorAll('#tag-cloud .tag').forEach(tagElement => {
                    tagElement.classList.toggle('selected', tagElement.textContent === `#${tag}`);
                });
            }
            
            // Update tag statistics
            function updateTagStats(filteredBookmarks = bookmarks) {
                const stats = {};
                filteredBookmarks.forEach(bookmark => {
                    bookmark.tags.forEach(tag => {
                        stats[tag] = (stats[tag] || 0) + 1;
                    });
                });
                
                const sortedStats = Object.entries(stats).sort((a, b) => b[1] - a[1]);
                
                tagStats.innerHTML = '<strong>Tag Stats:</strong> ';
                const statStrings = sortedStats.map(([tag, count]) => `#${tag} (${count})`);
                tagStats.innerHTML += statStrings.join(', ');
            }
            
            searchInput.addEventListener('input', filterBookmarks);
        });
</script>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Source+Sans+Pro:wght@400;600&display=swap');

    body {
        font-family: 'Source Sans Pro', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f9f9f9;
        margin: 0;
        padding: 0;
    }

    .my-container {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
        padding-top: 60px; /* Add padding to account for fixed navbar */
    }

    .header {
        background-color: #121212;
        color: #fff;
        padding: 1rem;
        text-align: center;
    }

    .page-title {
        font-family: 'Playfair Display', serif;
        font-size: 2em;
        font-weight: 700;
        margin: 0;
    }

    #search-container {
        padding: 1rem;
        background-color: #f0f0f0;
    }

    #search-input {
        width: 100%;
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-family: 'Source Sans Pro', sans-serif;
    }

    .content {
        display: flex;
        flex: 1;
    }

    .sidebar {
        width: 250px;
        background-color: #f0f0f0;
        padding: 1rem;
        overflow-y: auto;
    }

    .main {
        flex: 1;
        padding: 1rem;
        overflow-y: auto;
    }

    #bookmarks-container {
        margin-top: 1rem;
    }

    #tag-cloud {
        margin-bottom: 1rem;
    }

    .tag {
        color: white;
        padding: 4px 8px;
        border-radius: 3px;
        margin-right: 5px;
        margin-bottom: 5px;
        display: inline-block;
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .tag:hover {
        opacity: 0.8;
    }

    .tag.selected {
        box-shadow: 0 0 0 2px #121212;
    }

    h2 {
        font-family: 'Playfair Display', serif;
        font-size: 1.5em;
        font-weight: 700;
        color: #121212;
        margin-top: 1.5em;
        margin-bottom: 0.5em;
        border-bottom: 1px solid #ccc;
        padding-bottom: 0.2em;
    }

    ul {
        list-style-type: none;
        padding-left: 0;
        margin-left: 0;
    }

    li {
        margin-bottom: 0.5em;
        border-bottom: 1px solid #e0e0e0;
        padding-bottom: 0.5em;
        line-height: 1.4;
    }

    li:last-child {
        border-bottom: none;
    }

    .date {
        font-size: 0.9em;
        color: #666;
        margin-right: 10px;
        font-style: italic;
    }

    #bookmarks-container a {
        color: #1a1a1a;
        text-decoration: underline;
        transition: all 0.3s ease;
    }

    #bookmarks-container a:hover {
        color: #0000ff;
        text-decoration-color: #0000ff;
    }

    .tags {
        margin-top: 0.25em;
    }

    .tag-stats {
        background-color: #f0f0f0;
        padding: 0.5rem;
        margin-bottom: 1rem;
        border-radius: 4px;
        font-size: 0.9em;
        line-height: 1.4;
    }

    @media (max-width: 768px) {
        .content {
            flex-direction: column;
        }

        .sidebar {
            width: 100%;
            order: 2;
        }

        .main {
            order: 1;
        }

        .page-title {
            font-size: 1.5em;
        }

        h2 {
            font-size: 1.2em;
        }

        .tag-stats {
            font-size: 0.8em;
            padding: 0.3rem;
        }

        #tag-cloud {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
    }
</style>
