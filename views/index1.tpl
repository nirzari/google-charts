<html>
  <head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js" charset="utf-8"></script>
    <script type="text/javascript">
    $( document ).ready(function() {
             console.log("document.ready called")
   	         $("#next").click(function(){   
                                          window.location.replace("/");          
   });
   });   
      var chartdata = localStorage.getItem("chartdata");
      console.log(chartdata);   
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable($.parseJSON(chartdata));

        var options = {
          title: 'My Grade Distribution',
          is3D: true,
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body background="http://smartlabs.lewistonschools.net/jenifer/StudentProjects/StudentAnimationProjects/Pencil%20Animation.gif">
    <div id="next">
    <input type="button" id="next" value="Select another student">
    </div>
     <div id="piechart_3d" style="width: 900px; height: 500px;"></div>
  </body>
</html>