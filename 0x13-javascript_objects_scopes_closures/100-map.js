#!/usr/bin/node
let arr = require("./main").list;
let arrLength = arr.length;
let idx;
let arrMap = arr.map((i,j) => i * j);
console.log(arr);
console.log(arrMap);
