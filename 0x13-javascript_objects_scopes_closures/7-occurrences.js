#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const len = list.length;
  let idx;

  for (idx = 0; idx < len; idx++) {
    if (searchElement === list[idx]) {
      count++;
    }
  }
  return count;
};
