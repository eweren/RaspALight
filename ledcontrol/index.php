<?php
try{
  $color=$_GET['color'];
} catch(Exception $e){
  $color="";
}
try{
  $time=$_GET['time'];
  $date=$_GET['date'];
  $duration=$_GET['duration'];
}catch(Exception $e){
  $time="";
  $date="";
}
try{
  $abort=$_GET['abort'];
}catch(Exception $e){
  $abort="";
}/*
try{
  $fading=$_GET['fading'];
}catch(Exception $e){
  $fading=False;
}
try{
  $fadingabort=$_GET['fadingabort'];
}catch(Exception $e){
  $fadingabort="";
}*/
$datetoday=date("Y-m-d");
$timenow=date("H:i:s");
$execute = shell_exec("sudo pigpiod");
$timenow2=date("H:i");

if($color != ""){
   $color = str_replace("#", "", $color);
   $r = hexdec(substr($color,0,2));
   $g = hexdec(substr($color,2,2));
   $b = hexdec(substr($color,4,2));
   $execute = shell_exec("python /var/www/html/ledcontrol/Scripts/setColor.py $r $g $b");
}
if($abort != ""){
   $execute=shell_exec("python Scripts/killpython.py $abort");
}
if($time != "" & $date != ""){
   $h = substr($time,0,2);
   $m = substr($time,3,2);
   $dur = 30;
   if($duration != ""){
     $dur = $duration;
   }
   $day=substr($date,8,2);
   $month=substr($date,5,2);
   $year=substr($date,0,4);
   $execute = exec("python /var/www/html/ledcontrol/Scripts/alarm.py $year $month $day $h $m $dur > /dev/null 2>/dev/null &");
}
/*
if($fading == True){
   $execute = exec("python /var/www/html/ledcontrol/Scripts/fading.py");
}
*/
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Tinco Lightroom</title>
    <link rel="icon" href="Style/tincoicon.png">
    <link rel="stylesheet" type="text/css" href="Style/style.css">
  </head>
  <body>
    <container>
      <form  action="index.php" method="get">
        <h1><a href="index.php">Alarm</a></h1>
	<table style="margin-left:auto; margin-right:auto;"><tr>
          <td><input type='date' name='date' min='<?php echo("$datetoday"); ?>' value='<?php echo("$datetoday");?>'></td>
          <td><input type='time' name='time' step='60' value='<?php echo("$timenow2");?>'></td></tr><tr>
	  <td id="timepicker" style="opacity:0.5;">Datum</td>
          <td id="timepicker" style="opacity:0.5;">Uhrzeit</td></tr>
	  <tr><td colspan="2"><input type='range' min='0' max='60' name='duration'></td></tr>
	  <tr><td colspan="2" id="timepicker" style="opacity:0.5;">Dauer</td></tr>
	</table>
        <input type='submit' id='alarmBtn' value='Alarm stellen' style="margin-top:40px;">
      </form>
      <?php
	exec("pgrep -af ledcontrol/Scripts/alarm.py", $out);
	if(sizeof($out) > 1){
      	  echo("<form action='index.php' method='get'>");
          echo("<select name='abort'>");
          $i=0;
             while($out[$i] != ""){
                $arrayAlarms = explode(" ", $out[$i]);
                if($i < sizeof($out)-1){
                  echo("<option style='padding-left:40px;' value='$arrayAlarms[0]'>$arrayAlarms[5].$arrayAlarms[4] - $arrayAlarms[6]:$arrayAlarms[7] - $arrayAlarms[8]");
                }
                $i = $i+1;
             }
          echo("</select><br><input type='submit' value='Alarm abbrechen'></form>");
        }
      ?><br><br>
      <h1>Farbauswahl</h1>
      <br>
     <div style="width:100%; text-align:center;">
       <table id="colors" style="margin-left:auto;margin-right:auto;"><tr>
        <td><form id="color" method="post" action="index.php?color=%23FF5500">
          <input type='submit' value='' style='background-color:#FA0;'></a>
	</form></td><td>
	<form id="color" method="post" action="index.php?color=%23FF0000">
          <input type='submit' value='' style='background-color:#F00;'></a>
        </form></td><td>
	<form id="color" method="post" action="index.php?color=%2300FF00">
          <input type='submit' value='' style='background-color:#0F0;'></a>
        </form></td><td>
	<form id="color" method="post" action="index.php?color=%230000FF">
          <input type='submit' value='' style='background-color:#00F;'></a>
        </form></td><td>
	<form id="color" method="post" action="index.php?color=%23FFFFFF">
          <input type='submit' value='' style='background-color:white;'></a>
        </form></td></tr><tr>
        <td><form id="color" method="post" action="index.php?color=%23FF2200">
          <input type='submit' value='' style='background-color:#F70;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23AA0000">
          <input type='submit' value='' style='background-color:#C00;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%2300AA00">
          <input type='submit' value='' style='background-color:#0C0;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%230000AA">
          <input type='submit' value='' style='background-color:#00C;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23AAAAAA">
          <input type='submit' value='' style='background-color:#CCC;'></a>
        </form></td></tr><tr>
        <td><form id="color" method="post" action="index.php?color=%23AA1100">
          <input type='submit' value='' style='background-color:#A40;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23550000">
          <input type='submit' value='' style='background-color:#A00;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23005500">
          <input type='submit' value='' style='background-color:#0A0;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23000055">
          <input type='submit' value='' style='background-color:#00A;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23555555">
          <input type='submit' value='' style='background-color:#AAA;'></a>
        </form></td></tr><tr>
        <td><form id="color" method="post" action="index.php?color=%23770D00">
          <input type='submit' value='' style='background-color:#720;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23110000">
          <input type='submit' value='' style='background-color:#500;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23001100">
          <input type='submit' value='' style='background-color:#050;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23000011">
          <input type='submit' value='' style='background-color:#005;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23111111">
          <input type='submit' value='' style='background-color:#555;'></a>
        </form></td></tr><tr>
        <td><form id="color" method="post" action="index.php?color=%23100200">
          <input type='submit' value='' style='background-color:#400F00;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23020000">
          <input type='submit' value='' style='background-color:#200;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23000200">
          <input type='submit' value='' style='background-color:#020;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23000002">
          <input type='submit' value='' style='background-color:#002;'></a>
        </form></td><td>
        <form id="color" method="post" action="index.php?color=%23000">
          <input type='submit' value='' style='background-color:#000;'></a>
        </form></td>
	</tr>
      </table></div><br>
<?php /*	      <?php
        exec("pgrep -af ledcontrol/Scripts/fading.py", $out1);
        if($out1[1] != ""){
	  $arrayFadings = explode(" ", $out[$i]);
          if($arrayFadings[1] = "python" & $arrayFadings[3]="/var/www/html/ledcontrol/Scripts/fading.py"){
	    echo("<form action='index.php' method='get' action='index.php?fading=true'>
              <input type='hidden' name='fading' value='fading'>
              <input id='smallbtn' type='submit' value='fading'>
              </form><br><form action='index.php' method='get'>
              <input type='hidden' name='fadingabort' value='$arrayFadings[0]'>
              <input type='submit' id='smallbtn' value='fadingabort'>
              </form>");
           }
        }else{
	  echo("<form action='index.php' method='get' action='index.php>
              <input type='hidden' name='fading' value='fading'>
              <input type='submit' value='fading'>
              </form>");
	}
      ?>*/?>
	  <br>
       <form action="upload.php" method="post" enctype="multipart/form-data">
        <div class="myLabel">
 	  <input type="file" name="datei">
	  <span>Hintergrundbild ausw&auml;hlen</span><br>
	</div><br>
        <input type="submit" value="Hochladen">
      </form>
    </container>
  </body>
</html>
