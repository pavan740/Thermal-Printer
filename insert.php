<?php
	try{ 	
		$tbox=$_POST['tbox'];
		$database_name = "test.db";
		$db = new SQLite3($database_name);
		$query = "INSERT INTO PRINTER VALUES ('$tbox');";
		$db->exec($query);
		shell_exec("sudo python /var/www/html/printer_db.py");
		$query2 = "DELETE FROM PRINTER";
		$db->exec($query2);
		header('Location: test.html');
	}catch(PDOException $e) {
    		echo $e->getMessage();
	}
?>
