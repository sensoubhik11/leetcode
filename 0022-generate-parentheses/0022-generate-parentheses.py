class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def gen_util(open_cnt, close_cnt, s, res):
            if len(s) == 2*n:
                res.append(s)
                return
            if open_cnt < n:
                s = s+"("
                gen_util(open_cnt+1, close_cnt, s, res)
                s = s[:-1]
            if close_cnt < open_cnt:
                s = s+")"
                gen_util(open_cnt, close_cnt+1, s, res)
        gen_util(0,0,"",res)
        return res