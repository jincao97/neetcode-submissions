class Solution:

    def encode(self, strs: List[str]) -> str:
        str_len = []
        delim_ct = 0
        for s in strs:
            str_len.append(str(len(s)))
            delim_ct += 1
        return str(delim_ct) + "," + ",".join(str_len) + "," + "".join(strs)
        

    def decode(self, s: str) -> List[str]:
        res = []
        delim_tracker = 0
        total_word = -1
        i = 0
        while delim_tracker != total_word:
            j = i
            while s[j] != ",":
                j += 1
            if total_word == -1:
                total_word = int(s[i:j])
            else:
                res.append(int(s[i:j]))
                delim_tracker += 1
                
            i = j+1
        prefix_count = i
        output = []
        for num_l in res:
            word_end = prefix_count+num_l
            output.append(s[prefix_count:word_end])
            prefix_count+=num_l
        return output

