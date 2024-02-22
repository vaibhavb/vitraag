        var width = 600, height = 400;

        var projection = d3.geoMercator()
                           .scale(80)
                           .translate([width / 2, height / 2]); 

        var path = d3.geoPath().projection(projection); 

        var svg = d3.select("#map")
                    .append("svg")
                    .attr("width", width)
                    .attr("height", height);

        d3.json("https://unpkg.com/world-atlas@2.0.2/countries-110m.json") 
          .then(data => {
              svg.selectAll("path")
                 .data(topojson.feature(data, data.objects.countries).features)
                 .enter()
                 .append("path")
                 .attr("d", path)
                 .style("fill", "lightblue")
                 .style("stroke", "gray");
          });
