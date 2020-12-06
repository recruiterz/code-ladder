class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        count = 0
        string = ""
        list_of_parens = []

        def append_paren(count, string, num_completed_parens):
            if num_completed_parens == n:
                list_of_parens.append(string)
                return string

            if count > num_completed_parens:
                append_paren(count, string + ")", num_completed_parens+1)

            if count < n:
                append_paren(count + 1, string + "(", num_completed_parens)

            return string

        append_paren(count, string, 0)
        return list_of_parens
