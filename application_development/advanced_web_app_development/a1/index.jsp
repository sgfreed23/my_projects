<!DOCTYPE html>
<html lang="en">
<head>
<!--
"Time-stamp: <Sat, 01-02-21, 18:35:01 Eastern Standard Time>"
//-->
<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="My online portfolio that illustrates skills acquired while working through various project requirements.">
	<meta name="author" content="Samuel Freed">
	<link rel="icon" href="favicon.ico">

	<title>LIS4368 - Assignment1 - Samuel Freed</title>

	<%@ include file="/css/include_css.jsp" %>		
	
</head>
<body>

<!-- display application path -->
<% //= request.getContextPath()%>
	
<!-- can also find path like this...<a href="${pageContext.request.contextPath}${'/a5/index.jsp'}">A5</a> -->

	<%@ include file="/global/nav.jsp" %>	

	<div class="container">
		<div class="starter-template">
					<div class="page-header">
						<%@ include file="global/header.jsp" %>
					</div>

					<h4>JDK Installation:</h4>
					<img src="img/jdk_install.png" class="img-responsive center-block" alt="JDK Installation" />

					<br /> <br />
					<b>Tomcat Installation:</b><br />
					<img src="img/tomcat_install.png" class="img-responsive center-block" alt="Tomcat Installation" />

	<%@ include file="/global/footer.jsp" %>

	</div> <!-- end starter-template -->
 </div> <!-- end container -->

 	<%@ include file="/js/include_js.jsp" %>		

</body>
</html>
