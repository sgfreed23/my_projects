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
			<meta name="description" content="Skill Set 13: Simple Calculator.">
			<meta name="author" content="Samuel Freed">
			<link rel="icon" href="favicon.ico">

				<title>LIS 4381 - Simple Calculator</title>
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
					
					<?php
					if (!empty($_POST))
					{
						$num1 = $_POST['num1'];
						$num2 = $_POST['num2'];
						$operation = $_POST['operation'];
						
						if (is_numeric($num1) && is_numeric($num2))
						{
							echo '<h2>'."$operation".'</h2>';
							
							function AddNum($x, $y)
							{
								echo "$x"." + "."$y"." = ";
								echo $x + $y;
							}
							
							function SubtractNum($x, $y)
							{
								echo "$x"." - "."$y"." = ";
								echo $x - $y;
							}
							
							function MultiplyNum($x, $y)
							{
								echo "$x"." * "."$y"." = ";
								echo $x * $y;
							}
							
							function DivideNum($x, $y)
							{
								if($y == 0)
								{
									echo "cannot divide by zero!";
								}
								else
								{
									echo "$x"." / "."$y"." = ";
									echo $x / $y;
								}
							}
							
							function PowerNum($x, $y)
							{
								echo "$x"." raised to the power of "."$y"." = ";
								echo pow($x, $y);
							}
							
							
							if($operation == 'addition')
							{
								AddNum($num1, $num2);
							}
							
							else if($operation == 'subtraction')
							{
								SubtractNum($num1, $num2);
							}
							
							else if($operation == 'multiplication')
							{
								MultiplyNum($num1, $num2);
							}
							
							else if($operation == 'division')
							{
								DivideNum($num1, $num2);
							}
							
							else if($operation == 'exponentiation')
							{
								PowerNum($num1, $num2);
							}
							else
							{
								echo "Must select an operation.";
							}
						?>
						<p>
						<?php
						} //end preg_match if
						
						else
						{
							echo "Must enter a valid number.";
						} 
					} 
					
				else
				{
					header('Location: index.php');
				}
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