/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  if (strs.length === 0) {
    return "";
  }

  const minStrLength = Math.min(...strs.map((str) => str.length));
  let result = "";
  let index = 0;

  while (index < minStrLength) {
    const isAllEqual = strs.every((str) => str[index] === strs[0][index]);

    if (isAllEqual) {
      result += strs[0][index];
      index++;
    } else {
      break;
    }
  }

  return result;
};
