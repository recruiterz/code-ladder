/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  if (matrix.length === 0 || matrix[0].length === 0) {
    return false;
  }

  const width = matrix[0].length;
  const height = matrix.length;

  let m = width - 1;
  let n = 0;

  while (m >= 0 && n < height) {
    console.log(n, m);

    if (matrix[n][m] === target) {
      return true;
    } else if (target < matrix[n][m]) {
      m--;
    } else {
      n++;
    }
  }

  return false;
};
