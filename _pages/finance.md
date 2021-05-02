---
layout: report
title: Monthly Finance Report
permalink: /finance/
aside:
    metrics:
        - name: Transactions
          value: 100
        - name: Income
          value: 5k
        - name: Expense
          value: 3k
        - name: Investments
          value: 2k
    menuitems:
        - label: Monthly Finances 
          list: 
            - label: Dashboard
              link: 
            - label: Customers
              link:
        - label: Review Items
          list:
            - label: Business
              link:
            - label: Vendors
              link: 
            - label: Recurring Bills
              link: 
    fincat:
        - HSA
        - 
categories:
- finance
---
 <div class="container">
        <div class="columns">
            <div class="column is-3 ">
                <aside class="menu is-hidden-mobile">
                {% for menu in page.aside.menuitems %}
                    <p class="menu-label">
                        {{menu.label}}
                    </p>
                    <ul class="menu-list">
                    {% for item in menu.list %}
                        <li><a href='{{item.link}}'>{{item.label}}</a></li>
                    {% endfor %}
                    </ul>
                {% endfor %}
                </aside>
            </div>
            <div class="column is-9">
                <div class="container">
                    <a href="{{site.url}}/finances/?month=1" class="tag is-info">Jan</a>
                </div>
                <section class="hero is-info welcome is-small">
                    <div class="hero-body">
                        <div class="container">
                            <h1 class="title">
                                Hello, Vaibhav.
                            </h1>
                            <h2 class="subtitle">
                                I hope you are having a great day. Good Morning!
                            </h2>
                        </div>
                    </div>
                </section>
                <section class="info-tiles" id="dashboard">
                    <div class="tile is-ancestor has-text-centered">
                    {% for metric in page.aside.metrics %}
                        <div class="tile is-parent">
                            <article class="tile is-child box">
                                <p class="title">{{metric.value}}</p>
                                <p class="subtitle">{{metric.name}}</p>
                            </article>
                        </div>
                    {% endfor %}
                    </div>
                </section>
                <div class="columns">
                    <div class="column is-6">
                        <div class="card events-card">
                            <header class="card-header">
                                <p class="card-header-title">
                                    Transactions
                                </p>
                                <a href="#" class="card-header-icon" aria-label="more options">
                                    <span class="icon">
                                        <i class="fa fa-angle-down" aria-hidden="true"></i>
                                    </span>
                                </a>
                            </header>
                            <div class="card-table">
                                <!-- React App is working -->
                                <div id="react">
                                </div>
                                <div class="content">
                                    <table class="table is-fullwidth is-striped">
                                        <tbody>
                                            <tr>
                                                <td width="5%"><i class="fa fa-bell-o"></i></td>
                                                <td>Lorum ipsum dolem aire</td>
                                                <td><a class="button is-small is-primary" href="#">Action</a></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            <footer class="card-footer">
                                <a href="#" class="card-footer-item">View All</a>
                            </footer>
                        </div>
                    </div>
                    <div class="column is-6">
                        <div class="card">
                            <header class="card-header">
                                <p class="card-header-title">
                                    Merchant Search
                                </p>
                                <a href="#" class="card-header-icon" aria-label="more options">
                                    <span class="icon">
                                        <i class="fa fa-angle-down" aria-hidden="true"></i>
                                    </span>
                                </a>
                            </header>
                            <div class="card-content">
                                <div class="content">
                                    <div class="control has-icons-left has-icons-right">
                                        <input class="input is-large" type="text" placeholder="">
                                        <span class="icon is-medium is-left">
                                            <i class="fa fa-search"></i>
                                            </span>
                                            <span class="icon is-medium is-right">
                                            <i class="fa fa-check"></i>
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="card">
                            <header class="card-header">
                                <p class="card-header-title">
                                    Location Search
                                </p>
                                <a href="#" class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <i class="fa fa-angle-down" aria-hidden="true"></i>
                  </span>
                </a>
                            </header>
                            <div class="card-content">
                                <div class="content">
                                    <div class="control has-icons-left has-icons-right">
                                        <input class="input is-large" type="text" placeholder="">
                                        <span class="icon is-medium is-left">
                      <i class="fa fa-search"></i>
                    </span>
                                        <span class="icon is-medium is-right">
                      <i class="fa fa-check"></i>
                    </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

