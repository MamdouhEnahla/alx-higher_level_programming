#!/usr/bin/node
const request = require('request');
const num = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/' + num, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
