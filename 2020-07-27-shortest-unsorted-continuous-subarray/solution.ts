function findUnsortedSubarray(nums: number[]): number {
    let left = nums.length;
    let right = 0;

    for (let i = 0; i < nums.length - 1; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] > nums[j]) {
                right = Math.max(right, j);
                left = Math.min(left, i);
            }
        }
    }

    if (right - left < 0) {
        return 0;
    }

    return right - left + 1;
}
