---
date: 2022-10-17 05:06:00+00:00
layout: default
title: My Travels
permalink: /travels/
js: worldmap.js
categories:
- blog
---
{% if page.js %}
  <script src="https://d3js.org/d3.v7.min.js"></script>
  <script src="https://unpkg.com/topojson@3"></script>
  <script src="{{ base.url | prepend: site.url }}/assets/js/{{ page.js }}" defer></script>
{% endif %}

<div class="content" style="padding-top: 4rem;margin-left: 1rem;">
  <div>
  </div>
  <!-- experimental worldmap-->
  <div id="map" style="height: 400px;"></div>

{% assign counter = 0 %}
{% assign previous_year = "" %} <!-- Initialize as an empty string for comparison -->

{% for post in site.posts %}
  {% if post.categories contains 'travel' or post.categories contains 'mountaineering' or post.categories contains 'cycling' %}
    {% capture current_year %}{{ post.date | date: "%Y" }}{% endcapture %}
    {% assign counter = counter | plus: 1 %}

    {% if current_year != previous_year %}
      <!-- Close the previous list only if it's not the first iteration -->
      {% if previous_year != "" %}
        <div class="tag is-danger">Total posts {{ counter }}</div>
        </ul>
        {% assign counter = 0 %} <!-- Reset counter for the new year -->
      {% endif %}

      <h3>Archive of travel posts from {{ current_year }}</h3>
      <ul>
      {% assign previous_year = current_year %}
    {% endif %}

    <li>
      <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      {% for category in post.categories %} <span class="tag is-primary"><a href="/index.html#{{ category | slugify }}">{{ category }}</a></span> {% endfor %}
      {% for tag in post.tags %} <span class="tag is-secondary">{{ tag }}</span> {% endfor %}
    </li>
  {% endif %}

  {% if forloop.last %}
    <!-- This ensures the closing tags are added after the last post -->
    <div class="tag is-danger">Total posts {{ counter }}</div>
    </ul>
  {% endif %}
{% endfor %}

</div>


