       def longestCommonPrefix(self,strs):
            result=""
            common=[]
            length=len(strs)
            if length==1 and strs[0]=="":
                return ""
            if  length== 1:
                    return strs[0]
            for item in strs[1:]:
                if item == "":
                        return ""
                tmp=''
                len_of_item=len(strs[0])
                for i in range (len_of_item):
                    if i < len(item):
                        if item[i] == strs[0][i]:
                            tmp=tmp+strs[0][i]
                        elif item[i] != strs[0][i] and i==0:
                            return ""
                        else:
                            break
                if tmp!='':
                    common.append(tmp)
            if len(common)!=0:
                result=min(common,key=len)
            return result

