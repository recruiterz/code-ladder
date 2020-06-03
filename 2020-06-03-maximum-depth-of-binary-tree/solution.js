/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
// DFS
var maxDepth = function (root) {
  if (!root) {
    return 0;
  }

  return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
};

// BFS
var maxDepth = function (root) {
  if (!root) {
    return 0;
  }

  let depth = 0;
  const queue = [[root, depth]];

  while (queue.length) {
    const [node, level] = queue.shift();

    if (node.left) {
      queue.push([node.left, level + 1]);
    }

    if (node.right) {
      queue.push([node.right, level + 1]);
    }

    depth = Math.max(depth, level + 1);
  }

  return depth;
};
