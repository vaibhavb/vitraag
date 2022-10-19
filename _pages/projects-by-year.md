---
date: 2022-10-17 05:06:00+00:00
layout: default
title: Blog Posts
permalink: /projects-by-year/
categories:
- blog
---
<div class="content" style="padding-top: 4rem;margin-left: 1rem;">
{% assign counter = 0 %}
{% for p in site.data.projects %}
  {% capture current_year %}{{ p.date-started | date: "%Y" }}{% endcapture %}
  
  {% if current_year != previous_year %}
    {% unless forloop.first %}
      </ul>
    {% endunless %}
    <h3>Archive of Projects from {{ current_year }}</h3>
    <h4>{{p.name}}</h4>
    <ul>
    {% assign previous_year = current_year %}
  {% endif %}
  
  {% for cat in site.categories %}
  {% if cat[0] == p.blogpost-category %}
  {% for post in cat[1] %}

  <li>
    <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    {% for category in post.categories%} <span class="tag is-primary"><a href="/index.html/#{{ category | slugify }}">{{category}}</a></span> {%endfor%}
    {% for tag in post.tags%} <span class="tag is-secondary">{{tag}}</span>{%endfor%}
  </li>
  {%endfor%}
  <div class="tag is-danger"> Total posts {{ cat | last | size }}</div>
  {%endif%}
  {%endfor%}

  {% if forloop.last %}
    </ul>
  {% endif %}
{% endfor %}
</div>


