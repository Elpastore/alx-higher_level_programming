#!/usr/bin/node
const fs = require('fs');
const Filename = process.argv[2];
fs.readFile(Filename, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});