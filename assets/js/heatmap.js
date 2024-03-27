function createCommitGraph() {
    var commitGraph = document.getElementById("commit-graph");
    console.log(commitGraph);

    var days = ["M", "T", "W", "Th", "F", "S", "Su"];

    for (var j = 0; j < 7; j++) {
    // 7 days in a week
    var week = document.createElement("div");
    week.classList.add("week");

    var dayLabel = document.createElement("div");
    dayLabel.classList.add("day");
    dayLabel.textContent = days[j];
    week.appendChild(dayLabel);

    for (var i = 0; i < 52; i++) {
        // assuming 52 weeks in a year
        var commit = document.createElement("div");
        commit.classList.add("commit");
        var commits = Math.floor(Math.random() * 5); // Random number of commits between 0 and 4
        if (commits > 0) {
        commit.style.backgroundColor = "hsl(120, " + commits * 20 + "%, 50%)";
        } else {
        commit.style.backgroundColor = "#eee"; // Color for days without commits
        }
        week.appendChild(commit);
    }

    commitGraph.appendChild(week); // Append the week to the graph
    }
}

document.addEventListener("DOMContentLoaded", createCommitGraph)
