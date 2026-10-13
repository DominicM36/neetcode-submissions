class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # key: {1e, 1a, 1t} Val: ['eat', 'tea']

        for s in strs:
            count = [0] * 26 # a...z
            for c in s:
                count[ord(c) - ord("a")] += 1 #gets ascii val and subtracts first val a
            res[tuple(count)].append(s)
        return res.values()

