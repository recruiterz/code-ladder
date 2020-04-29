/**
 * @param {string} s
 * @return {string[]}
 */
var removeInvalidParentheses = function (s) {
  const results = new Set();
  let leftInvalidCount = 0;
  let rightInvalidCount = 0;

  for (let index = 0; index < s.length; index++) {
    if (s.charAt(index) === "(") {
      leftInvalidCount++;
    }

    if (s.charAt(index) === ")") {
      if (leftInvalidCount > 0) {
        leftInvalidCount--;
      } else {
        rightInvalidCount++;
      }
    }
  }

  function discardOrContinue(
    leftInvalidCount,
    rightInvalidCount,
    index,
    open,
    validAnswer
  ) {
    if (leftInvalidCount < 0 || rightInvalidCount < 0 || open < 0) {
      return;
    }

    if (index === s.length) {
      if (leftInvalidCount === 0 && rightInvalidCount === 0 && open === 0) {
        results.add(validAnswer);
      }

      return;
    }

    if (s.charAt(index) === "(") {
      discardOrContinue(
        leftInvalidCount - 1,
        rightInvalidCount,
        index + 1,
        open,
        validAnswer
      );
      discardOrContinue(
        leftInvalidCount,
        rightInvalidCount,
        index + 1,
        open + 1,
        `${validAnswer}${s.charAt(index)}`
      );
    } else if (s.charAt(index) === ")") {
      discardOrContinue(
        leftInvalidCount,
        rightInvalidCount - 1,
        index + 1,
        open,
        validAnswer
      );
      discardOrContinue(
        leftInvalidCount,
        rightInvalidCount,
        index + 1,
        open - 1,
        `${validAnswer}${s.charAt(index)}`
      );
    } else {
      discardOrContinue(
        leftInvalidCount,
        rightInvalidCount,
        index + 1,
        open,
        `${validAnswer}${s.charAt(index)}`
      );
    }
  }

  discardOrContinue(leftInvalidCount, rightInvalidCount, 0, 0, "");

  return [...results.values()];
};
