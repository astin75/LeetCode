import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", s)
        print(s)
        if not len(s):
            return True
        elif len(s) == 1:
            if s.isalpha():
                return True
        else:
            new_list = ""
            for i in range(len(s)):
                a = s[i]
                new_list+=a.lower()
            if len(new_list) == 1:
                return True

            r_s = new_list[::-1]
            for i in range(len(new_list)):
                a = new_list[i]
                b = r_s[i]

                if a.lower() != b.lower():
                    return False

        return True