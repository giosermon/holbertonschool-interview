#!/usr/bin/node
const request = require('request');
const process = require('process');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request({ url: url }, (err1, res, body) => {
  const nid = [];
  const bjs = JSON.parse(body);
  bjs.characters.forEach(urls => {
    const id = urls.split('/')[5];
    request({ url: urls }, (err2, res, body) => {
      const bjs1 = JSON.parse(body);
      nid[id] = bjs1.name;
    });
  });
  setTimeout(function () {
    bjs.characters.forEach(element => {
      const id = element.split('/')[5];
      console.log(nid[id]);
    });
  }, 1000);
});
