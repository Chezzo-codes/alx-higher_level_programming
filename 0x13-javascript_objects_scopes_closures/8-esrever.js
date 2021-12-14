#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  let idx = list.length - 1; // Set to last index.

  while (idx >= 0) {
    revList.push(list[idx]);
    idx--;
  }
  return revList;
};
