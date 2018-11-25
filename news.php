<?php
shell_exec("sudo python /var/www/html/top_news.py");
header('Location: test.html');
?>
