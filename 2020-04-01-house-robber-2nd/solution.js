function robbery(nums) {
  const robbedMoney = [];
  robbedMoney[0] = nums[0];
  robbedMoney[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    robbedMoney[i] = Math.max(nums[i] + robbedMoney[i - 2], robbedMoney[i - 1]);
  }

  return robbedMoney[robbedMoney.length - 1];
}

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
  if (nums.length < 1) {
    return 0;
  }

  if (nums.length === 1) {
    return nums[0];
  }

  if (nums.length <= 3) {
    return Math.max(...nums);
  }

  return Math.max(robbery(nums.slice(1)), robbery(nums.slice(0, -1)));
};
