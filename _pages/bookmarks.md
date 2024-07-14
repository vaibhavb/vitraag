---
layout: page
title: bookmarks
permalink: /bookmarks
---
<div class="bookmarks-wrapper">
  <h1>My Bookmarks</h1>
  <div id="search-container">
    <input type="text" id="search-input" placeholder="Search bookmarks...">
  </div>
  <div id="tag-container">
    <select id="tag-select">
      <option value="">All Tags</option>
    </select>
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
      const tagSelect = document.getElementById('tag-select');
      
      // Parse tags from titles and update bookmarks
      const tags = new Set();
      bookmarks.forEach(bookmark => {
        const parsedTags = bookmark.title.match(/#\w+/g) || [];
        bookmark.tags = parsedTags.map(tag => tag.substring(1));
        bookmark.tags.forEach(tag => tags.add(tag));
        
        // Remove tags from the displayed title
        bookmark.displayTitle = bookmark.title.replace(/#\w+/g, '').trim();
      });
      
      // Populate tag select
      Array.from(tags).sort().forEach(tag => {
        const option = document.createElement('option');
        option.value = tag;
        option.textContent = tag;
        tagSelect.appendChild(option);
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
            const tagSpans = link.tags.map(tag => `<span class="tag">#${tag}</span>`).join(' ');
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
      
      // Search and filter functionality
      function filterBookmarks() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedTag = tagSelect.value.toLowerCase();
        const filteredBookmarks = bookmarks.filter(bookmark => 
          (bookmark.displayTitle.toLowerCase().includes(searchTerm) ||
           bookmark.url.toLowerCase().includes(searchTerm)) &&
          (!selectedTag || bookmark.tags.some(tag => tag.toLowerCase() === selectedTag))
        );
        renderBookmarks(filteredBookmarks);
      }
      
      searchInput.addEventListener('input', filterBookmarks);
      tagSelect.addEventListener('change', filterBookmarks);
    });
</script>

<style>
  .bookmarks-wrapper {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 20px;
  }
  #search-container, #tag-container {
    margin-bottom: 20px;
  }
  #search-input, #tag-select {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  .date {
    font-size: 0.8em;
    color: #666;
    margin-right: 10px;
  }
  ul {
    list-style-type: none;
    padding-left: 0;
    margin-left: 20px;
  }
  li {
    margin-bottom: 10px;
    text-indent: -20px;
    padding-left: 20px;
  }
  h2 {
    margin-top: 30px;
    border-bottom: 1px solid #ccc;
    padding-bottom: 5px;
  }
  .tags {
    margin-top: 5px;
  }
  .tag {
    font-size: 0.8em;
    background-color: #f0f0f0;
    padding: 2px 5px;
    border-radius: 3px;
    margin-right: 5px;
  }
</style>
