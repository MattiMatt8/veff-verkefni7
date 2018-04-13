<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Verkefni 7</title>
	<link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body>
<div class="container">
	%for vara in vorur:
		<h2>
			{{vara["Vörunafn"]}}
			%verd = "{:,}".format(vara["Verð"]).replace(",",".")
			{{verd}} kr.
		</h2>
		<a href="/lidur2/add/{{vara['Vörunafn']}}">Bæta við vörunni</a>
	%end
	<a href="/lidur2/karfa">Karfa</a>
	<a href="/">Til baka</a>
</div>
</body>
</html>