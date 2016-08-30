<!DOCTYPE html>
<html>
	<head>
  
	<style type="text/css">
    html, body{height: 100%; margin: 0; padding: 0;}

	#map,#camera{
		height: 100%;
		width: 50%;
		float: left;

	}
	
	label{
		position: absolute;
		top:45%;
		left: 16%;
		font-size: 50px;
		/*border: 2px dashed #f00;*/
	}

    </style>
  
	<title>Client</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
	<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
	
    <audio id = "dingsound">
		<source src="Airplane-ding-sound.mp3" type="audio/mpeg">
	</audio>
	
    <script>
		var apiKey = 'AIzaSyDyHM6h1-cWPrgOu5nHcIEMA0XqF16OQUU';
		var map;

		var p = new google.maps.Polyline({ map: map, strokeColor: '#4986E7' });

		var image = {
			url: 'car.png',
			size: new google.maps.Size(32, 35),
			origin: new google.maps.Point(0, 0),
			anchor: new google.maps.Point(0, 32)
		};

		var eventimage = {
			url: 'caution.png',
			size: new google.maps.Size(32,35),
			origin: new google.maps.Point(0,0),
			anchor: new google.maps.Point(0,32)
		};
  
		var marker = new google.maps.Marker({icon:image});
		var warningmassage = '請降低車速'; 
		var snappedCoordinates = [];
		var pathValues = [];
		var centerlat = 53.749314;
		var centerlng = -2.487953;
		
		var originalcol = 'rgb(65, 105, 225)';
		var changecol = 'rgb(255, 255, 255)';
		


		function runSnapToRoad() {
			$.get('https://roads.googleapis.com/v1/snapToRoads', {
			interpolate: true,
			key: apiKey,
			path: pathValues.join('|')
		}, function(data) {
			
			processSnapToRoadResponse(data);
			drawSnappedPolyline();
			});
		}

		function processSnapToRoadResponse(data) {
			snappedCoordinates = [];
			placeIdArray = [];
			for (var i = 0; i < data.snappedPoints.length; i++) {
				var latlng = new google.maps.LatLng(
				data.snappedPoints[i].location.latitude,
				data.snappedPoints[i].location.longitude);
				snappedCoordinates.push(latlng);
				placeIdArray.push(data.snappedPoints[i].placeId);
				}
			marker.setPosition(snappedCoordinates[snappedCoordinates.length-1]);
		}

		function drawSnappedPolyline() {
			snappedPolyline = new google.maps.Polyline({
				path: snappedCoordinates,
				strokeColor: '#007fff',
				strokeWeight: 3
			});
			snappedPolyline.setMap(map);
		}

  
		function initialize() {
			var cen = new google.maps.LatLng(24.97025667,121.26703);
			var myOptions = {
				zoom: 18,
				mapTypeId: google.maps.MapTypeId.ROADMAP,
				center: cen
			}
			map = new google.maps.Map(document.getElementById("map"), myOptions);
		};

		function setlinepath(temp){
			pathValues.push(temp);
		 }
		  
		
		function updatemap(newlat,newlng)
		{
		  pathValues.push(newlat.toString() + ',' + newlng.toString());
		  runSnapToRoad();
		  marker.setMap(map);
		  map.setCenter(snappedCoordinates[snappedCoordinates.length-1]);
		   console.log(map)
		}

		function markevent(description)
		{
		  var eventmarker = new google.maps.Marker({
		   icon: eventimage,
		   position: snappedCoordinates[snappedCoordinates.length-1],
		   Title: description,
		   Map: map});
		 
		}
		function popwarning(description)
		{  
		   warningcontrol.innerHTML= description;
		   var blink = setInterval(function() {
			  warningcontrol.style.display = (warningcontrol.style.display == 'none' ? '' : 'none');
		   }, 500);
		   setTimeout(function(){clearInterval(blink);warningcontrol.innerHTML='';warningcontrol.style.display='';},2700);
		}
		
		function eventopanel(description){
		$("#eventpanel").append("<div class = 'event' onclick = 'remove();' > "+description+" </div>")
		$(".event").hover(function(){
			$(this).css("background-color",originalcol);}
			,function(){$(this).css("background-color",changecol);}
		)}
		
	    var ding = document.getElementById("dingsound");
		
	  
	    var ding = document.getElementById("dingsound");
		function voicewarning(description){
			ding.src = "Airplane-ding-sound.mp3";
			ding.play();
			var count = 0;
			dingsound.onended = function(){
				if(count<1){
					count = count +1;
					ding.src = description + '.mp3';
					ding.play();}
				else{
					ding.pause();}
				};
		}
  
</script>  
</head>
 
<body>
	<div id = "camera">
		<label>no signal..</label>
	</div>
	<div id = "map"></div>
	
	<script>
	initialize();
	marker.setPosition(new google.maps.LatLng(24.97025667,121.26703))
	marker.setMap(map);
	setTimeout(function(){
		pathValues.push('24.97025667,121.26703');
		runSnapToRoad();
	},3000);
	setTimeout(function() {updatemap(24.97021833,121.267185);},5000);
	setTimeout(function() {updatemap(24.96999833,121.2672867);},7000);
	setTimeout(function() {updatemap(24.96984167,121.26743);},9000);
	setTimeout(function() {updatemap(24.96917667,121.2674583);},13000);
	/*
    
	
	setTimeout(function() {updatemap(53.748609, -2.486473);},3000);
	setTimeout(function() {updatemap(53.748712, -2.486549);},3000);
	setTimeout(function() {updatemap(53.748842, -2.486517);},3000);
	setTimeout(function() {updatemap(53.748848, -2.486383);},3000);
	*/

	</script>
		
</body>
</html>