#!/usr/bin/node
const num_1 = parseInt(process.argv[2]);
const num_2 = parseInt(process.argv[3]);

console.log(add(num_1, num_2));

function add (a, b) {
  return a + b;
}
