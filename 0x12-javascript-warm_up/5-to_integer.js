#!/usr/bin/node
const argument = process.argv[2];
const parsedNumber = parseInt(argument, 10);

if (!isNaN(parsedNumber)) {
  console.log(`My number: ${parsedNumber}`);
} else {
  console.log('Not a number');
}
