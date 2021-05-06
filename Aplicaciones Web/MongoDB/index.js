const MongoClient = require('mongodb').MongoClient;
const express = require('express');
const app = express()
const port = 3000
const path = require('path');
const router = express.Router();
const bodyParser = require('body-parser')

const uri = "mongodb+srv://dndadmin:.DnDadm1n.@proyectofinal.heiln.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

app.use(express.urlencoded({ extended: true }));

app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});

app.post('/dbsignup', function (req, res) {
    console.log(req.body);
    dbConnect(req.body);
    res.sendFile(path.join(__dirname + '/index.html'));
});

async function dbConnect(body) {
    try {
        const client = await MongoClient.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true, });
        const collection = client.db("Actividad").collection("persona");
        await collection.insertOne({ name: body.Nombre, surname1: body.PrimerApellido, surname2: body.SegundoApellido, birthday: body.FechaNacimiento });
        client.close();
    } catch (error) {
        console.log(error);
    }
}

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})

module.exports = app;