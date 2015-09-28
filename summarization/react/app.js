var express = require('express');
var cookieParser = require('cookie-parser');

var app = express();
app.use(cookieParser())

app.get('/', function(req, res) {
  if (req.cookies.demoUserLoggedIn) {
    res.redirect('/patients');
  } else {
    res.sendFile('index.html', { root: __dirname });
  }
});

app.get('/patients', function(req, res) {
  if (req.cookies.demoUserLoggedIn) {
    res.sendFile('index.html', { root: __dirname });
  } else {
    res.redirect('/');
  }
});

app.post('/login', function(req, res) {
  res.cookie('demoUserLoggedIn', true);
  res.send('OK');
});

app.post('/logout', function(req, res) {
  res.clearCookie('demoUserLoggedIn');
  res.send('OK');
});

app.get('/js/bundle.js', function(req, res) {
  res.sendFile('bundle.js', { root: __dirname + '/js/' });
});

app.get('/js/3rdparty/:name', function(req, res) {
  var options = {
    root: __dirname + '/js/3rdparty/',
    dotfiles: 'deny'
  };
  res.sendFile(req.params.name, options);
});

app.get('/css/:name', function(req, res) {
  var options = {
    root: __dirname + '/css/',
    dotfiles: 'deny'
  };
  res.sendFile(req.params.name, options);
});

app.get('/images/:name', function(req, res) {
  var options = {
    root: __dirname + '/images/',
    dotfiles: 'deny'
  };
  res.sendFile(req.params.name, options);
});

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});