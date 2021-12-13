#!/usr/bin/node
const arg = process.argv[2];
let i;

if (arg && isNaN(arg) === false) {
  const sqrSize = arg;

  for (i = 0; i < sqrSize; i++) {
    console.log('X'.repeat(sqrSize));
  }
} else {
  console.log('Missing size');
}
