
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        refmap = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

        digits = [int(x) for x in digits]
        reslist = []
        tset = []
        n = len(digits)


        def dfs(prev):
            if len(tset) == n:
                string = ""
                for x in tset:
                    string += str(x)
                reslist.append(string)
                return
            
            for i in refmap[digits[prev]]:
                tset.append(i)
                dfs(prev+1)
                tset.pop()

        
        dfs(0)
        return reslist       