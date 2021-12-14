#!/usr/bin/node

const SquareClass = require('./5-square');

module.exports = class Square extends SquareClass {
  charPrint (c) {
    let pen;
    if (c === undefined) {
      pen = 'X';
      for (let i = 0; i < this.height; i++) {
        console.log(String(pen).repeat(this.width));
      }
    } else {
      pen = c;
      for (let i = 0; i < this.height; i++) {
        console.log(String(pen).repeat(this.width));
      }
    }
  }
};
