/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var largestValues = function (root) {
  if (!root) {
    return [];
  }

  const queue = [{ level: 0, node: root }];
  const results = [];

  while (queue.length) {
    let { level, node } = queue.pop();

    if (node.left) {
      queue.push({ level: level + 1, node: node.left });
    }

    if (node.right) {
      queue.push({ level: level + 1, node: node.right });
    }

    if (!results[level]) {
      results.push(node.val);
    }

    if (results[level] < node.val) {
      results[level] = node.val;
    }
  }

  return results;
};
