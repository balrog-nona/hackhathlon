<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  
  <link rel="stylesheet" href="/static/style.css" />
  <title>HlidejFilmy</title>
</head>
<body>
<div class="banner"></div>

<p style="text-align: center">
  <big><big><big>Vítejte na našem webu.</big></big></big>
</p>
<p style="text-align: center">
  <big><big><big>Tady se můžete podívat, kdy dávají Váš oblíbený film. </big></big></big>
</p>

<form method='POST' id='najdi' action='/hledani' style="text-align: center">
<table>
<p style="text-align: center">
  Stačí sem pouze napsat film, který hledáš (s diakritikou a malými písmenky:)
</p>

<textarea name="seznam_filmu"></textarea>
<input value='hledej' type='submit' />
</form>

</body>
</html>