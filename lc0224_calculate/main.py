from typing import List, Tuple

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    OPERATORS = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
    }

    def tokenize(self, s: str) -> List[str]:
        for operator in self.OPERATORS:
            s = s.replace(operator, f" {operator} ")
        
        for bracket in '()':
            s = s.replace(bracket, f" {bracket} ")
        
        return s.split()

    def parse(self, s: List[str], i) -> Tuple[int, int]:
        # print(i)
        if i >= len(s):
            return None, None
        
        if s[i].isnumeric():
            return int(s[i]), i + 1

        elif s[i] == '(':
            result, nextIndex = self.parse(s, i + 1)
            while nextIndex != None and nextIndex < len(s) and s[nextIndex] != ')':
                operation = self.OPERATORS[s[nextIndex]]
                nextIndex += 1
                next_operand, nextIndex = self.parse(s, nextIndex)
                result = operation(result, next_operand)
            
            # at this point we have a closed paren
            return result, nextIndex + 1

        elif s[i] == '-':
            result, nextIndex = self.parse(s, i + 1)
            return -result, nextIndex

        return None, None

    def calculate(self, s: str) -> int :
        tokenized = self.tokenize(f'({s})')
        # print(tokenized)
        value, _ = self.parse(tokenized, 0)

        return value

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("1 + 1", ),
        (" 2-1 + 2 ", ),
        ("(1+(4+5+2)-3)+(6+8)", ),
        ("(-(-1))", ),
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.calculate(*test)
        print(answer)

