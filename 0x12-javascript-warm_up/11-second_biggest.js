#!/usr/bin/node
const all_args = process.argv;
const values = all_args.slice(2);

if (all_args.length == 2 || values.length == 1) {
  console.log('0');
} else {
  sorted_arr = values.sort();
  rev_arr = sorted_arr.reverse();
  second_big = rev_arr[1];
  console.log(second_big);
}
