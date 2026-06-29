#include <vector>
#include <string>

class Solution {
public:
    int numOfStrings(std::vector<std::string>& patterns, std::string word) {
        int count = 0;
        
        for (const std::string& pattern : patterns) {
            // string::npos is returned if the substring is NOT found
            if (word.find(pattern) != std::string::npos) {
                count++;
            }
        }
        
        return count;
    }
};