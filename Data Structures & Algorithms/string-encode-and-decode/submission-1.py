class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_str = ""
        for i in range(len(strs)):
            word_length = len(strs[i])
            ret_str = ret_str + str(word_length) + '#' + strs[i]

        return ret_str

    def decode(self, s: str) -> List[str]:
        i = 0
        ret_list = []
        next_str_len = ""
        while i < len(s):
            #not delim, add to length str
            if s[i] != '#':
                next_str_len = next_str_len + s[i]
                i += 1
            if s[i] == '#':
                numlen = int(next_str_len)
                ret_list.append(s[i+1:i+1+int(next_str_len)])
                i = i + 1 + int(next_str_len)
                next_str_len = ""
            
        return ret_list
