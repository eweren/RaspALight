<?php
###############################################################################
// Try catch blocks for the color, the time of an alarm and the abortion

$recoveredData = file_get_contents('/var/www/html/ledcontrol/Scripts/init.save');
$init_array = unserialize($recoveredData);
try{
  if(isset($_GET['color'])){
    $color=$_GET['color'];
    $color = str_replace("#", "", $color);
    $r = hexdec(substr($color,0,2));
    $g = hexdec(substr($color,2,2));
    $b = hexdec(substr($color,4,2));
    $execute = shell_exec("python /var/www/html/ledcontrol/Scripts/setColor.py $r $g $b");
  }
} catch(Exception $e){
  $color="";
}

try{
  if(isset($_GET['time']) && isset($_GET['date']) && isset($_GET['duration'])){
    $h = substr($_GET['time'],0,2);
    $m = substr($_GET['time'],3,2);
    $date = $_GET['date'];
    $dur = $_GET['duration'];
    $day=substr($date,8,2);
    $month=substr($date,5,2);
    $year=substr($date,0,4);
    $cut = $init_array['cut_off_time'];
    $execute = exec("python /var/www/html/ledcontrol/Scripts/alarm.py $year $month $day $h $m $dur $cut > /dev/null 2>/dev/null &");
  }
}catch(Exception $e){
  $time="";
  $date="";
}

try{
  if(isset($_GET['abort'])){
    $abort=$_GET['abort'];
    $execute=shell_exec("python Scripts/killpython.py $abort");
  }
}catch(Exception $e){
  $abort="";
}
###############################################################################


$datetoday=date("Y-m-d");
$timenow=date("H:i:s");
$execute = shell_exec("sudo pigpiod");
$timenow2=date("H:i");
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>RaspALight</title>
    <link rel="icon" href="Style/raspalight.png">
    <link rel="stylesheet" type="text/css" href="Style/style.css">
    <div class="popup" id="init" onclick="myFunction()">Settings!</div>
      <span class="popuptext" id="settings"><iframe id="pop-out" src="init.php"></iframe><div id="" onclick="myFunction()"></div></span>
  </head>
  <body>
    <container>
      <form  action="index.php" method="get">
        <h1><a href="index.php">Alarm</a></h1><br>
	<div class="floater">
          <input class="halffloat" type='date' name='date' min='<?php echo("$datetoday"); ?>' value='<?php echo("$datetoday");?>'>
          <div id="timepicker" class="text">Date</div><br>
          <input class="halffloat" type='time' name='time' step='60' value='<?php echo("$timenow2");?>'>
          <div id="timepicker" class="text">Time</div><br>
          <input class="fullfloat" type='range' min='0' max='120' step='2' name='duration' value="<?php echo($init_array['duration'])?>" oninput="durationoutput.value = duration.value">
          <br><div class="text"><output name="durationoutput" id="durationoutput"><?php echo($init_array['duration'])?></output>min
          <div id="timepicker">Duration</div></div><br>
    </div>
      <input type='submit' id='alarmBtn' value='Set Alarm' style="margin-top:40px;">
    </form></div>
      <?php
	exec("pgrep -af ledcontrol/Scripts/alarm.py", $out);
	if(sizeof($out) > 1){
      	  echo("<form action='index.php' method='get'>");
          echo("<select name='abort'>");
          $i=0;
             while($out[$i] != ""){
                $arrayAlarms = explode(" ", $out[$i]);
                if($i < sizeof($out)-1){
                  echo("<option style='padding-left:40px;' value='$arrayAlarms[0]'>$arrayAlarms[5].$arrayAlarms[4] - $arrayAlarms[6]:$arrayAlarms[7] - $arrayAlarms[8] min");
                }
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
      // When the user clicks on div, open the popup
      function myFunction() {
          var popup = document.getElementById("settings");
          popup.classList.toggle("show");

      }
    </script>
  </body>
</html>
