<?php 
$filename=$_POST['file'];
$myfile = fopen($filename, "w");
$data=$_POST['data'];


fwrite($myfile, $data);





 ?>
