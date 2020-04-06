/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var distributeCoins = function (root) {
  if (root === null) {
    return 0;
  }

  const leftCount = distributeCoins(root.left);
  const rightCount = distributeCoins(root.right);
  let count = 0;

  if (root.left !== null && root.left.val !== 1) {
    count += Math.abs(1 - root.left.val);
    root.val += root.left.val - 1;
    root.left.val = 1;
  }

  if (root.right !== null && root.right.val !== 1) {
    count += Math.abs(1 - root.right.val);
    root.val += root.right.val - 1;
    root.right.val = 1;
  }

  return leftCount + rightCount + count;
};
