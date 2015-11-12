# Heuristieken
<b>Contents:</b>
To-Do
Klassen en Functies

<h3>Klassen en Functies</h3>
<i><b>Point</b></i><br>
Deze klasse is voor het defineren van een bepaald punt als een object, waarna deze ook snel aangepast kan worden.<br>
Zo zijn ook de hoekpunten van de huizen gedefineerd als Points, om deze makkelijk, maar vooral consistent, door te geven.<br>
<i>Variabelen:</i><br>
<i>self.x</i> - X-Coordinaat van het punt.<br>
<i>self.y</i> - Y-Coordinaat van het punt.<br>

<i>Functies:</i><br>
<i>setPoint(int x, int y)</i> - Zet de coordinaten van het punt op x,y.<br>

<i>Child-klassen:</i><br>
Er zijn geen klassen die Point als parent hebben.


<i><b>Map</b></i><br>
Deze klasse bevat alle informatie voor het initializeren van de dictionary waarmee gecontroleerd wordt wat waar staat. <br>
Ook bevat deze klasse alle functies die de waarden e.d. in deze dict aanpassen.<br>
<i>Variabelen:</i><br>
<i>self.data</i> - Dictionary welke met de initializeMap functie keys gegeven wordt.<br>
<i>self.length</i> - Maximale lengte (Y-waarde) van het kavel voor Amstelhaege in eenheden<br>
<i>self.width</i> - Maximale breedte (X-waarde) van het kavel voor Amstelhaege in eenheden<br>

<i>Functies:</i><br>
<i>initializeMap()</i> - Vult de dictionary in met keys voor elk punt op de kaart.<br>
<i>fill(int keyx, int keyy, int vrij, int width, int height)</i> - Geeft waarden aan entries in de dictionary. <br>
  Uitleg input:<br>


<i>Child-klassen:</i><br>
Er zijn geen klassen die Map als parent hebben.
