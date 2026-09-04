class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str_ele in strs:
            #creating letter frequency using index list
            lfreq_list = [0] * 26
            for l in str_ele:
                lfreq_list[ord(l)-ord('a')] +=1
            res[tuple(lfreq_list)].append(str_ele)
        return list(res.values())