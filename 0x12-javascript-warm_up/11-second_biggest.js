#!/usr/bin/node
const allArgs = process.argv;
const values = allArgs.slice(2);

if (allArgs.length === 2 || values.length === 1) {
  console.log('0');
} else {
  const sortedArr = values.sort();
  const revArr = sortedArr.reverse();
  const secondBig = revArr[1];
  console.log(secondBig);
}
