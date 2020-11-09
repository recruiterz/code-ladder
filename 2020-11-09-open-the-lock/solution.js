function replaceAt(value, index, word) {
  return `${value.substr(0, index)}${word}${value.substr(index + 1)}`;
}

function openLock(deadends, target) {
  const queue = [[0, '0000']];
  const deadendSet = new Set(deadends);

  while (queue.length) {
    const [turn, value] = queue.shift();

    if (value === target) {
      return turn;
    }

    if (!deadendSet.has(value)) {
      deadendSet.add(value);
    }

    const steps = [];

    for (let index = 0; index < 4; index++) {
      const nextReplacement =
        Number(value[index]) + 1 <= 9 ? Number(value[index]) + 1 : 0;
      const prevReplacement =
        Number(value[index]) - 1 >= 0 ? Number(value[index]) - 1 : 9;

      const next = replaceAt(value, index, nextReplacement);
      const prev = replaceAt(value, index, prevReplacement);

      steps.push(next, prev);
    }

    steps.forEach((step) => {
      if (!deadendSet.has(step)) {
        queue.push([turn + 1, step]);
      }
    });
  }

  return -1;
}
