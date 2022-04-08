#!/usr/bin/node
const request = require('request');

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        console.log(JSON.parse(body).name);
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}
// hi
let chars;
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, async function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  chars = JSON.parse(body).characters;
  let x;
  if (chars) {
    for (x of chars) {
      await doRequest(x);
      // console.log(JSON.parse(res.body).name);
    }
  }
});
