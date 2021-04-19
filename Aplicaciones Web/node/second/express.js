/* var http = require('http');

let port = 8000;

http.createServer(function (req, res) {
    
    console.log('Una visita');

    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<html><body><h1>')
    res.write('Alo Mundo</h1>')

    res.end('</html>')

}).listen(port);

console.log(`Server running on url http://127.0.0.1:${port}`) */

const express = require('express');
const wiki = require('./wiki.js');

const app = express();

const port = 3000;

app.get('/hello', function (req, res) {
    res.send('Hola Mundo!\n:)')
});

app.get('/about', (req, res) => {
    res.send('Bye bye!')
})

app.use('/', wiki);

app.listen(port, function () {
    console.log(`Server running on url http://127.0.0.1:${port}`)
})