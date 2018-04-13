<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Verkefni 7</title>
	<link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body>
<div class="container">
	%heildarVerd = 0
	%for vara in karfa:
	e<div class="utanum">
		<h2>
			{{vara["Magn"]}} x {{vara["Vörunafn"]}} =
			%voruVerd = vorur[vara["Reytur"]]["Verð"] * vara["Magn"]
			%heildarVerd += voruVerd
			%voruVerd = "{:,}".format(voruVerd).replace(",",".")
			{{voruVerd}} kr.
		</h2>
		<a href="/lidur2/eyda/{{vara['Vörunafn']}}">Eyða</a>
	</div>
	%end
	%heildarVerd = "{:,}".format(heildarVerd).replace(",",".")
	<h2>Heildarverð = {{heildarVerd}} kr.</h2>
	<a href="/lidur2">Halda áfram að versla</a>
	<a href="/lidur2/eyda">Eyða öllum vörum úr körfu</a>
</div>
</body>
</html>
