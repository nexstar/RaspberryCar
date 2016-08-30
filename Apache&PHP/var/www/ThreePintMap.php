<?php

	$count = 0;
	++$count;
	//$Point = "24.97025667,121.26703";
	$Longitude = 24.97025667; 
	$Latitude = 121.26703;
	
?>

<html>
<head>
<title>ThreePintMap</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <script src="jquery-1.9.1.js"></script>
<script src="http://maps.google.com/maps?file=api&amp;v=2&amp;key=ABQIAAAAG_4i2swR3KOd-nGYrlrt8RTkyS8SRe_kYPTAbwTumvAqao01PRRUcCtCzTBnNH2kRURGR8RhQQoZ3w"
      type="text/javascript"></script>

<script type="text/javascript">

function load() {

	if (GBrowserIsCompatible()) {
		var myMap = new GMap2(document.getElementById("map"));
		var myLatLng = new GLatLng(<?php echo $Longitude;?>,<?php echo $Latitude;?>);
	
		myMap.setCenter(myLatLng, 18);
		myMap.addControl(new GLargeMapControl());
		
		var myMarker = new GMarker( myLatLng );
		myMap.addOverlay( myMarker );
		var count = 1;
		GEvent.addListener(myMap, "click", function( overlay, point ){
			var NewArray = new Array();
			if(point){ //設定標註座標
				myMarker.setLatLng(point);
				NewArray = point.toString().substr(1,37).split(',');
				var p = document.createElement("p");
				
				var text = document.createTextNode(count+".");
    			p.appendChild(text);
    			
				var input = document.createElement("input");

				input.setAttribute("id","A"+count);
				input.setAttribute("type","text");
				input.setAttribute("name",count);
				input.setAttribute("value",NewArray[0]+","+NewArray[1]);

			    document.getElementById('formInput').appendChild(p);
			    document.getElementById('formInput').appendChild(input);
			    
			    var br =document.createElement('br');
			    document.getElementById('formInput').appendChild(br);    
			    count++;
			    
			}
		});
	}
}

//]]>
</script>
<style type="text/css">
	input{
		width:330px;
		text-align: center;
	}

	#Input{
		position: absolute;
		left: 1.5%;
	}

	#Content{
		position: relative;
		width:80%;
		height: 100%;
	}

	#map{
		left: 36%;
		width: 87%;
		height: 100%;
		position: fixed;
		bottom:0;
	}

</style>
</head>
<body  onload="load()" onunload="GUnload()">
	<div id="Content">
		<div id="Input">
			<form ation="?" id="formInput">
			
			</form>
			<button>Sent Data</button>
		</div>
		<div id="map"></div>
	</div>
</body>
</html>