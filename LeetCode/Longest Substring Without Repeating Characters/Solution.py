class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_num=0
        
        # 문자의 위치를 dictionary안에 저장하고 중복되는 문자가 나타났을 때는 중복되는 문자 다음 문자를 start로 옮기고 중복되는 문자가 없을 경우 그대로 진행하면서 길이를 체크
        start=0
        dic={}
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]]>=start:
                start=dic[s[i]]+1
                dic[s[i]]=i
            else:
                dic[s[i]]=i
            if i-start+1>max_num:
                max_num=i-start+1
        return max_num
        
