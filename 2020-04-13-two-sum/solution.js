/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// O(n^2)
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }

  return null;
};

// O(n)
var twoSum = function (nums, target) {
  const sumMap = new Map();

  for (let lastIndex = 0; lastIndex < nums.length; lastIndex++) {
    const firstIndex = sumMap.get(target - nums[lastIndex]);

    if (firstIndex !== undefined) {
      return [firstIndex, lastIndex];
    }

    sumMap.set(nums[lastIndex], lastIndex);
  }
};
