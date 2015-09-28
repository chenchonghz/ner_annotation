var d3 = require('d3');

var zh_CN = {
  "decimal": ".",
  "thousands": ",",
  "grouping": [3],
  "currency": ["￥", ""],
  "dateTime": "%Y %b %e %X",
  "date": "%Y %B %e",
  "time": "%H:%M:%S",
  "periods": ["AM", "PM"],
  "days": ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"],
  "shortDays": ["周日", "周一", "周二", "周三", "周四", "周五", "周六"],
  "months": ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"],
  "shortMonths": ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
}
var CN = d3.locale(zh_CN);

var margin = {top: -5, right: 20, bottom: 35, left: 20},
    width = 960 - margin.left - margin.right,
    height = 120 - margin.top - margin.bottom;
var expansionRatio = 0.05;
var iconWidth = 15, iconHeight = 50;

var parseDate = d3.time.format("%Y-%m-%d %H:%M:%S").parse;

var x = d3.time.scale().range([0, width]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .ticks(5)
    .tickFormat(CN.timeFormat("%Y年%b%-d号"));

var arc = d3.svg.arc()
    .outerRadius(iconHeight / 2 - 2)
    .startAngle(0)
    .endAngle(function(d, i) { return i ? -Math.PI : Math.PI; });

var d3Timeline = {}

d3Timeline.drawTimeline = function(notes, active, onBrush) {
  var brush = d3.svg.brush()
      .x(x);
  brush.on("brush", onBrush(brush));

  var svg = d3.select(".timeline .panel-content").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
  var innerContainer = svg.append("g")
      .attr("transform", "translate(" + (margin.left + 25) + "," + margin.top + ")")
    .append("g");

  var svgContainer = d3.select(svg.node().parentNode);

  var data = notes.map(function(d) { return parseDate(d.date); });
  var extent = d3.extent(data);
  var expanedExtent = [
    new Date(+extent[0] - (extent[1] - extent[0]) * expansionRatio),
    new Date(+extent[1] + (extent[1] - extent[0]) * expansionRatio)
  ];
  x.domain(expanedExtent);

  var notesContainer = innerContainer.append("g");
  var brushContainer = innerContainer.append("g");

  notesContainer
    .selectAll("g")
      .data(data)
    .enter().append("g")
      .attr("transform", function(d) { return "translate(" + x(d) + "," + 0 + ")"; })
    .append("rect")
      .attr("class", function(d, i) {
        if (i === active) {
          return "note active";
        } else {
          return "note";
        }
      })
      .attr("width", function(d) { return iconWidth; })
      .attr("height", function(d) { return iconHeight; });

  var axis = innerContainer.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + iconHeight + ")")
    .call(xAxis);

  brushContainer
      .attr("class", "brush")
      .call(brush)
    .selectAll("rect")
      .attr("height", iconHeight+2);

  brushContainer
    .selectAll(".resize").append("path")
      .attr("transform", "translate(0," +  (iconHeight / 2 + 4) + ")")
      .attr("d", arc);

  d3.select(window).on("resize." + svgContainer.attr("id"), resize);

  resize();

  function resize() {
    var targetWidth = parseInt(svgContainer.style("width")) - 40;
    svg.attr("width", targetWidth);
    x.range([0, targetWidth - 20]);
    notesContainer
      .selectAll("g")
        .data(data)
        .attr("transform", function(d) { return "translate(" + x(d) + "," + 0 + ")"; });
    xAxis.scale(x);
    axis.call(xAxis);
    brush.x(x);
    brushContainer.call(brush);
  }
}

d3Timeline.updateActiveNote = function(active) {
  d3.select(".timeline .panel-content svg g g g")
    .selectAll("g")
    .select("rect")
      .attr("class", function(d, i) {
        if (i === active) {
          return "note active";
        } else {
          return "note";
        }
      })
}

module.exports = d3Timeline;