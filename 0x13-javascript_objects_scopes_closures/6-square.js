#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let side = '';
      for (let j = 0; j < this.width; j++) {
        side += c;
      }
      console.log(side);
    }
  }
}
module.exports = Square;
