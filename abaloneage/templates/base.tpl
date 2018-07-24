<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Age Guess of abalone!</title>
  <!--
  <link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v2.3.7/dist/mini-default.min.css">
  -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/mini.css/3.0.0/mini-default.min.css" />
  % setdefault('use_bokeh', False)
  % if use_bokeh:
    <link href="http://cdn.pydata.org/bokeh/release/bokeh-0.13.0.min.css" rel="stylesheet" type="text/css">
    <script src="http://cdn.pydata.org/bokeh/release/bokeh-0.13.0.min.js"></script>
    {{ !script }}
  % end
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <header>
    <a href="/" class="button">Application to guess the age of abalone.</a>
  </header>
  <!-- Other template file will be inserted here. -->
  {{ !base }}
</body>
</html>
