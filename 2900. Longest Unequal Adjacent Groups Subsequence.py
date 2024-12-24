class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if(len(words)<=0):
            return []
        last = groups[0]
        string = [words[0]]
        for i in range(1,len(words)):
            if(groups[i]!=last):
                last = groups[i]
                string+=[words[i]]
        return string
