from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the input list is empty, there is no common prefix
        if not strs:
            return ""
        
        # Start by assuming the first string is the common prefix
        prefix = strs[0]
        
        # Compare the prefix with each subsequent string
        for s in strs[1:]:
            # Shrink the prefix from the end until the current string starts with it
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                
                # If the prefix becomes empty, there is no common prefix at all
                if not prefix:
                    return ""
                    
        return prefix