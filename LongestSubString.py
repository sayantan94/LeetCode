class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        n = len(s)
        params = dict()
        st = 0
        maxLen = 0
        currLen = 0
        start = 0
        bQ = True
        
        for i in range(0,n):
            if s[i] not in params:
                params[s[i]] = i
            else:
                if params[s[i]] >= start:
                    currLen = i - start
                    if currLen > maxLen:
                        maxLen = currLen
                        st = start
                    start = params[s[i]] + 1
                
                params[s[i]] = i
                
        maxLen = max(maxLen,len(s[start:i]) + 1)
        return (maxLen)
        
        print (maxLen)
        
        print (start, st, currLen)
        return (maxLen + 1 if bQ else maxLen)
if __name__ == '__main__':
    print (Solution().lengthOfLongestSubstring("pwwkew"))
    
    
    
    
    
    
    