class Solution(object):
    def isPalindrome(self, s):
        word=""
        
        for i in s:
            if i.isalnum():
                word+=i.lower()
    

        if word==word[::-1]:
           return True
        