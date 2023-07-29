class Solution:
    def sortSentence(self, s: str) -> str:
        lis=s.split()
        dic={}
        for i in lis:
            dic[i[-1]]=i[:-1]
        return ' '.join([dic[j] for j in sorted(dic)])  