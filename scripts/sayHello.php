<?php

echo "Hello there. Type yo name in here:\n";
$name = trim(fgets(STDIN));

echo "\nThanks, " . $name . ", it's really nice to meet you.\n\n";

?>