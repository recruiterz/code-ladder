/**
 * @param {number} k
 * @param {number} W
 * @param {number[]} Profits
 * @param {number[]} Capital
 * @return {number}
 */
var findMaximizedCapital = function (k, W, Profits, Capital) {
  const profitCapitals = Profits
    .map((profit, index) => [profit, Capital[index]])
    .sort((a, b) => b[0] - a[0]);

  while (k > 0) {
    const index = profitCapitals.findIndex(([profit, capital]) => W >= capital);

    if (index === -1) {
      break;
    }

    const [profit, capital] = profitCapitals[index];
    W += profit;
    profitCapitals.splice(index, 1);
    k--;
  }

  return W;
};
