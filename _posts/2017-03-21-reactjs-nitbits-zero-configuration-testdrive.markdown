---
author: vitraag
comments: true
date: 2017-03-21 20:26:11+00:00
layout: post
link: https://vitraagblog.wordpress.com/2017/03/21/reactjs-nitbits-zero-configuration-testdrive/
slug: reactjs-nitbits-zero-configuration-testdrive
title: Reactjs Nitbits — Zero Configuration TestDrive
wordpress_id: 1552
categories:
- ramblings
tags:
- JavaScript
- React
---





The goal of this post is to document my experience of starting to code a react application without much experience. The simple app will have a responsive interface to enable me to log how much water I drink to a google spreadsheet. I would like to host the application either on github or s3.




### **Minimum Viable React Unit**




Step 1. Start with the **facebook** getting started one page app **template**



    
    > sudo npm install -g create-react-app




Step 2: Create the water-logger app



    
    > create-react-app water-app<br></br>> npm start




Step 3: Deploy to **github pages**




The react documentation has a few steps to deploy it to github pages by specifying the _homepage _field. Once the repository is created, and the homepage defined (so much for zero configuration) you can deploy the application.



    
    > npm run deploy




**Voila!**




![](https://vitraagblog.files.wordpress.com/2017/03/7ce08-1j46jw2c7zppvenysy59kqg.png)

The one-page all up and running!

### Next Steps




Now we need to add the buttons, and support the capability of storing information in google sheets to complete our minimum-viable-product.



