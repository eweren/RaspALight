<?php
###############################################################################
// Try catch blocks for the color, the time of an alarm and the abortion

$recoveredData = file_get_contents('Scripts/init.save');
$init_array = unserialize($recoveredData);

$recoveredData1 = file_get_contents('Scripts/alarms.save');
$alarms_array = unserialize($recoveredData1);

###############################################################################
###################Catching the colors of the color-picker#####################
try{
  if(isset($_POST['color'])){
    $color=$_POST['color'];
    $color = str_replace("#", "", $color);
    $r = hexdec(substr($color,0,2));
    $g = hexdec(substr($color,2,2));
    $b = hexdec(substr($color,4,2));
    #$execute = shell_exec("python Scripts/setColor.py $r $g $b");
  }
} catch(Exception $e){
  $color="";
}
###############################################################################
############################Catch the alarm time###############################
try{
  if(isset($_POST['time']) && isset($_POST['date']) && isset($_POST['duration'])){
    $h = substr($_POST['time'],0,2);
    $m = substr($_POST['time'],3,2);
    $date = $_POST['date'];
    $dur = $_POST['duration'];
    $day=substr($date,8,2);
    $month=substr($date,5,2);
    $year=substr($date,0,4);
    $cut = $init_array['cut_off_time'];
	$monday = "0";
	$tuesday = "0";
	$wednesday = "0";
	$thursday = "0";
	$friday = "0";
	$saturday = "0";
	$sunday = "0";
	if(isset($_POST['monday'])){
    if($_POST['monday']!=""){
		    $monday = $_POST['monday'];
    }
	}
  if(isset($_POST['tuesday'])){
    if($_POST['tuesday']!=""){
		    $tuesday = $_POST['tuesday'];
    }
	}
  if(isset($_POST['wednesday'])){
    if($_POST['wednesday']!=""){
		    $wednesday = $_POST['wednesday'];
    }
	}
  if(isset($_POST['thursday'])){
    if($_POST['thursday']!=""){
		    $thursday = $_POST['thursday'];
    }
	}
  if(isset($_POST['friday'])){
    if($_POST['friday']!=""){
		    $friday = $_POST['friday'];
    }
	}
  if(isset($_POST['saturday'])){
    if($_POST['saturday']!=""){
		    $saturday = $_POST['saturday'];
    }
	}
  if(isset($_POST['sunday'])){
    if($_POST['sunday']!=""){
		    $sunday = $_POST['sunday'];
    }
	}
	$alarm = array(array('year' => $year,
							'month' => $month,
							'day' => $day,
							'hour' => $h,
							'minute' => $m,
							'duration' => $dur,
							'cutoff' => $cut,
							'monday' => $monday,
							'tuesday' => $tuesday,
							'wednesday' => $wednesday,
							'thursday' => $thursday,
							'friday' => $friday,
							'saturday' => $saturday,
							'sunday' => $sunday));
	if(is_array($alarms_array)){
		$merged = array_merge($alarms_array, $alarm);
	}else{
		$merged = $alarm;
	}

	$serializedData = serialize($merged);
	 file_put_contents('Scripts/alarms.save', $serializedData);
   header("Refresh: 0");
  }
}catch(Exception $e){
  $time="";
  $date="";
}

###############################################################################
#########Catch the alarm the user wants to delete and updates the .save########
try{
  if(isset($_POST['abort'])){
    $abort=$_POST['abort'];
    array_splice($alarms_array,$abort,1);
    $serializedData = serialize($alarms_array);
    file_put_contents("Scripts/alarms.save", $serializedData);
  }
}catch(Exception $e){
  $abort="";
}
###############################################################################


$datetoday=date("Y-m-d");
#$timenow=date("H:i:s");
$timenow2=date("H:i");
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>RaspALight</title>
    <link rel="icon" href="Style/raspalight.png">
    <link rel="stylesheet" type="text/css" href="Style/style.css">
    <div class="popup" id="init" onclick="openSettings()">Settings!</div>
      <span class="popuptext" id="settings"><iframe id="pop-out" src="init.php"></iframe><div id="" onclick="myFunction()"></div></span>
  </head>
  <body>
    <container>
      <form  action="index.php" method="post">
        <h1><a href="index.php">Alarm</a></h1><br>
	<div class="floater">
          <input class="halffloat" type='date' name='date' min='<?php echo("$datetoday"); ?>' value='<?php echo("$datetoday");?>'>
          <div id="timepicker" class="text">Date</div><br>
          <input class="halffloat" type='time' name='time' step='60' value='<?php echo("$timenow2");?>'>
          <div id="timepicker" class="text">Time</div><br>
          <input class="fullfloat" type='range' min='0' max='120' step='2' name='duration' value="<?php echo($init_array['duration'])?>" oninput="durationoutput.value = duration.value">
          <br><div class="text"><output name="durationoutput" id="durationoutput"><?php echo($init_array['duration'])?></output>min
          <div id="timepicker">Duration</div></div><br>
		  <button type="button" class="popup" id="btn" onclick="openRepeat()">Repeat</button>
		  <span class="popuptext2" id="repeat">
		  <div style="margin-left:50px;text-align:left">
			<input type="checkbox" name="monday" id="monday" class="css-checkbox" value="1"/>
			<label for="monday" class="css-label">Monday</label>
			<br>
			<input type="checkbox" name="tuesday" id="tuesday" class="css-checkbox" value="1"/>
			<label for="tuesday" class="css-label">Tuesday</label>
			<br>
			<input type="checkbox" name="wednesday" id="wednesday" class="css-checkbox" value="1"/>
			<label for="wednesday" class="css-label">Wednesday</label>
			<br>
			<input type="checkbox" name="thursday" id="thursday" class="css-checkbox" value="1"/>
			<label for="thursday" class="css-label">Thursday</label>
			<br>
			<input type="checkbox" name="friday" id="friday" class="css-checkbox" value="1"/>
			<label for="friday" class="css-label">Friday</label>
			<br>
			<input type="checkbox" name="saturday" id="saturday" class="css-checkbox" value="1"/>
			<label for="saturday" class="css-label">Saturday</label>
			<br>
			<input type="checkbox" name="sunday" id="sunday" class="css-checkbox" value="1"/>
			<label for="sunday" class="css-label">Sunday</label>
			<br>
		</div>
		</span>
    </div>
      <input type='submit' id='alarmBtn' value='Set Alarm' style="margin-top:40px;">
    </form></div>
      <?php
	  if(is_array($alarms_array) && sizeof($alarms_array)>0){
      	  echo("<form action='index.php' method='post'>");
          echo("<select name='abort'>");
		  $i = 0;
             while($alarms_array[$i] != ""){
				                $y=$alarms_array[$i]['year'];
				                $m=$alarms_array[$i]['month'];
              				  $d=$alarms_array[$i]['day'];
              				  $h=$alarms_array[$i]['hour'];
              				  $mi=$alarms_array[$i]['minute'];
              				  $du=$alarms_array[$i]['duration'];
                  echo("<option style='padding-left:4$ipx;' value='$i'>$y.$m.$d - $h:$mi - $du min</option>");
				  $i = $i+1;
            }
        echo("</select><br><input type='submit' value='Abort alarm'></form>");

        }
    ?><br><br>
    <h1>Colorgroup</h1>
    <br>
    <div style="width:100%; text-align:center;">
      <table id="colors" style="margin-left:auto;margin-right:auto;"><tr>
        <td>
          <form id="color" method="post" action="index.php?color=%23FF5500">
            <input type='submit' value='' style='background-color:#FA0;'>
          </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23FF0000">
             <input type='submit' value='' style='background-color:#F00;'>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%2300FF00">
             <input type='submit' value='' style='background-color:#0F0;'>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%230000FF">
             <input type='submit' value='' style='background-color:#00F;'>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23FFFFFF">
             <input type='submit' value='' style='background-color:white;'>
           </form>
         </td>
       </tr>
       <tr>
         <td>
           <form id="color" method="post" action="index.php?color=%23FF2200">
             <input type='submit' value='' style='background-color:#F70;'>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23AA0000">
             <input type='submit' value='' style='background-color:#C00;'>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%2300AA00">
             <input type='submit' value='' style='background-color:#0C0;'>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%230000AA">
             <input type='submit' value='' style='background-color:#00C;'>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23AAAAAA">
             <input type='submit' value='' style='background-color:#CCC;'>
           </form>
         </td>
       </tr>
       <tr>
         <td>
           <form id="color" method="post" action="index.php?color=%23AA1100">
             <input type='submit' value='' style='background-color:#A40;'>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23550000">
             <input type='submit' value='' style='background-color:#A00;'>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23005500">
             <input type='submit' value='' style='background-color:#0A0;'></a>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23000055">
             <input type='submit' value='' style='background-color:#00A;'></a>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23555555">
             <input type='submit' value='' style='background-color:#AAA;'></a>
           </form>
         </td>
       </tr>
       <tr>
         <td>
           <form id="color" method="post" action="index.php?color=%23770D00">
             <input type='submit' value='' style='background-color:#720;'></a>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23110000">
             <input type='submit' value='' style='background-color:#500;'></a>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23001100">
             <input type='submit' value='' style='background-color:#050;'></a>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23000011">
             <input type='submit' value='' style='background-color:#005;'></a>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23111111">
             <input type='submit' value='' style='background-color:#555;'></a>
           </form>
         </td>
       </tr>
       <tr>
         <td>
           <form id="color" method="post" action="index.php?color=%23100200">
             <input type='submit' value='' style='background-color:#400F00;'></a>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23020000">
             <input type='submit' value='' style='background-color:#200;'></a>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23000200">
             <input type='submit' value='' style='background-color:#020;'></a>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23000002">
             <input type='submit' value='' style='background-color:#002;'></a>
           </form>
         </td>
         <td>
           <form id="color" method="post" action="index.php?color=%23000">
             <input type='submit' value='' style='background-color:#000;'></a>
           </form>
         </td>
       </tr>
     </table>
    </div>
    </container>
    <script>
      function openSettings() {
          var popup = document.getElementById("settings");
          popup.classList.toggle("show");
      }
	  function openRepeat() {
          var popup = document.getElementById("repeat");
          popup.classList.toggle("show2");
      }
    </script>
  </body>
</html>
