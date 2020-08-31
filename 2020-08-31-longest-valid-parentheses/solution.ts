function longestValidParentheses(s: string): number {
  const stack: number[] = [];
  const invalids: number[] = [];

  for (let index = 0; index < s.length; index++) {
    if (s[index] === '(') {
      stack.push(index);
    } else {
      if (stack.length > 0) {
        stack.pop();
      } else {
        invalids.push(index);
      }
    }
  }

  while (stack.length > 0) {
    invalids.push(stack.pop() as number);
  }

  let max = 0;
  let count = 0;

  for (let index = 0; index <= s.length; index++) {
    if (index < s.length && !invalids.includes(index)) {
      count++;
    } else {
      max = Math.max(max, count);
      count = 0;
    }
  }

  return max;
}
