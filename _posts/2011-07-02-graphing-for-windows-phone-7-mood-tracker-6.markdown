---
author: vitraag
comments: true
date: 2011-07-02 00:41:25+00:00
layout: post
link: https://vitraagblog.wordpress.com/2011/07/01/graphing-for-windows-phone-7-mood-tracker-6/
slug: graphing-for-windows-phone-7-mood-tracker-6
title: 'Graphing for Windows Phone 7– Mood Tracker #6'
wordpress_id: 347
categories:
- Mobile
- MoodTracker
---

Wishing every one a happy independence day!

 

In the last post we [enabled](http://healthblog.vitraag.com/2011/06/entering-new-data-with-mood-tracker-5/) Mood Tracker to enter new data in to HealthVault. Before I start this post in details of adding graphing layer let me motivate it by showing what the graph for Mood Tracker looks like -

 

[![image]({{site.images}}/2011/07/image_thumb.png)]({{site.images}}/2011/07/image.png)

 

Fig 1. Graphing Over the 7 days

 

The interesting aspect here is that we are tracking Mood, Stress and Wellbeing over a period of one week, and looking for patterns in terms of mood, stress and wellbeing correlations. There are better ways to do graphing for this data but this is a simplistic approach.

 

In order to be able to get data from HealthVault for a specific time period we will have to update the implementation of our [GetThings](https://github.com/vaibhavb/moodtracker/blob/master/MoodTracker/HealthVaultMethods.cs) method to allow for a filter for effective date max and min. Notice the interesting formatting we need to do to make DateTime serializable.

 
    
    <span class="kwrd">private</span> <span class="kwrd">static</span> <span class="kwrd">string</span> EffDateMinXml(DateTime? effDateMin)
    {
        <span class="kwrd">if</span> (effDateMin != <span class="kwrd">null</span>)
            <span class="kwrd">return</span>
                <span class="kwrd">string</span>.Format(<span class="str">@"<eff-date-min>{0}</eff-date-min>"</span>,
                    effDateMin.Value.ToString(<span class="str">"yyyy-MM-ddTHH:mm:ss.FFFZ"</span>,
                                CultureInfo.InvariantCulture)
                    );
        <span class="kwrd">else</span> <span class="kwrd">return</span> <span class="str">""</span>;
    }







.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }Once we are powered with a way to selectively get information from HealthVault we can simply make use of the awesome open-source amCharts library. Infact I added it to the project with one-click using [NuGet Package manager](http://www.nuget.org/List/Packages/amChartsQuickCharts) (note to self: may be post a version of HealthVault Windows Phone library on NuGet). Here is a snippet of how I configured the SerialChart.




    
    <p><span class="kwrd"><</span><span class="html">amq:SerialChart</span> <span class="attr">x:Name</span><span class="kwrd">="EmotionsChart"</span>
                    <span class="attr">BorderThickness</span><span class="kwrd">="1"</span>
                    <span class="attr">DataSource</span><span class="kwrd">="{Binding EmotionList}"</span> 
                    <span class="attr">CategoryValueMemberPath</span><span class="kwrd">="FormattedWhen"</span>
                    <span class="attr">AxisForeground</span><span class="kwrd">="White"</span>
                    <span class="attr">PlotAreaBackground</span><span class="kwrd">="Black"</span>
                    <span class="attr">GridStroke</span><span class="kwrd">="DarkGray"</span> <span class="attr">Height</span><span class="kwrd">="463"</span> <span class="attr">Width</span><span class="kwrd">="450"</span><span class="kwrd">></span>
        <span class="kwrd"><</span><span class="html">amq:SerialChart.Graphs</span><span class="kwrd">></span>
            <span class="kwrd"><</span><span class="html">amq:LineGraph</span> <span class="attr">ValueMemberPath</span><span class="kwrd">="Mood"</span> 
                            <span class="attr">Title</span><span class="kwrd">="Mood"</span> <span class="attr">Brush</span><span class="kwrd">="Blue"</span>
                            <span class="attr">StrokeThickness</span><span class="kwrd">="6"</span>
                            <span class="attr">BorderBrush</span><span class="kwrd">="Cornsilk"</span><span class="kwrd">/></span>
            <span class="kwrd"><</span><span class="html">amq:LineGraph</span> <span class="attr">ValueMemberPath</span><span class="kwrd">="Stress"</span> 
                            <span class="attr">Title</span><span class="kwrd">="Stress"</span> <span class="attr">Brush</span><span class="kwrd">="#8000FF00"</span> 
                            <span class="attr">StrokeThickness</span><span class="kwrd">="8"</span> <span class="kwrd">/></span>
            <span class="kwrd"><</span><span class="html">amq:LineGraph</span> <span class="attr">ValueMemberPath</span><span class="kwrd">="Wellbeing"</span> 
                            <span class="attr">Title</span><span class="kwrd">="Wellbeing"</span> 
                            <span class="attr">StrokeThickness</span><span class="kwrd">="2"</span>
                            <span class="attr">Brush</span><span class="kwrd">="#80FF0000"</span><span class="kwrd">/></span>
        <span class="kwrd"></</span><span class="html">amq:SerialChart.Graphs</span><span class="kwrd">></span>
    <span class="kwrd"></</span><span class="html">amq:SerialChart</span><span class="kwrd">></span></p><p><span class="kwrd"></span> </p>




.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }



Note that the formatting for the X-Axis is derived by a special property we added to the [EmotionalStateModel](https://github.com/vaibhavb/moodtracker/blob/master/MoodTracker/EmotionalStateModel.cs), it probably is not the right place to add that property.





Over last few days I have implemented an interesting idea to make entering emotional state information easier similar in themes as the original mood tree but more focused on making data entry fun , I call it vMudi.





So next time w’ll look at vMudi.
