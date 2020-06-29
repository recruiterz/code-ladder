/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function (days, costs) {
  const minimumCosts = new Array(days[days.length - 1] + 1);
  minimumCosts[0] = 0;

  for (let day = 1; day < minimumCosts.length; day++) {
    if (days.includes(day)) {
      minimumCosts[day] = Math.min(
        minimumCosts[Math.max(0, day - 1)] + costs[0],
        minimumCosts[Math.max(0, day - 7)] + costs[1],
        minimumCosts[Math.max(0, day - 30)] + costs[2]
      );
    } else {
      minimumCosts[day] = minimumCosts[day - 1];
    }
  }

  return minimumCosts[minimumCosts.length - 1];
};
