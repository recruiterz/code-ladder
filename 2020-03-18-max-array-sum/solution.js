"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", inputStdin => {
  inputString += inputStdin;
});

process.stdin.on("end", function() {
  inputString = inputString
    .replace(/\s*$/, "")
    .split("\n")
    .map(str => str.replace(/\s*$/, ""));

  main();
});

function readLine() {
  return inputString[currentLine++];
}

// Complete the maxSubsetSum function below.
function maxSubsetSum(arr) {
  const result = [Math.max(arr[0], 0), Math.max(arr[0], arr[1], 0)];

  for (let i = 2; i < arr.length; i++) {
    result.push(Math.max(result[i - 1], result[i - 2] + arr[i]));
  }

  return result.slice(-1);
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine(), 10);

  const arr = readLine()
    .split(" ")
    .map(arrTemp => parseInt(arrTemp, 10));

  const res = maxSubsetSum(arr);

  ws.write(res + "\n");

  ws.end();
}
