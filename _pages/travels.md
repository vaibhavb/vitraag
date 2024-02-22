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

{% assign previous_year = "" %} <!-- Initialize as an empty string for comparison -->
{% assign posts_counted = false %}

{% for post in site.posts %}
  {% if post.categories contains 'travel' or post.categories contains 'mountaineering' or post.categories contains 'cycling' %}
    {% capture current_year %}{{ post.date | date: "%Y" }}{% endcapture %}
    {% if current_year != previous_year %}
      {% if posts_counted %}
        <!-- Display the count for the previous year before resetting -->
        <div class="tag is-danger">Total posts in {{ previous_year }}: {{ counter }}</div>
        </ul> <!-- Ensure this is closed only if a new year is started or at the end -->
        {% assign counter = 0 %} <!-- Reset counter for the new year -->
        {% assign posts_counted = false %}
      {% endif %}
      <h3>Archive of travel posts from {{ current_year }}</h3>
      <ul>
      {% assign previous_year = current_year %}
    {% endif %}

    {% assign counter = counter | plus: 1 %}
    {% assign posts_counted = true %}

    <li>
      <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      {% for category in post.categories %}<span class="tag is-primary"><a href="/index.html#{{ category | slugify }}">{{ category }}</a></span>{% endfor %}
      {% for tag in post.tags %}<span class="tag is-secondary">{{ tag }}</span>{% endfor %}
    </li>
  {% endif %}

  {% if forloop.last %}
    <!-- Handle the last post correctly, ensuring the counter for the last year is displayed -->
    {% if posts_counted %}
      <div class="tag is-danger">Total posts in {{ previous_year }}: {{ counter }}</div>
    {% endif %}
    </ul>
  {% endif %}
{% endfor %}

</div>


