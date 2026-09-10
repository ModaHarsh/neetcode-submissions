class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(i, string, op, cl):
            if cl > op:
                return
            if op > (n):
                return
            if i == (2 * n):
                res.append(string)
                return
            backtrack(i + 1, string + '(', op + 1, cl)
            backtrack(i + 1, string + ')', op, cl + 1)
        backtrack(0, "", 0, 0)
        return res