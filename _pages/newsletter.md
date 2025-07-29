---
layout: default
title: "The Weekly Tech Digest"
permalink: /newsletter/
---

<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Source+Serif+Pro:wght@400;600;700&display=swap');
    
    .newsletter-landing {
        max-width: 900px;
        margin: 0 auto;
        padding: 3rem 2rem;
        font-family: 'Source Serif Pro', Georgia, serif;
    }
    
    .masthead {
        text-align: center;
        margin-bottom: 4rem;
        border-bottom: 3px solid #000;
        padding-bottom: 3rem;
    }
    
    .masthead h1 {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 900;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #000;
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .tagline {
        font-size: 1.4rem;
        color: #666;
        font-style: italic;
        margin-bottom: 1rem;
    }
    
    .description {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #444;
        max-width: 600px;
        margin: 0 auto;
    }
    
    .latest-issue {
        background: #f8f8f8;
        border: 3px solid #000;
        padding: 3rem;
        margin: 3rem 0;
        text-align: center;
    }
    
    .latest-issue h2 {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 1.5rem;
        color: #000;
    }
    
    .issue-preview {
        margin: 2rem 0;
    }
    
    .issue-meta {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 1rem;
    }
    
    .issue-highlights {
        font-size: 1.1rem;
        line-height: 1.7;
        color: #444;
        margin-bottom: 2rem;
    }
    
    .cta-buttons {
        margin: 2rem 0;
    }
    
    .btn {
        display: inline-block;
        padding: 1rem 2rem;
        margin: 0.5rem;
        border: 2px solid #000;
        background: #000;
        color: #fff;
        text-decoration: none;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        font-size: 1rem;
    }
    
    .btn:hover {
        background: #fff;
        color: #000;
    }
    
    .btn-outline {
        background: #fff;
        color: #000;
    }
    
    .btn-outline:hover {
        background: #000;
        color: #fff;
    }
    
    .rss-info {
        background: #fff;
        border: 2px solid #000;
        padding: 2rem;
        margin: 3rem 0;
    }
    
    .rss-info h3 {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1rem;
        color: #000;
    }
    
    .rss-url {
        background: #f0f0f0;
        padding: 1rem;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
        border: 1px solid #ccc;
        word-break: break-all;
    }
    
    .rss-readers {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1rem;
        margin: 1.5rem 0;
    }
    
    .rss-reader {
        text-align: center;
        padding: 1rem;
        border: 1px solid #ddd;
        text-decoration: none;
        color: #000;
        transition: all 0.3s ease;
    }
    
    .rss-reader:hover {
        border-color: #000;
        background: #f8f8f8;
    }
    
    .recent-issues {
        margin: 4rem 0;
    }
    
    .recent-issues h2 {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 2rem;
        text-align: center;
        color: #000;
    }
    
    .issues-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .issue-card {
        border: 2px solid #000;
        padding: 2rem;
        background: #fff;
        transition: all 0.3s ease;
    }
    
    .issue-card:hover {
        background: #f8f8f8;
    }
    
    .issue-card h3 {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
        color: #000;
    }
    
    .issue-card .date {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    .issue-card .summary {
        color: #444;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .issue-card .read-link {
        color: #0066cc;
        text-decoration: none;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-size: 0.9rem;
    }
    
    .issue-card .read-link:hover {
        text-decoration: underline;
    }
    
    .newsletter-stats {
        background: #000;
        color: #fff;
        padding: 3rem 2rem;
        margin: 4rem 0;
        text-align: center;
    }
    
    .newsletter-stats h2 {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        margin-bottom: 2rem;
        text-transform: uppercase;
        letter-spacing: 1px;
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
        font-size: 2.5rem;
        font-weight: 700;
        display: block;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .why-rss {
        margin: 4rem 0;
        padding: 3rem;
        background: #f8f8f8;
        border-left: 6px solid #000;
    }
    
    .why-rss h2 {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        margin-bottom: 2rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #000;
    }
    
    .benefits-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
    }
    
    .benefit-item {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
    }
    
    .benefit-icon {
        font-size: 1.5rem;
        color: #000;
        margin-top: 0.2rem;
    }
    
    .benefit-text {
        color: #444;
        line-height: 1.6;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .newsletter-landing {
            padding: 2rem 1rem;
        }
        
        .masthead h1 {
            font-size: 2.5rem;
            letter-spacing: 1px;
        }
        
        .latest-issue {
            padding: 2rem 1rem;
        }
        
        .btn {
            display: block;
            margin: 0.5rem 0;
            text-align: center;
        }
        
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .rss-readers {
            grid-template-columns: repeat(2, 1fr);
        }
    }
</style>

<div class="newsletter-landing">
    <header class="masthead">
        <h1>The Weekly Vitraag Digest</h1>
        <div class="tagline">A curated collection of the week's most important tech stories</div>
        <div class="description">
            Every week, I handpick the most significant developments across cybersecurity, 
            artificial intelligence, digital health, product management, and financial technology. 
            From breakthrough research to industry shifts, get the insights that matter.
        </div>
    </header>

    {% assign latest_newsletter = site.newsletters | default: empty | sort: 'date' | reverse | first %}
    
    {% if latest_newsletter %}
    <section class="latest-issue">
        <h2>Latest Issue</h2>
        <div class="issue-preview">
            <div class="issue-meta">
                Issue #{{ latest_newsletter.issue_number }} • {{ latest_newsletter.date | date: "%B %d, %Y" }}
            </div>
            <div class="issue-highlights">
                <strong>This week's highlights:</strong> {{ latest_newsletter.total_stories }} stories across 
                {% if latest_newsletter.security_count > 0 %}cybersecurity,{% endif %}
                {% if latest_newsletter.ai_count > 0 %} AI breakthroughs,{% endif %}
                {% if latest_newsletter.health_count > 0 %} digital health innovations,{% endif %}
                {% if latest_newsletter.pm_count > 0 %} product management insights,{% endif %}
                {% if latest_newsletter.finance_count > 0 %} and market trends{% endif %}.
            </div>
        </div>
        
        <div class="cta-buttons">
            <a href="{{ latest_newsletter.url }}" class="btn">📖 Read This Week's Edition</a>
            <a href="/newsletter.xml" class="btn btn-outline">📡 Subscribe via RSS</a>
        </div>
    </section>
    {% endif %}

    <section class="rss-info">
        <h3>🚀 Subscribe via RSS</h3>
        <p>Get every issue delivered automatically to your preferred RSS reader. No email signup required!</p>
        
        <div class="rss-url">
            <strong>RSS Feed:</strong> https://vitraag.com/newsletter.xml
        </div>
        
        <p><strong>Popular RSS Readers:</strong></p>
        <div class="rss-readers">
            <a href="https://feedly.com" target="_blank" class="rss-reader">
                <div><strong>Feedly</strong></div>
                <div>Web + Mobile</div>
            </a>
            <a href="https://www.inoreader.com" target="_blank" class="rss-reader">
                <div><strong>Inoreader</strong></div>
                <div>Advanced Features</div>
            </a>
            <a href="https://netnewswire.com" target="_blank" class="rss-reader">
                <div><strong>NetNewsWire</strong></div>
                <div>Mac + iOS</div>
            </a>
            <a href="https://reederapp.com" target="_blank" class="rss-reader">
                <div><strong>Reeder</strong></div>
                <div>Beautiful UI</div>
            </a>
        </div>
        
        <p><em>New to RSS? It's a simple way to follow your favorite websites without email subscriptions. 
        Just add our RSS URL to any RSS reader and get updates automatically!</em></p>
    </section>

    {% assign recent_newsletters = site.newsletters | default: empty | sort: 'date' | reverse | limit: 6 %}
    {% if recent_newsletters.size > 0 %}
    <section class="recent-issues">
        <h2>Recent Editions</h2>
        
        <div class="issues-grid">
            {% for newsletter in recent_newsletters limit: 3 %}
            <div class="issue-card">
                <h3>Issue #{{ newsletter.issue_number }}</h3>
                <div class="date">{{ newsletter.date | date: "%B %d, %Y" }}</div>
                <div class="summary">
                    {{ newsletter.total_stories }} curated stories covering the week's biggest tech developments
                    {% if newsletter.security_count > 0 %}• {{ newsletter.security_count }} security stories{% endif %}
                    {% if newsletter.ai_count > 0 %}• {{ newsletter.ai_count }} AI developments{% endif %}
                    {% if newsletter.health_count > 0 %}• {{ newsletter.health_count }} health tech updates{% endif %}
                </div>
                <a href="{{ newsletter.url }}" class="read-link">Read Issue →</a>
            </div>
            {% endfor %}
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <a href="/newsletter/archive" class="btn btn-outline">📂 View All Editions</a>
        </div>
    </section>
    {% endif %}

    <section class="newsletter-stats">
        <h2>By the Numbers</h2>
        <div class="stats-grid">
            <div class="stat-item">
                <span class="stat-number">{{ site.newsletters.size | default: "0" }}</span>
                <span class="stat-label">Issues Published</span>
            </div>
            <div class="stat-item">
                {% assign total_stories = 0 %}
                {% if site.newsletters %}
                    {% for newsletter in site.newsletters %}
                        {% assign total_stories = total_stories | plus: newsletter.total_stories %}
                    {% endfor %}
                {% endif %}
                <span class="stat-number">{{ total_stories | default: "0" }}</span>
                <span class="stat-label">Stories Curated</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">5</span>
                <span class="stat-label">Tech Categories</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">Weekly</span>
                <span class="stat-label">Publishing Schedule</span>
            </div>
        </div>
    </section>

    <section class="why-rss">
        <h2>Why RSS?</h2>
        <div class="benefits-list">
            <div class="benefit-item">
                <div class="benefit-icon">✅</div>
                <div class="benefit-text">
                    <strong>No Email Clutter</strong><br>
                    Keep your inbox clean while staying informed
                </div>
            </div>
            <div class="benefit-item">
                <div class="benefit-icon">🔒</div>
                <div class="benefit-text">
                    <strong>Privacy First</strong><br>
                    No tracking, no ads, no data collection
                </div>
            </div>
            <div class="benefit-item">
                <div class="benefit-icon">📱</div>
                <div class="benefit-text">
                    <strong>Your Choice of Reader</strong><br>
                    Use any RSS reader you prefer
                </div>
            </div>
            <div class="benefit-item">
                <div class="benefit-icon">📴</div>
                <div class="benefit-text">
                    <strong>Offline Reading</strong><br>
                    Most RSS readers support offline access
                </div>
            </div>
            <div class="benefit-item">
                <div class="benefit-icon">⚡</div>
                <div class="benefit-text">
                    <strong>Never Miss an Issue</strong><br>
                    Automatic delivery to your reader
                </div>
            </div>
            <div class="benefit-item">
                <div class="benefit-icon">🆓</div>
                <div class="benefit-text">
                    <strong>Always Free</strong><br>
                    No premium tiers or subscription fees
                </div>
            </div>
        </div>
    </section>

    <div style="text-align: center; margin: 4rem 0; padding: 2rem; border: 2px solid #000;">
        <h3 style="font-family: 'Playfair Display', serif; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1rem;">
            Ready to Stay Informed?
        </h3>
        <p style="margin-bottom: 2rem; color: #666;">
            Join readers who trust my weekly curation to stay ahead of tech trends.
        </p>
        <a href="/newsletter.xml" class="btn" style="margin-right: 1rem;">📡 Subscribe to RSS Feed</a>
        {% if latest_newsletter %}
        <a href="{{ latest_newsletter.url }}" class="btn btn-outline">📖 Read Latest Issue</a>
        {% endif %}
    </div>
</div>