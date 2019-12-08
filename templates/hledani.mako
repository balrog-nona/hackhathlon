<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="/static/style.css" />
  <title>Výsledky hledání</title>
</head>
<body>

<p>
To, co jsi hledal/a, najdeš v TV následovně:
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

<form method='POST' id='posli' action='/posli'>
<table>
<p>
  Jestli chceš, můžeme Ti poslat výsledky našeho hledání na e-mail. Zadej ho případně sem.
</p>
<input type="text" name="email">
<input value='OK' type='submit' />
</form>

</body>
</html>