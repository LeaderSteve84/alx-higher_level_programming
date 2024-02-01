#!/usr/bin/node
// display the status code of a GET request.

const req = require('request');
const url = process.argv[2];
req.get(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:' + ' ' + response.statusCode);
  }
});
