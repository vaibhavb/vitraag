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
              // Define the countries to highlight
              var highlightCountries = ["India", "United States of America", "Germany", "Japan", "Spain", "Peru", "Mexico", "Ecquador", "Chile", "Canada", "Egypt", "UK", "Ireland", "Australia", "Indonesia", "Hongkong", "Columbia", "Turkey", "Costa Rica", "Thailand"];

              // Convert TopoJSON to GeoJSON
              var countries = topojson.feature(data, data.objects.countries).features;

              // Draw each country
              svg.selectAll("path")
                 .data(countries)
                 .enter()
                 .append("path")
                 .attr("d", path)
                 .attr("fill", function(d) {
                    // Check the country name against the highlight list
                    var name = d.properties.name;
                    if (highlightCountries.includes(name)) {
                        return "red"; // Highlight color
                    } else {
                        return "lightblue"; // Default color
                    }
                 })
                 .style("stroke", "gray");
          });
