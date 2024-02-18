#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const chars = JSON.parse(body).characters;
    for (const character of chars) {
      const p = new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          } else {
            reject('error');
          }
        });
      });
      console.log(await p);
    }
  }
});
