<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Skill Set 15: Read/Write File.">
	<meta name="author" content="Samuel Freed">
	<link rel="icon" href="favicon.ico">

	<title>LIS 4381 - Write/Read File</title>
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

				<h2>File Data</h2>
				<form class="form-horizontal" role="form" method="post" action="process.php">
					<div class="form-group">
						<label class="control-label col-sm-2" for="comment">Comment:</label>
						<div class="col-sm-10">
							<textarea class="form-control" rows="5" name="comment" id="comment" placeholder="Please enter text here..."></textarea>
						</div>
					</div>
					
					<div class="form-group">
						<div class="col-sm-12">
							<button type="submit" class="btn btn-default">Submit</button>
						</div>
					</div>
				</form>
				
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