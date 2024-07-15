---
layout: page
title: bookmarks
permalink: /bookmarks
---
<div class="bookmarks-wrapper">
  <h1 class="page-title">My Bookmarks</h1>
  <div id="search-container">
    <input type="text" id="search-input" placeholder="Search bookmarks...">
  </div>
  <div id="tag-cloud">
    <!-- Tags will be dynamically inserted here -->
  </div>
  <div id="bookmarks-container">
    <!-- Bookmarks will be dynamically inserted here -->
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
      
      // Parse tags from titles and update bookmarks
      const tagCounts = {};
      bookmarks.forEach(bookmark => {
        const parsedTags = bookmark.title.match(/#\w+/g) || [];
        bookmark.tags = parsedTags.map(tag => tag.substring(1));
        bookmark.tags.forEach(tag => {
          tagCounts[tag] = (tagCounts[tag] || 0) + 1;
        });
        
        // Remove tags from the displayed title
        bookmark.displayTitle = bookmark.title.replace(/#\w+/g, '').trim();
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
        const maxSize = 2;
        return minSize + (count - minCount) * (maxSize - minSize) / (maxCount - minCount);
      }

      // Get min and max tag counts
      const minCount = Math.min(...Object.values(tagCounts));
      const maxCount = Math.max(...Object.values(tagCounts));
      
      // Create tag cloud
      Object.entries(tagCounts).sort((a, b) => b[1] - a[1]).forEach(([tag, count]) => {
        const tagElement = document.createElement('span');
        tagElement.classList.add('tag', 'clickable');
        tagElement.textContent = `#${tag} (${count})`;
        tagElement.addEventListener('click', () => filterBookmarksByTag(tag));
        
        // Apply color and font size
        const color = stringToColor(tag);
        const fontSize = calculateFontSize(count, minCount, maxCount);
        tagElement.style.backgroundColor = color;
        tagElement.style.fontSize = `${fontSize}em`;
        
        tagCloud.appendChild(tagElement);
      });
      
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
            liElement.innerHTML = `
              <span class="date">${link.date}</span>
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
          bookmark.url.toLowerCase().includes(searchTerm)
        );
        renderBookmarks(filteredBookmarks);
      }
      
      // Tag filter functionality
      function filterBookmarksByTag(tag) {
        const filteredBookmarks = bookmarks.filter(bookmark => 
          bookmark.tags.includes(tag)
        );
        renderBookmarks(filteredBookmarks);
        // Highlight selected tag
        document.querySelectorAll('#tag-cloud .tag').forEach(tagElement => {
          tagElement.classList.toggle('selected', tagElement.textContent.startsWith(`#${tag} (`));
        });
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
  }

  .bookmarks-wrapper {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 20px;
  }

  .page-title {
    font-family: 'Playfair Display', serif;
    font-size: 3em;
    font-weight: 700;
    color: #121212;
    text-align: center;
    margin-bottom: 0.5em;
    border-bottom: 2px solid #121212;
    padding-bottom: 0.2em;
  }

  #search-container, #tag-cloud {
    margin-bottom: 2em;
  }

  #search-input {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: 'Source Sans Pro', sans-serif;
  }

  .date {
    font-size: 0.9em;
    color: #666;
    margin-right: 10px;
    font-style: italic;
  }

  ul {
    list-style-type: none;
    padding-left: 0;
    margin-left: 0;
  }

  li {
    margin-bottom: 1.5em;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 1em;
  }

  li:last-child {
    border-bottom: none;
  }

  h2 {
    font-family: 'Playfair Display', serif;
    font-size: 1.8em;
    font-weight: 700;
    color: #121212;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
    border-bottom: 1px solid #ccc;
    padding-bottom: 0.2em;
  }

  #tag-cloud {
    line-height: 2.5;
    text-align: center;
  }

  .tag {
    color: white;
    padding: 4px 8px;
    border-radius: 3px;
    margin-right: 5px;
    margin-bottom: 5px;
    display: inline-block;
    transition: all 0.3s ease;
  }

  .tag.clickable {
    cursor: pointer;
  }

  .tag.clickable:hover {
    opacity: 0.8;
  }

  .tag.selected {
    box-shadow: 0 0 0 2px #121212;
  }

  a {
    color: #1a1a1a;
    text-decoration: none;
    border-bottom: 1px solid #1a1a1a;
    transition: all 0.3s ease;
  }

  a:hover {
    color: #0000ff;
    border-bottom-color: #0000ff;
  }

  .tags {
    margin-top: 0.5em;
  }

  @media (max-width: 600px) {
    .page-title {
      font-size: 2.5em;
    }

    h2 {
      font-size: 1.5em;
    }

    li {
      margin-bottom: 1em;
    }
  }
</style>
