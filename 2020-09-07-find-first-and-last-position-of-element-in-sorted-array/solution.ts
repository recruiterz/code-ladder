function searchRange(nums: number[], target: number): number[] {
  const result: [number, number] = [-1, -1];

  nums.forEach((item, index) => {
    if (item === target) {
      if (result[0] === -1) {
        result[0] = index;
        result[1] = index;
      } else {
        result[1] = index;
      }
    }
  });

  return result;
}

function searchRange(nums: number[], target: number): number[] {
  return nums.reduce((result, num, index) => {
    if (num === target) {
      if (result[0] === -1) {
        return [index, index];
      }

      return [result[0], index];
    }

    return result;
  }, [-1, -1]);
}
