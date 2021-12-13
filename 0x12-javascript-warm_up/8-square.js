#!/usr/bin/node
const arg = process.argv[2];

if (arg && isNaN(arg) == false) {
  const sqr_size = arg;

  for (i = 0; i < sqr_size; i++) {
    console.log('X'.repeat(sqr_size));
  }
} else {
  console.log('Missing size');
}
