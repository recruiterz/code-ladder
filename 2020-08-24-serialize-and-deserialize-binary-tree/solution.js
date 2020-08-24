/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function (root) {
  let result = "";

  function serializer(node) {
    if (node === null) {
      result += "null ";
    } else {
      result += `${node.val} `;
      serializer(node.left);
      serializer(node.right);
    }
  }

  serializer(root);

  return result.slice(0, result.length - 1);
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function (data) {
  const dataToArr = data.split(" ");
  const result = deserializer();

  function deserializer() {
    const val = dataToArr.shift();

    if (val === "null") {
      return null;
    } else {
      const node = new TreeNode(val);
      node.left = deserializer();
      node.right = deserializer();

      return node;
    }
  }

  return result;
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
