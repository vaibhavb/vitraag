---
date: 2022-10-17 05:06:00+00:00
layout: default
title: Blog Posts
permalink: /posts-by-year/
categories:
- blog
---
<div class="content" style="padding-top: 4rem;margin-left: 1rem;">
{% for post in site.posts %}
  {% capture current_year %}{{ post.date | date: "%Y" }}{% endcapture %}
  {% if current_year != previous_year %}
    {% unless forloop.first %}
      </ul>
    {% endunless %}
    <h3>Archive of posts from {{ current_year }}</h3>
    <ul>
    {% assign previous_year = current_year %}
  {% endif %}
  <li>
    <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    {% for category in post.categories%} <span class="tag is-primary">{{category}}</span> {%endfor%}
    {% for tag in post.tags%} <span class="tag is-secondary"> {{tag}} </span>{%endfor%}
  </li>
  {% if forloop.last %}
    </ul>
  {% endif %}
{% endfor %}
</div>
