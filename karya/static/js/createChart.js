"use strict;"

var chart;

/*This function helps convert raw data from Django
  to meaningful data for tehe nvd3.js */
function generateData() {
  var sin = [];
  var x = window.x;
  var y = window.y;


  for(var i = 0; i < x.length; i++)
  {
    sin.push({ x:x[i], y:y[i] });
  }

  //Returns an object to map the set of data points
  return [
    {
      area:true,
      values: sin,
      key: window.company,
    }
  ]
}

/* Generates the chart using the data supplied
http://nvd3.org/examples/line.html used as reference to create 
the function */

nv.addGraph(function() {
  var data = generateData();
  chart = nv.models.lineChart()
  .options({
    margin: {left: 100, bottom: 100},
    showXAxis: true,
    showYAxis: true,
    transitionDuration: 250
  });

  // chart sub-models (ie. xAxis, yAxis, etc) 
  chart.xAxis
      .showMaxMin(false)
      .axisLabel('Date (m/d/y)')
      .tickFormat(function(d) {
        return d3.time.format('%m/%d/%Y')(new Date(d))
      });

  chart.yAxis
    .axisLabel('Price ($)')
    .tickFormat(d3.format(',.2f'));

  d3.select('#chart1 svg')
    .datum(data)
    .call(chart);

  nv.utils.windowResize(chart.update);

  chart.dispatch.on('stateChange', function(e) { nv.log('New State:', JSON.stringify(e)); });

  return chart;
});