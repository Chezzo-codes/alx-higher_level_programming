#!/usr/bin/node
const num = parseInt(process.argv[2]);

console.log(factorial(num));

function factorial (int) {
  if (isNaN(int) == true) {
    return 1;
  } else if (int == 0) {
    return 1;
  } else {
    return int * factorial(int - 1);
  }
}
