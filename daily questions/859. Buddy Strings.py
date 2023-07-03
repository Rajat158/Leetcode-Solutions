'''
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
 

Constraints:

1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters.
'''
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Step 1: Check if the lengths of s and goal are different
        if len(s) != len(goal):
            return False
        
        # Step 2: Check if s and goal are exactly the same
        # and there are duplicate characters in s
        if s == goal and len(set(s)) < len(s):
            return True
        
        # Step 3: Find the pairs of different characters in s and goal
        diffs = [(a, b) for a, b in zip(s, goal) if a != b]
        
        # Step 4: Check if there are exactly two different pairs of characters
        # and the first pair can be transformed into the second pair by flipping it
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
