function checkEqual(former, latter) {
  return former.every((item) => latter.includes(item));
}

/**
 * @param {number} N
 * @param {number[][]} dislikes
 * @return {boolean}
 */
var possibleBipartition = function (N, dislikes) {
  let isPossible = true;
  const graph = {};
  const groupOne = [];
  const groupTwo = [];

  for (const [i, j] of dislikes) {
    if (graph[i]) {
      graph[i].push(j);
    } else {
      graph[i] = [j];
    }

    if (graph[j]) {
      graph[j].push(i);
    } else {
      graph[j] = [i];
    }
  }

  // FIXME: use graph
  for (let person = 1; person < N + 1; person++) {
    groupOne.push(person);

    for (let [node, edges] of Object.entries(graph)) {
      edges.forEach((edge) => {
        if (checkEqual([parseInt(node, 10), edge], groupOne)) {
          groupTwo.push(groupOne.pop());
        }
      });

      edges.forEach((edge) => {
        if (checkEqual([parseInt(node, 10), edge], groupTwo)) {
          console.log([node, edge], groupOne, groupTwo);

          isPossible = false;
        }
      });
    }
  }

  return isPossible;
};
