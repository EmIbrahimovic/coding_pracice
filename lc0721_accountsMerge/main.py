from typing import List
from collections import defaultdict
# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
# from utils import *


class Solution:
    def accountsMerge(self, accounts: List[str]) -> List[List[str]]:
        idx_to_email = {i: account[1:] for i, account in enumerate(accounts) }
        email_to_idx = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_idx[email].append(i)

        assigned_idx = { email: None for email in email_to_idx }
        visited_idx = set()
        def dfs(idx_or_email, Idx):
            if isinstance(idx_or_email, str):
                assigned_idx[idx_or_email] = Idx
                for idx in email_to_idx[idx_or_email]:
                    if idx not in visited_idx:
                        dfs(idx, Idx)

            elif isinstance(idx_or_email, int):
                visited_idx.add(idx_or_email)
                for email in idx_to_email[idx_or_email]:
                    if assigned_idx[email] is None:
                        dfs(email, Idx)

        for idx in range(len(accounts)):
            if idx not in visited_idx:
                dfs(idx, idx)
        
        accounts_mid = defaultdict(list)
        for email, idx in assigned_idx.items():
            accounts_mid[idx].append(email)

        final_accs = []
        for acc, emails in accounts_mid.items():
            emails.sort()
            final_accs.append([accounts[acc][0]] + emails)

        return final_accs

if __name__ == "__main__":
    sol = Solution()

    tests = [
            ([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]], ),
            ([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]],),
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.accountsMerge(*test)
        print(answer)
