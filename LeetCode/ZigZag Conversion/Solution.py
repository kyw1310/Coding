class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        pivot_string=2*(numRows-1)
        
        pivot_matrix=numRows-1
        pivot=list(range(numRows))+list(range(numRows-2,-1,-1))
        st=['']*numRows
        
        for i in range(len(s)):
            st[pivot[i%(len(pivot)-1)]]+=s[i]
        return ''.join(st)
                    
