#!/usr/bin/node
const arg = process.argv[2];

if (arg && isNaN(arg) == false) {
  const arg2int = parseInt(arg);
  console.log('My number: ' + arg2int);
} else {
  console.log('Not a number');
}
