class Solution:
    def twoSum(self, nums, target):
        hash_dict={}
        index=0
        sol=[]
        for i in nums:
            if target-i not in hash_dict:
                hash_dict[i]=index
                index+=1
            else:
                return [hash_dict[target-i],index]