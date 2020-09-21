function maxArea(heights: number[]): number {
  let area = 0;
  let leftIndex = 0;
  let rightIndex = heights.length - 1;

  while (leftIndex < rightIndex) {
    const leftHeight = heights[leftIndex];
    const rightHeight = heights[rightIndex];
    area = Math.max(
      area,
      Math.min(leftHeight, rightHeight) * (rightIndex - leftIndex)
    );

    if (leftHeight < rightHeight) {
      leftIndex += 1;
    } else {
      rightIndex -= 1;
    }
  }

  return area;
}
