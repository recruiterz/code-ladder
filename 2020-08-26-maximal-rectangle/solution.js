/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalRectangle = function (matrix) {
  if (matrix.length === 0) {
    return 0;
  }

  const widths = new Array(matrix[0].length).fill(0);
  let size = 0;

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      if (matrix[i][j] === "1") {
        widths[j] += 1;
      } else {
        widths[j] = 0;
      }
    }
  }

  return size;
};
