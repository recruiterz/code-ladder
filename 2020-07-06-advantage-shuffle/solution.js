/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var advantageCount = function (A, B) {
  const result = [];
  A.sort((a, b) => a - b);

  for (let bIndex = 0; bIndex < B.length; bIndex++) {
    let aIndex = 0;

    while (A[aIndex] <= B[bIndex]) {
      aIndex++;
    }

    aIndex = aIndex < A.length ? aIndex : 0;
    result.push(A[aIndex]);
    A.splice(aIndex, 1);
  }

  return result;
};
