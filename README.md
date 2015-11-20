# Heuristieken
<b>Contents:</b><br>
[To-Do](https://github.com/JoeySchouten/Heuristieken/tree/class-development#to-do)<br>
[Klassen en Functies] (https://github.com/JoeySchouten/Heuristieken/tree/class-development#klassen-en-functies) <br>

<h3>To-Do</h3>
<ul> placeAll efficienter maken, op de x-as plaatst ie sowieso goed; maar na de 1e rij huizen loopt ie alle punten die bezet zijn door die huizen door. Moet beter.</ul>
<ul> Alle Klassen en Functies toevoegen aan documentatie (zodat we het zelf ook nog blijven snappen)</ul>
<ul> Functie die de min. vrijstand rondom een huis bepaalt; in een spiraal ipv. linear.</ul>
<ul> Waterberekenfunctie de oppervlakte willekeurig laten opdelen over de lichamen.</ul>
<ul> Wanneer de "domme oplossing" af is, mergen met master. </ul>
<ul> Kijken of een 2-dimensionale array sneller is wanner placeAll functie compleet werkt.</ul>


<h3>Klassen en Functies</h3>
<i><b>Point</b></i><br>
Deze klasse is voor het defineren van een bepaald punt als een object, waarna deze ook snel aangepast kan worden.
Zo zijn ook de hoekpunten van de huizen gedefineerd als Points, om deze makkelijk, maar vooral consistent, door te geven.

<i>Variabelen:</i><br>
<i>self.x</i> - X-Coordinaat van het punt.<br>
<i>self.y</i> - Y-Coordinaat van het punt.<br>

<i>Functies:</i><br>
<i>setPoint(int x, int y)</i> - Zet de coordinaten van het punt op x,y.<br>

<i>Child-klassen:</i><br>
Er zijn geen klassen die Point als parent hebben.


<i><b>Map</b></i><br>
Deze klasse bevat alle informatie voor het initializeren van de dictionary waarmee gecontroleerd wordt wat waar staat.
Ook bevat deze klasse alle functies die de waarden e.d. in deze dict aanpassen.

<i>Variabelen:</i><br>
<i>self.data</i> - Dictionary welke met de initializeMap functie keys gegeven wordt.<br>
<i>self.length</i> - Maximale lengte (Y-waarde) van het kavel voor Amstelhaege in eenheden<br>
<i>self.width</i> - Maximale breedte (X-waarde) van het kavel voor Amstelhaege in eenheden<br>

<i>Functies:</i><br>
<i>initializeMap()</i> - Vult de dictionary in met keys voor elk punt op de kaart.<br>
<i>fill(int keyx, int keyy, int vrij, int width, int height)</i> - Geeft waarden aan entries in de dictionary. <br>
  Uitleg input:<br>
      int keyx - Begin x waarde voor de dictionary key ([keyx,y]).<br>
      int keyy - Begin x waarde voor de dictionary key ([x,keyy]).<br>
      int vrij - Hoeveelheid vereiste vrijstand van het huis dat ingevoerd wordt.<br>
      int width - Breedte van het huis dat ingevoerd wordt.<br>
      int height - Lengte van het huis dat ingevoerd wordt<br>

<i>Child-klassen:</i><br>
Er zijn geen klassen die Map als parent hebben.
