
<?php
$greeting = 'Hey';
echo "Hello" . " Everyone <br> ";
echo " $greeting Programmer <br> "; 
echo (int) 3.22, "<br>";
?>

<!-- array  -->
<?php
$friends = array("ram", "shyam", "krishna");
echo var_dump($friends); // to see what inside friends
echo "<br>";
echo $friends[0];
echo "<br>";
echo $friends[1];
?>

<?php 
foreach ($friends as $value) {
    echo "$value <br>";
}

?> 

<!-- Function -->
<?php
function processMarks($marksArr){
    $sum = 0;
    foreach ($marksArr as $value) {
        $sum = $sum + $value;
    }
    return $sum;   
}
$ram = [34,98,45,12,98,93];
$sumMarks = processMarks($ram);

echo "Total marks of ram is $sumMarks <br>";
?>

<!-- date -->
<?php
$date = date("d l D");
echo "todays date is $date <br>"
?>

<?php
//Associative Array
$color = array("ram" => "red", "shyam" => "purple",
 "krishna" => "blue", 69 => "yellow");

echo $color["ram"] ;
foreach ($color as $key => $value) {
    echo "<br> Favorite color of $key is $value "; 
}
?>

<?php
// Connecting to the Database
$servername = "localhost";
$username = "root";
$password ="";
$database = "Prashana";

//Create connection
$conn = mysqli_connect($servername, $username, $password, $database);

//Die if connection not successful
if (!$conn){
    die("Sorry failed to connect: " . mysqli_connect_error());
}

else{
    echo"<br>Successfully connected <br>";
}

//Create a database
/*$sql = "CREATE DATABASE Prashana";
$result = mysqli_query($conn, $sql);

//Check for the db creation
if($result){
    echo "The DB was created <br>";
}
else{    
    echo "The DB wasn't created" . mysqli_connect_error();
}
echo "The result is ";
echo var_dump($result);
?>
*/

//Create table 
$sql = "CREATE TABLE `trip` ( `sno` INT(6) NOT NULL AUTO_INCREMENT ,  `name` VARCHAR(12) NOT NULL ,  `dest` VARCHAR(6) NOT NULL ,  PRIMARY KEY  (`sno`))";
$result = mysqli_query($conn, $sql);

//Check for the table creation
if($result){
    echo "The table was created <br>";
}
else{    
    echo "The table wasn't created" . mysqli_connect_error();
}