var chord = d3.char.layout.chord();

var arc = d3.svg.arc();

var svg = d3.select("body").append("svg")

d3.json("matrix.json", function(error, json) {
    if (error) throw error;

    matrix = json;

    chord.matrix(matrix);

    var group = svg.selectAll(".group")
    .data(chord.groups)
    .enter().append("g")
    .attr("class", "group");

    var groupPath = group.append("path")
    .attr("id", function(d, i) { return "group" + i; })
    .attr("d", arc)

    var links = svg.selectAll(".chord")
    .data(layout.chords)
    .enter().append("path")
    .attr("class", "chord")
    .attr("d", path);
}

