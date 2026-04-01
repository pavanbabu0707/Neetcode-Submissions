class Solution:
    def isValid(self, s: str) -> bool:

        val_str = []
        op_br = ('(','[','{')

        for ch in s:
            if ch in op_br:
                val_str.append(ch)
            else:
                if val_str == []:
                    return False
            
                top = val_str.pop()

                if ch == ')' and top != '(':
                    return False
                if ch == ']' and top != '[':
                    return False
                if ch == '}' and top != '{':
                    return False

        return val_str == []
