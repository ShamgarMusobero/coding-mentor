from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)
        return list(anagrams.values())

# Line 1: from collections import defaultdict 
# This line imports the defaultdict class from the collections module.

# Line 4: class Solution:
# This line defines a class called Solution.

# Line 5: def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# This line defines a function called groupAnagrams that takes a list of strings as an argument and returns a list of list of strings. 

# Line 6: anagrams = defaultdict(list)
# This line creates a default dictionary called anagrams with a value type of list.

# Line 7: for s in strs:
