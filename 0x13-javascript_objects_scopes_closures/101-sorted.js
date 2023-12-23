#!/usr/bin/node

const inputDict = require('./101-data').dict;
// Initialize an empty dictionary for the new result
const resultDict = {};
// Iterate over the keys in the input dictionary
for (const userId in inputDict) {
  const occurrences = inputDict[userId];
  // if the occurrences value is not already a key in the result dictionary. create it
  if (!resultDict[occurrences]) {
    resultDict[occurrences] = [];
  }
  // Add the user id to the list corresponding to the occurrences value
  resultDict[occurrences].push(userId);
}
console.log(resultDict);
