<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Výsledky hledání</title>
</head>
<body>

<p>
To, co jsi hledaj, najdeš v TV následovně:
</p>
<table>
<tr>
    <th>Název pořadu</th>
    <th>Datum</th>
    <th>Kanál</th>
    <th>Čas</th>
  </tr>
  %for porad in vysledek:
    <tr>
      <td>${porad['nazev']}</td>
      <td>${porad['datum']}</td>
      <td>${porad['kanal']}<td>
      <td>${porad['cas']}</td>
    </tr>
  %endfor
</table>

</body>
</html>