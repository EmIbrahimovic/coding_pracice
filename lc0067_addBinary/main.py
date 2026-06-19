from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = ""
        
        while len(a) < len(b):
            a = "0" + a
        while len(b) < len(a):
            b = "0" + b

        carry = 0
        i = len(a) - 1
        while i >= 0:
            summy = (a[i] == '1') + (b[i] == '1') + carry
            carry = summy // 2
            c = str(summy % 2) + c
            i -= 1
        if carry:
            c = '1' + c
        return c

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("11", "1"),
        ("1010", "1011")
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.addBinary(*test)
        print(answer)
