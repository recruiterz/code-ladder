/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function (graph) {
  const paths = []
  const currentPath = [0]

  function findPath(entryPoint) {
    if (entryPoint === graph.length - 1) {
      paths.push([...currentPath]);
    } else {
      graph[entryPoint].forEach(node => {
        currentPath.push(node);
        findPath(node);
        currentPath.pop();
      })
    }
  }

  findPath(0);

  return paths;
};
