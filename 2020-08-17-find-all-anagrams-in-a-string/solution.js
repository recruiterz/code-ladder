// FIXME: Time limit exceeded
function stringSort(letters) {
  const letterArray = letters.split("");

  letterArray.sort((a, b) => a.localeCompare(b));

  return letterArray.join("");
}

/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function (s, p) {
  const results = [];
  const sortedP = stringSort(p);

  for (let index = 0; index < s.length - p.length + 1; index++) {
    const sortedSubString = stringSort(s.slice(index, index + p.length));

    if (sortedSubString === sortedP) {
      results.push(index);
    }
  }

  return results;
};
