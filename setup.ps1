param(
    [int]$ProblemNumber,
    [string]$FunctionName,
    [string]$ReturnType,
    [string]$Platform="lc",
    [string]$PLanguage="all",
    [bool]$BetterCpp=0
)

$ProblemNumberStr = $ProblemNumber.ToString("D4")

$PlatformFull = "UnrecognizedPlatform"
if ($Platform -eq "lc") {
    $PlatformFull = "LeetCode"
} elseif ($Platform -eq "spoj") {
    $PlatformFull = "SPOJ"
} else {
    Write-Host "Warning: Platform choice $Platform unrecognized" -ForegroundColor Red
}
Write-Host "Platform choice: $PlatformFull" -ForegroundColor Green

$FolderName = "$Platform$($ProblemNumberStr)_$FunctionName"

if (!(Test-Path $FolderName)) {
    New-Item -Path $FolderName -ItemType Directory
    Write-Host "Created $FolderName" -ForegroundColor Yellow
} else {
    Write-Host "Already exists $FolderName" -ForegroundColor Gray
}

$PyFile = "$FolderName\main.py"
$CppFile = "$FolderName\main.cpp"
$BetterCppFile = "$FolderName\better.cpp"
$MdFile = "$FolderName\tricks_$FunctionName.md"

$PyTemplate = @"
import typing

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
from utils import *


class Solution:
    def $FunctionName(self, inputs) -> $ReturnType :
        out: $ReturnType

        return out

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.$FunctionName(*test)
        print(answer)

"@

$CppTemplate = @"
#include <iostream>
#include <string>
#include <vector>
#include "utils.h"

using namespace std;

class Solution {
public:
    $ReturnType $FunctionName(/* input needed */) {
        $ReturnType result;

        return result;
    }
};

int main() {
    Solution sol;
    /* input type + inputs needed */
    int tests[] = {

    };

    // Use utils if complex output
    for (auto test : tests) {
        cout << sol.$FunctionName(test) << endl;
    }

    return 0;
}

"@

$MdTemplate = @"
---
strongly-connected:
- "[[]]"
tags:
- problem
favorite: False
---

# $PlatformFull $ProblemNumber. $FunctionName



## approach lessons



## cpp optimizations


"@

$BetterCppTemplate = @"
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

int main() {

    int t;
    cin >> t;

    while (t--) {

        
    }

    return 0;
}
"@


if (($PLanguage -eq "cpp" -or $PLanguage -eq "all") -and !(Test-Path $CppFile)) {
    $CppTemplate | Out-File $CppFile
    Write-Host "main.cpp created" -ForegroundColor Cyan
} else {
    Write-Host "python selected or main.cpp already exists" -ForegroundColor Gray
}

if (($PLanguage -eq "py" -or $PLanguage -eq "all") -and !(Test-Path $PyFile)) {
    $PyTemplate | Out-File $PyFile
    Write-Host "main.py created" -ForegroundColor Cyan
} else {
    Write-Host "cpp selected or main.py already exists" -ForegroundColor Gray
}

if (!(Test-Path $MdFile)) {
    $MdTemplate | Out-File $MdFile
    Write-Host "tricks_$FunctionName.md created" -ForegroundColor Cyan
} else {
    Write-Host "tricks_$FunctionName.md already exists" -ForegroundColor Gray
}

if (($BetterCpp -eq 1) -and !(Test-Path $BetterCppFile)) {
    $BetterCppTemplate | Out-File $BetterCppFile
    Write-Host "better.cpp created" -ForegroundColor Cyan
} else {
    Write-Host "BetterCpp not selected or better.cpp already exists" -ForegroundColor Gray
}
