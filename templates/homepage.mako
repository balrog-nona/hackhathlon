<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Hello</title>
</head>
<body>
<p>
  Vítejte na našem webu.
  Tady se můžete podívat, kdy dávají Váš oblíbený film.
</p>

<form method='POST' id='najdi' action='/hledani.mako'>
<table>
<p>
  Stačí napsat sem film, který hledáš, s diakritikou a malými písmenky :)
</p>
<textarea name="seznam_filmu">Sem napis seznam filmu</textarea>
<input value='HLEDEJ' type='submit' />
</form>

<p>
  Hello world from Czechitas Hackaton to ${name}!
</p>
</body>
</html>