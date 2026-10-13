class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # key: num, val: count
        freq = [[] for i in range(len(nums) + 1)] #initialize each frequency list for the val
        
        for n in nums:
            count[n] += 1
            #initialize the hashmap for numbers and counts. each number will map to a count
        for num, cnt in count.items(): #num is the keys, cnt is the count of each key
            # freq array is 2d array where each count has a list of numbers that are that count
            freq[cnt].append(num) #freq at index count's value list add num to it
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # last index, go till zero, subtract by one
            for num in freq[i]:
                res.append(num)
                if len(res) == k: #will always happen if k is less than n
                    return res