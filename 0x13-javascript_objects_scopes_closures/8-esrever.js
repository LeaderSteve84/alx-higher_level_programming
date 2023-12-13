#!/usr/bin/node

exports.esrever = function (list) {
  // create a new array to store the reversed elements
  const reversedList = [];

  // iterate through the original list in reverse order.
  for (let i = list.length - 1; i >= 0; i--) {
    // add each element to the reversedList array
    reversedList.push(list[i]);
  }

  return reversedList;
};
