---
date: 2022-10-17 05:06:00+00:00
layout: default
title: Posts By Year! 
permalink: /posts-by-year/
js: heatmap.js
categories:
- blog
---
{% if page.js %}
  <script src="/assets/js/{{ page.js }}"></script>
{% endif %}

<div class="content" style="padding-top: 4rem;margin-left: 1rem;">
  <!-- experimental heatmap-->
  <div class="heatmap">
    <div id="commit-graph" class="grid"></div>
  </div>

  <!-- feature: popular posts -->
  <h2>Popular Posts</h2>
    <p>Last updated: {{ site.data.popular_posts.last_updated | date: "%Y-%m-%d %H:%M:%S %Z" }}</p>
    <ul>
    {% for post in site.data.popular_posts.posts %}
      <li>
        <a href="{{ post.path }}">{{ post.title }}</a>
        ({{ post.pageviews }} views)
      </li>
    {% endfor %}
    </ul>
  <hr/>

  <h2>Yearly Posts</h2>
{% assign counter = 0 %}
{% for post in site.posts %}
  {% capture current_year %}{{ post.date | date: "%Y" }}{% endcapture %}
  {% assign counter = counter | plus: 1 %}
  
  {% if current_year != previous_year %}
    {% unless forloop.first %}
      <div class="tag is-danger"> Total posts {{counter}}</div>
      </ul>
    {% endunless %}
    <h3>Archive of posts from {{ current_year }}</h3>
    <ul>
    {% assign counter = 0 %}
    {% assign previous_year = current_year %}
  {% endif %}
  
  <li>
    <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    {% for category in post.categories%} <span class="tag is-primary"><a href="/index.html#{{ category | slugify }}">{{category}}</a></span> {%endfor%}
    {% for tag in post.tags%} <span class="tag is-secondary">{{tag}}</span>{%endfor%}
  </li>

  {% if forloop.last %}
    </ul>
  {% endif %}
{% endfor %}
</div>


