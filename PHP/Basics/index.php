
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





