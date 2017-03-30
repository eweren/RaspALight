<?php
###############################################################################
// Try catch block for the form and for getting the init setting we already set.
try{
  $recoveredData = file_get_contents('init.save');
  $savedArray = unserialize($recoveredData);
  $duration=$savedArray['duration'];
  $cut_off_time=$savedArray['cut_off_time'];
  $r_pin=$savedArray['r_pin'];
  $g_pin=$savedArray['g_pin'];
  $b_pin=$savedArray['b_pin'];
}catch(Exception $e){
  $duration=30;
  $cut_off_time=60;
  $r_pin=24;
  $g_pin=22;
  $b_pin=17;
}
try{
  if(isset($_GET['duration'])){
    $duration = $_GET['duration'];
  }
    if(isset($_GET['cut_off_time'])){
      $cut_off_time = $_GET['cut_off_time'];
    }
    if(isset($_GET['r_pin'])){
      $r_pin=$_GET['r_pin'];
    }
    if(isset($_GET['g_pin'])){
      $g_pin=$_GET['g_pin'];
    }
    if(isset($_GET['b_pin'])){
      $b_pin=$_GET['b_pin'];
    }
  $init_array = array('duration' => $duration,
                    'cut_off_time' => $cut_off_time,
                    'r_pin' => $r_pin,
                    'g_pin' => $g_pin,
                    'b_pin' => $b_pin);
  $serializedData = serialize($init_array);
  file_put_contents('init.save', $serializedData);
}catch(Exception $e){
}
try{
  if(isset($_GET['cut_off_time'])){
    $cut_off_time = $_GET['cut_off_time'];
  }
  if(isset($_GET['r_pin'])){
    $r_pin=$_GET['r_pin'];
  }
  if(isset($_GET['g_pin'])){
    $g_pin=$_GET['g_pin'];
  }
  if(isset($_GET['b_pin'])){
    $b_pin=$_GET['b_pin'];
  }
  $init_string = $r_pin . "," . $g_pin . "," . $b_pin . "," . $cut_off_time;
  file_put_contents('pins.save', $init_string);
}catch(Exception $e){

}
###############################################################################
//functions to handle the writing to the ini
###############################################################################
// serialize your input array (say $array)/**
//$serializedData = serialize($array);

// save serialized data in a text file
//file_put_contents('your_file_name.txt', $serializedData);

// at a later point, you can convert it back to array like:
//$recoveredData = file_get_contents('your_file_name.txt');

// unserializing to get actual array
//$savedArray = unserialize($recoveredData);

// you can print your array like
//print_r($savedArray);
###############################################################################




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
      <form  action="init.php" method="get">
        <h1><a href="init.php">Set-up</a></h1>
        <h2 style="opacity:0.5;">Set your standard setting up.<h2><br><br>
	       <div class="floater">
           <input class="fullfloat" type='range' min='0' max='120' step='2' name='duration' value="<?php echo($init_array['duration'])?>"></div>
           <div id="timepicker" class="text">Duration</div><br>
           <input class="fullfloat" type='range' min='0' max='120' step='2' name='cut_off_time' value="<?php echo($init_array['cut_off_time'])?>"></div>
           <div id="timepicker" class="text">Cut-off-time</div><br>
           <input class="fullfloat" type='number' name='r_pin' value="<?php echo($init_array['r_pin'])?>"></div><br>
           <div id="timepicker" class="text">Red pin</div><br>
           <input class="fullfloat" type='number' name='g_pin' value="<?php echo($init_array['g_pin'])?>"></div><br>
           <div id="timepicker" class="text">Green pin</div><br>
           <input class="fullfloat" type='number' name='b_pin' value="<?php echo($init_array['b_pin'])?>"></div><br>
           <div id="timepicker" class="text">Blue pin</div><br>
	       </div>
         <input type='submit' id='alarmBtn' value='Set standards' style="margin-top:40px;">
      </form>
    <br>
	  <br>
      <form action="upload.php" method="post" enctype="multipart/form-data">
        <div class="myLabel">
 	        <input type="file" name="datei">
	        <span>Select background</span><br>
	      </div>
        <br>
        <input type="submit" value="Upload">
      </form>
    </container>
  </body>
</html>
