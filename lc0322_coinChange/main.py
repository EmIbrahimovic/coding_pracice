from typing import List

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1

        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        for t in range(amount + 1):
            dp[0][t] = t // coins[0] if (t % coins[0] == 0) else -1
        for i in range(len(coins)):
            dp[i][0] = 0

        for i in range(1, len(coins)):
            for t in range(amount + 1):
                firstRelevant = dp[i][t - coins[i]] + 1 if t - coins[i] >= 0 and dp[i][t - coins[i]] != -1 else -1
                secondRelevant = dp[i - 1][t]
                if firstRelevant == -1 and secondRelevant == -1:
                    dp[i][t] = -1
                elif firstRelevant != -1 and secondRelevant != -1:
                    dp[i][t] = min(firstRelevant, secondRelevant)
                else:
                    dp[i][t] = max(firstRelevant, secondRelevant)

        return dp[len(coins) - 1][amount]

if __name__ == "__main__":
    sol = Solution()

    tests = [
    ([1, 2, 5], 11),
    ([2], 3),
    ([1], 0)
            ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.coinChange(*test)
        print(answer)
