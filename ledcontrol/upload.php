<?php
#move_uploaded_file($_FILES['datei']['tmp_name'], 'upload/'.$_FILES['datei']['name']);
$temp = explode(".", $_FILES["datei"]["name"]);
$newfilename = "background.jpg";
move_uploaded_file($_FILES["datei"]["tmp_name"], "Style/" . $newfilename);
?>
<style>
body{
text-align:center;
background:url('background.jpg');
}
a{
padding:5px;
border:1 px solid black;
border-radius:10px;
color:black;
}
a:hover{
color:white;
background-color:rgba(0,0,0,0.5);
}
</style>
<body>
<br><br><h1>Upload erfolgreich!</h1><br><br>
<a href="index.php">Kehre zur Seite zur&uuml;ck</a>
</body>
