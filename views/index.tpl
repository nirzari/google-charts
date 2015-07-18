<html>
<head>
<script type="text/javascript" src="https://www.google.com/jsapi"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js" charset="utf-8"></script>
<script type="text/javascript">
$( document ).ready(function(){
	                           $("#pie").click(function(){
                               console.log("Button clicked");
                               var dataobj = {"sid": $("#sid").val()}; 
    			                     $.ajax({
				                            type: "POST",
        			                      url: "/pie",
        			                      data: dataobj,
     			                          success: function(data,status)
                                     {          
                                      localStorage.setItem("chartdata",data);
                                      window.location.replace("/pie_chart");
                                     }			    
     
                                      });	
  
  });
});

window.onload = function () {
    var select = document.getElementById("sid");
    for(var i = 1; i < 51; i++) {
        var option = document.createElement('option');
        option.text  = i;
        select.add(option, 0);
    }
};
</script>
</head>
<body background="http://www.zastavki.com/pictures/1920x1200/2009/3D-graphics_Charts_017984_.jpg">
<h2>Plot a pie chart </h2>
<br> 
Select student ID: <select id="sid" name="sid"></select>
<br>
<br>
<input type="button" id="pie" value="Plot PieChart">
<br>
<p>Note: Students have appeared for their midterm exam. <br> This pie chart shows every student's grade distribution <br> in all subjects. </p>
</body>
</html>