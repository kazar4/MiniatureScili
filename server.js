const express = require('express')
var cors = require('cors');
const app = express()
const port = 5672

var allowedOrigins = ['http://kazar4.com:5500', 'http://kazar4.com', 'http://127.0.0.1:5500', 'http://127.0.0.1.com']
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
app.get('/lights/:color', (req, res) => {
  res.send(req.params["color"])
  console.log(req.params["color"])
  colorToSend = req.params["color"]
})

// returns back color when Arduino asks for LED color
app.get('/lights', (req, res) => {
    res.send(colorToSend)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})