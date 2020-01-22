---
layout: default
title: Blog HeatMap
permalink: /data/
categories:
- data
---
Heatmap of all posts.
<script src="https://d3js.org/d3.v5.min.js"></script>
<script>
    var data = [5]
    var canvas = d3.select("body").append("svg").attr("width", 500).attr("height", 500)
    var canvas = canvas.append("circle").attr("cx",100).attr("cy",100).attr("r",25).attr("fill", "red")
</script>