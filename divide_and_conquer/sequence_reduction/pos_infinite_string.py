"""
Link: https://www.geeksforgeeks.org/problems/the-infinite-string1049/1

Time Complexity: O(log(pos))
- String length more than doubles at each step, so finding the required level takes O(log(pos)) steps.
- Tracing back down to level 0 also takes O(log(pos)) steps.

Space Complexity: O(log(pos))
- The length list stores the string size at each level up to O(log(pos)).

Concept:
- Instead of building the infinite string, track the total string length at each expansion level until it covers pos.
- Trace pos backward level by level to map it back to the original string s.
- Why it works:
  - At step i (level), the string transforms from S_prev into: [S_prev] + [i '$' characters] + [reverse(S_prev)].
  - Total length formula: cur_len = 2 * prev_len + level.
  - This represents the two copies of S_prev plus the middle block of 'level' dollar signs.
  - Tracing backward from the current level (1-based indexing):
    - Part 1 (pos <= prev_len):
      - pos lies in the unchanged first half (S_prev), so pos stays the same.
    - Part 2 (prev_len < pos <= prev_len + level):
      - pos lands in the middle '$' block, so immediately return '$'.
    - Part 3 (pos > prev_len + level):
      - pos lies in the reversed copy at the end.
      - Because [S_prev] + ['$' * level] + [reverse(S_prev)] is symmetric around its center, Part 3 is the exact mirror image of Part 1.
      - The mirror index from the right end is cur_len - pos + 1, which maps pos back to its exact index in Part 1.
"""


def posInfinite(s, pos):
    level = 0
    length = [len(s)]
    
    while length[-1]<pos:
        level += 1
        length.append(2*length[-1]+level)
        
    while level>0:
        prev_len = length[level-1]
        cur_len = length[level]
        
        if pos<=prev_len: # if pos in part1
            pass
        elif pos <= prev_len + level:
            return '$'
        else:
            pos = cur_len - pos + 1
        
        level -= 1
        
    return s[pos-1]
        