param(
    [int]$ProblemNumber,
    [string]$FunctionName,
    [string]$ReturnType,
    [string]$Platform="lc"
)

$ProblemNumberStr = $ProblemNumber.ToString("D4")

$PlatformFull = "UnrecognizedPlatform"
if ($Platform -eq "lc") {
    $PlatformFull = "LeetCode"
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

$CppFile = "$FolderName\main.cpp"
$MdFile = "$FolderName\tricks.md"

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
---

# $PlatformFull $ProblemNumber. $FunctionName



## approach lessons



## cpp optimizations


"@


if (!(Test-Path $CppFile)) {
    $CppTemplate | Out-File $CppFile
    Write-Host "main.cpp created" -ForegroundColor Cyan
} else {
    Write-Host "main.cpp already exists" -ForegroundColor Gray
}

if (!(Test-Path $MdFile)) {
    $MdTemplate | Out-File $MdFile
    Write-Host "tricks.md created" -ForegroundColor Cyan
} else {
    Write-Host "tricks.md already exists" -ForegroundColor Gray
}
