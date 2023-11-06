const express = require('express')
var cors = require('cors');
var https = require('https')
var fs = require('fs')
const app = express()
const port = 5672

var allowedOrigins = ['https://kazar4.com', 'http://kazar4.com']
app.use(cors({
    origin: function (origin, callback){
        if (!origin) return callback(null, true);

        if(allowedOrigins.indexOf(origin) === -1){
            var msg = 'The COS policty for this site does not ' +
            'allow adcess from the specified Origin.';
            return callback(new Error(msg), false);
        }
        return callback(null, true)
    }

}));

let colorToSend = "RED"

// sets color for LEDs to check
app.get('/', (req, res) => {
  res.send("Hi!")
})

// sets color for LEDs to check
app.get('/lights/:color', (req, res) => {
  res.send(req.params["color"])
  console.log(req.params["color"])
  colorToSend = req.params["color"]
})

// returns back color when Arduino asks for LED color
app.get('/lights', (req, res) => {
    res.send(colorToSend)
})

https.createServer({
    key: fs.readFileSync('/ssl/server.key'),
    cert: fs.readFileSync('/ssl/server.crt')
  }, app).listen(port, () => {
    console.log('Running on port ' + port);
  });
