# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = [" flower",
#                 "flow",
#                 "flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

def longest_common_prefix(strs: list[str]) -> str:
    result = ""
    strs_len = len(strs) 
    f_str = len(strs[0])
    for i in range(f_str):
        buffer = strs[0][i]
        for j in range(1,strs_len):
            if i > len(strs[j]) or strs[j][i] != buffer:
                return result
        result += buffer    
    return result

if __name__ == "__main__":
    print( longest_common_prefix(['flower', 'flow', 'flight']) )
    assert longest_common_prefix(["dog","racecar","car"]) == ""
    assert longest_common_prefix(['flower', 'flow', 'flight']) == "fl"