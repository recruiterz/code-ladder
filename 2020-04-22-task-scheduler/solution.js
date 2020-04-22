/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function (tasks, n) {
  if (n === 0) {
    return tasks.length;
  }

  let interval = 0;
  const queue = [];

  while (tasks.length) {
    const queueLength = queue.length;

    tasks.forEach((task, index) => {
      if (!queue.slice(-n).includes(task)) {
        queue.push(...tasks.splice(index, 1));
        interval++;
      }
    });

    if (queueLength === queue.length) {
      queue.push("idle");
      interval++;
    }
  }

  return interval;
};
