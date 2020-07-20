function countSubstrings(s: string): number {
    let dp: string[] = s.split("");

    for (let firstIndex = 0; firstIndex < s.length; firstIndex++) {
        let lastIndex: number = firstIndex + 1;
        let substring: string = s[firstIndex];

        while (lastIndex < s.length) {
            let isPalindromic: boolean = true;
            substring += s[lastIndex];

            for (
                let substringIndex = 0;
                substringIndex < substring.length;
                substringIndex++
            ) {
                if (
                    substring[substringIndex] !==
                    substring[substring.length - substringIndex - 1]
                ) {
                    isPalindromic = false;
                }
            }

            if (isPalindromic) {
                dp.push(substring);
            }

            lastIndex++;
        }
    }

    return dp.length;
}
