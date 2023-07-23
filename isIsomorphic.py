def isIsomorphic(s: str, t: str):
    new_dict={}
    for i in range(0,len(s)):
        val=new_dict.values()
        #print(s[i],t[i],val)
        if (s[i] not in new_dict) and (t[i] not in val):
             new_dict[s[i]]=t[i]
        elif s[i] in new_dict  and new_dict[s[i]]==t[i]:
                continue
        else: 
            return False   
    return True 