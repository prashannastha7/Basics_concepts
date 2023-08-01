
<?php
$greeting = 'Hey';
echo "Hello" . " Everyone <br> ";
echo " $greeting Programmer";
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
echo "todays date is $date"
?>


