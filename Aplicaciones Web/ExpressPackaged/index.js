const express = require('express');
const app = express();

const port = 3000;

app.get('/', (req, res) => {

    res.send('Hello, world!');

});

app.get('/user/:userId', (req, res) => {

    res.send(req.params.userId)

})

app.get('/user/:userId/books/:bookId', (req, res) => {

    res.send(req.params.userId + '\n' + req.params.bookId);

})

app.listen(port, () => {
    console.log(`Server is running in http://localhost:${port}`)
})