class Solution(object):
   
        def isPalindrome(self,x):
                """
                :type x: int
                :rtype: bool
                """     
                if x < 0:
                        return False
                remainder=11
                no=x
                ans=''
                while not(len(str(no))== 1):
                    div=int(no/10)
                    remainder=no%10

                    ans=ans+str(remainder)
                    no=div
                ans=ans+str(no)
                ans=int(ans)
                if ans == x:
                        return True
                else:
                        return False
