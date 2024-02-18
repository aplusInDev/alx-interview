#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';

request(url, (err, res) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(res.body);
    for (const character of data.characters) {
      request(character, (err, res) => {
        if (err) console.log(err);
        else {
          const data = JSON.parse(res.body);
          console.log(data.name);
        }
      });
    }
  }
});
