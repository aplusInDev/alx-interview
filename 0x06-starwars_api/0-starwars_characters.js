#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const chars = JSON.parse(body).characters;
    for (const character of chars) {
      const requestPromise = new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          }
          if (error) {
            reject(error);
          }
        });
      });
      console.log(await requestPromise);
    }
  }
});
