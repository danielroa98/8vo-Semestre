const MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/animals', function (err, db) {

    if (err) throw err;

    db.collection('animals').find().toArray(function (err, res) {
        if (err) throw err;

        console.log(res)
    })
})