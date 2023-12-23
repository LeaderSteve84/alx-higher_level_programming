#!/usr/bin/node

const list = require('./100-data').list;
// use map to create a new list with values multiplier by their indices
const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
