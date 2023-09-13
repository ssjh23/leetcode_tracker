from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    # We retrieve the shortest word in the list
    strs.sort(key=len)
    shortest_word = strs[0]
    longest_prefix = ""
    stop_loop = False
    # We iterate through the shortest word
    for i in range(len(shortest_word)):
        # We iterate through the list of strs
        for other_word in strs:
            if shortest_word[i] != other_word[i]:
                # On the first instance of the ith letter in shortest_word and other word not matching, we break the loop, as the longest prefix has been found
                stop_loop = True
                break
        if stop_loop:
            break
        longest_prefix = shortest_word[:i+1]
    return longest_prefix

result = longestCommonPrefix(["dog","racecar","car"])
print(result)
