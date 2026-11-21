class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        from collections import deque
        result = deque()
        i = len(num) - 1
        carry = 0
        while i >= 0 or k > 0 or carry > 0:
            digit = k % 10
            sum_val = carry + (num[i] if i >= 0 else 0) + digit
            result.appendleft(sum_val % 10)
            carry = sum_val // 10
            k //= 10
            i -= 1
        return list(result)