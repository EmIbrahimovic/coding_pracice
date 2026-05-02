import typing
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_parens = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        closed_parens = {closed: opens for opens, closed in open_parens.items()}
        for c in s:
            t = stack[-1] if len(stack) else "."
            if c in open_parens:
                stack.append(c)
            else:
                if t == closed_parens[c]:
                    stack.pop()
                else:
                    return False
                
        
        return len(stack) == 0

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("()[]{}", ),
        ("(]", ),
        ("([])", ),
        ("([)]", )
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.isValid(*test)
        print(answer)

