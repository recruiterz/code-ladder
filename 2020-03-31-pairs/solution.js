"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", inputStdin => {
  inputString += inputStdin;
});

process.stdin.on("end", _ => {
  inputString = inputString
    .replace(/\s*$/, "")
    .split("\n")
    .map(str => str.replace(/\s*$/, ""));

  main();
});

function readLine() {
  return inputString[currentLine++];
}

// Complete the pairs function below.
// NOTE: brute force answer / O(n^2)
function pairs(k, arr) {
  let pairCount = 0;

  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      const result = Math.abs(arr[i] - arr[j]);

      if (result === k) {
        pairCount++;
      }
    }
  }

  return pairCount;
}

// NOTE: time complexity
function pairs(k, arr) {
  let pairCount = 0;

  arr.forEach(item => {
    if (arr.includes(item + k)) {
      pairCount++;
    }
  });

  return pairCount;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const nk = readLine().split(" ");

  const n = parseInt(nk[0], 10);

  const k = parseInt(nk[1], 10);

  const arr = readLine()
    .split(" ")
    .map(arrTemp => parseInt(arrTemp, 10));

  let result = pairs(k, arr);

  ws.write(result + "\n");

  ws.end();
}
