/**
 * @param {string} S
 * @return {string}
 */
var removeDuplicates = function (S) {
  const stack = [];
  for (let index = 0; index < S.length; index++) {
    if (stack.slice(-1)[0] === S.charAt(index)) {
      stack.pop();
    } else {
      stack.push(S.charAt(index));
    }
  }
  return stack.join("");
};

var removeDuplicates = function (S) {
  const stack = [];
  for (const s of S) {
    if (stack.slice(-1)[0] === s) {
      stack.pop();
    } else {
      stack.push(s);
    }
  }
  return stack.join("");
};
