const express = require('express');

const router = express.Router();

router.get('/home', function(req, res) {
    res.send('Pag. de inicio');
})

router.get('/about', function(req, res) {
    res.send('About this Wiki')
})

module.exports = router;