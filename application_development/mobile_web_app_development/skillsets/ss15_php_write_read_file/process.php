<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

?>
<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="utf-8">
			<meta http-equiv="X-UA-Compatible" content="IE=edge">
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<meta name="description" content="Skill Set 15: Write/Read File.">
			<meta name="author" content="Samuel Freed">
			<link rel="icon" href="favicon.ico">

				<title>LIS 4381 - Write-Read File</title>
				<?php include_once("../css/include_css.php"); ?>
		
				<style type="text/css">
				h1
				{
					margin: 0;     
					color: #488DFF;
					padding-top: 48px;
					font-size: 48px;
					font-family: "trebuchet ms", sans-serif; 
					text-shadow: 2px 2px #bdbdbd
				}
				</style>
		 
		</head>
		
		<body>
		
			<?php include_once("../global/nav.php"); ?>
			
			<div class="container">
				<div class="starter-template">
					<div class="page-header">
						<?php include_once("global/header.php"); ?>
					</div>
					<p class="text-justify">
					<?php
					
					$myfile = fopen("file.txt","w+") or exit("Unable to open file!");
					$txt = $_POST['comment'];
					fwrite($myfile, $txt); 
					fclose($myfile); 
					
					$myfile = fopen("file.txt", "r+") or exit("Unable to open file!");
					while(!feof($myfile)){
						echo fgets($myfile)."<br />";
					}
					
					fclose($myfile);
					?>
					</p>
					<?php include_once "global/footer.php"; ?>
				</div> 
			</div>	
			
			<?php include_once("../js/include_js.php"); ?>
			
			<script>
			$(document).ready(function(){
				$('#myTable').DataTable({
					responsive: true
				});
			});
			</script>
		</body>
	</html>