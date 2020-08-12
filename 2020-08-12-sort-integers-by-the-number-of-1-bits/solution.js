/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function (arr) {
  arr.sort((a, b) => a - b);

  const bits = arr.map((item) => ({
    item,
    oneCount: item.toString(2).split("").reduce(
      (result, item) => item === "1" ? result + 1 : result,
      0,
    ),
  }));

  bits.sort((a, b) => a.oneCount - b.oneCount);

  return bits.map(({ item }) => item);
};
