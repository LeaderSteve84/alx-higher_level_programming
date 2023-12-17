#!/usr/bin/node

const fs = require('fs');
// check if the correct number of argument is provided
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}
// Extract file paths from command line arguments
const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const fileCPath = process.argv[4];

// Read the content of the first source file
fs.readFile(fileAPath, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  // Read the content of the second file
  fs.readFile(fileBPath, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
    // concatenate the content of both files
    const concatenatedContent = dataA + dataB;
    // Write the concatenated content to the rigth destination
    fs.writeFile(fileCPath, concatenatedContent, 'utf8', (err) => {
      if (err) {
        console.error(err);
        process.exit(1);
      }
      console.log(`Files ${fileAPath} and ${fileBPath} have been concatenated to ${fileCPath}`);
    });
  });
});
