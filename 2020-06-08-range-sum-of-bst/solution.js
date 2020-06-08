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
 * @param {number} L
 * @param {number} R
 * @return {number}
 */
var rangeSumBST = function (root, L, R) {
  let sum = 0;

  function sumValue(node) {
    if (!node) {
      return;
    }

    if (node.val >= L && node.val <= R) {
      sum += node.val;
    }

    if (node.left && node.left.val) {
      sumValue(node.left);
    }

    if (node.right && node.right.val) {
      sumValue(node.right);
    }
  }

  sumValue(root);

  return sum;
};
