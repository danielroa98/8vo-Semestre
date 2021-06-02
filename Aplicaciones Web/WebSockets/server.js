const http = require('http');
const WebSocketServer = require('websocket').server;
const server = http.createServer();

server.listen(9898);

const wServer = new WebSocketServer({
    httpServer: server
});

WebSocketServer.on('request', function (request) {
    const connection = request.accept(null, request.origin);
    connection.on('message', function (message) {
        console.log('Received message: ');
    })
})