const express = require('express');
const app = express();
const redis = require('redis');
const responseTime = require('response-time');

const promClient = require('prom-client');

const restResponseTimeHistogram = new promClient.Histogram({
  name: 'rest_response_time_duration_seconds',
  help: 'REST API endpoint response time in seconds',
  labelNames: ['method', 'route', 'status_code'],
});

app.use(responseTime( (req, res, time) => {
  if (req?.route?.path) {
    restResponseTimeHistogram.observe({
      method: req.method,
      route: req.route.path,
      status_code: res.statusCode,
    }, time / 1000);
  }
},
));

const client = redis.createClient(6379, process.env.npm_config_srvname);
client.on('error', function(err) {
  console.error('Redis error', err);
});

const collectDefaultMetrics = promClient.collectDefaultMetrics;
collectDefaultMetrics();

app.get('/metrics', async (req, res) => {
  res.send(await promClient.register.metrics());
});

app.get('/', function(req, res) {
  res.redirect('/index.html');
});

app.get('/metrics', function(req, res) {

});

app.get('/json', function(req, res) {
  client.hlen('wallet', function(err, coins) {
    client.get('hashes', function(err, hashes) {
      const now = Date.now() / 1000;
      res.json( {
        coins: coins,
        hashes: hashes,
        now: now,
      });
    });
  });
});

app.use(express.static('files'));
// Using least privileged user node in docker image
// to run the app can only be done running throught a port below 1024
app.listen(1024, function() {
  console.log('WEBUI running on port 1024');
});
