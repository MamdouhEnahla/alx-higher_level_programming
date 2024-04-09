#!/usr/bin/node
function factorial (n) {
  if (n > 1) {
    return n * factorial(n - 1);
  } else {
    return 1;
  }
}

const n = parseInt(process.argv[2], 10);
console.log(factorial(n));
