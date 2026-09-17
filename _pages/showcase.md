---
date: 2026-09-16 00:00:00+00:00
layout: default
title: Showcase
permalink: /showcase
categories:
- projects
---
<section class="section">
  <div class="container">
    <div class="section-heading">
      <h1 class="title is-2">Showcase</h1>
      <h2 class="subtitle is-5">A few things I've built, one at a time.</h2>
    </div>
    <br>
    <div class="showcase-list">
      {% for item in site.data.showcase %}
      <div class="box showcase-item">
        <div class="columns is-vcentered">
          <div class="column is-two-fifths">
            {% if item.image %}
            <figure class="image">
              <a href="{{ item.link }}" target="_blank">
                <img src="{{site.url}}{{site.baseurl}}/assets/images/projects/{{item.image}}" alt="{{item.title}} screenshot">
              </a>
            </figure>
            {% endif %}
          </div>
          <div class="column">
            <h3 class="title is-4">
              {{item.title}}
              {% if item.subtitle %}<span class="subtitle is-6 has-text-grey">&nbsp;{{item.subtitle}}</span>{% endif %}
            </h3>
            {% if item.tags %}
            <div class="tags">
              {% for tag in item.tags %}
              <span class="tag is-primary is-light">{{tag}}</span>
              {% endfor %}
            </div>
            {% endif %}
            <div class="content">
              {{item.description | markdownify}}
            </div>
            <div class="buttons">
              {% if item.link %}
              <a href="{{item.link}}" target="_blank" class="button is-primary is-rounded">{{item.link_label | default: "View Project"}}</a>
              {% endif %}
              {% if item.blog_link %}
              <a href="{{item.blog_link}}" class="button is-light is-rounded">{{item.blog_label | default: "Read the writeup"}}</a>
              {% endif %}
            </div>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<style>
  .showcase-item {
    border-radius: 8px;
  }
  .showcase-item .image img {
    border-radius: 6px;
  }
</style>
