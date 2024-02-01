#!/usr/bin/node
// computes the number of tasks completed by user id

const req = require('request');
req.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const completedtasks = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!completedtasks[todo.userId]) {
        completedtasks[todo.userId] = 1;
      } else {
        completedtasks[todo.userId] += 1;
      }
    }
  });
  console.log(completedtasks);
});
