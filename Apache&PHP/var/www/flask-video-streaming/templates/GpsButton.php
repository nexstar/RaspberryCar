<?php
$Longitude = 24.97025667; 
$Latitude = 121.26703;
?>
<html>
<head>
<title>GpsButton</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <script src="jquery-1.9.1.js"></script>
    <script type="text/javascript">
    		
    		function myFunction() {
			    location.href = 'ThreePintMap.php';
			}

    </script>
<style type="text/css">
	

	div{
		position: absolute;
		top:25%;
		left: 20%;
		width:60%;
		text-align: center;

	}

	#GPS{
		position: relative;
		width:400px;
		height:250px;
		font-size:70px;
	}
	#sent{
		position: absolute;
		width:100px;
		left: 90%;
		top:80%;
	}


	#XXX{
		position: relative;
		height:150px;
		text-align: center;
	}
	table{
		position: absolute;
		top:25%;
	
	}

	table, th, td {
		text-align: center;
		border: 1px solid black;
	}

	td{
		width:500px;
		text-align: center;
	}
</style>

</head>
<body>
	<div>
		<button id = "GPS">GPS</button>
		<div id ="XXX">
			<table>
				<tr>
			    	<th>Longitude</th>
			    	<th>Latitude</th>
				</tr>
				<tr>
					<td><?php echo $Longitude?></td>
					<td><?php echo $Latitude?></td>
				</tr>
			</table>

			
<button id="sent" onclick="myFunction()" <?php echo (isset($_GET['YN'])==1)? "":"disabled";?> >Get it</button>
			
		</div>
	</div>
</body>
</html>