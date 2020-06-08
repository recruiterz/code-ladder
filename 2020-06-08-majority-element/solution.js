/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  let majority = null;
  const elements = new Map();

  for (const num of nums) {
    if (elements.has(num)) {
      elements.set(num, elements.get(num) + 1);
    } else {
      elements.set(num, 1);
    }
  }

  for (const [num, count] of elements) {
    if (count > nums.length / 2) {
      majority = num;
    }
  }

  return majority;
};
