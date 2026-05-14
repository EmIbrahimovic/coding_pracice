#!/usr/bin/env bash

set -e

# Defaults
PLATFORM="lc"
PLANGUAGE="all"
BETTER_CPP=0

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --problem)
            PROBLEM_NUMBER="$2"
            shift 2
            ;;
        --function)
            FUNCTION_NAME="$2"
            shift 2
            ;;
        --return)
            RETURN_TYPE="$2"
            shift 2
            ;;
        --platform)
            PLATFORM="$2"
            shift 2
            ;;
        --language)
            PLANGUAGE="$2"
            shift 2
            ;;
        --better-cpp)
            BETTER_CPP=1
            shift
            ;;
        *)
            echo "Unknown argument: $1"
            exit 1
            ;;
    esac
done

# Validation
if [[ -z "$PROBLEM_NUMBER" || -z "$FUNCTION_NAME" || -z "$RETURN_TYPE" ]]; then
    echo "Usage:"
    echo "./setup.sh --problem 1 --function twoSum --return int"
    exit 1
fi

# Zero-pad problem number
PROBLEM_NUMBER_STR=$(printf "%04d" "$PROBLEM_NUMBER")

# Platform full name
PLATFORM_FULL="UnrecognizedPlatform"

if [[ "$PLATFORM" == "lc" ]]; then
    PLATFORM_FULL="LeetCode"
elif [[ "$PLATFORM" == "spoj" ]]; then
    PLATFORM_FULL="SPOJ"
else
    echo "Warning: Platform choice $PLATFORM unrecognized"
fi

echo "Platform choice: $PLATFORM_FULL"

FOLDER_NAME="${PLATFORM}${PROBLEM_NUMBER_STR}_${FUNCTION_NAME}"

if [[ ! -d "$FOLDER_NAME" ]]; then
    mkdir "$FOLDER_NAME"
    echo "Created $FOLDER_NAME"
else
    echo "Already exists $FOLDER_NAME"
fi

PY_FILE="$FOLDER_NAME/main.py"
CPP_FILE="$FOLDER_NAME/main.cpp"
BETTER_CPP_FILE="$FOLDER_NAME/better.cpp"
MD_FILE="$FOLDER_NAME/tricks_${FUNCTION_NAME}.md"

# Python template
read -r -d '' PY_TEMPLATE << EOF || true
import typing

# shenanegans to import utils
# from pathlib import Path
# import sys
# current_file = Path(__file__).resolve()
# parent_directory = current_file.parent.parent
# sys.path.append(str(parent_directory))
from utils import *


class Solution:
    def ${FUNCTION_NAME}(self, inputs) -> ${RETURN_TYPE}:
        out: ${RETURN_TYPE}

        return out

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.${FUNCTION_NAME}(*test)
        print(answer)
EOF

# C++ template
read -r -d '' CPP_TEMPLATE << EOF || true
#include <iostream>
#include <string>
#include <vector>
#include "utils.h"

using namespace std;

class Solution {
public:
    ${RETURN_TYPE} ${FUNCTION_NAME}(/* input needed */) {
        ${RETURN_TYPE} result;

        return result;
    }
};

int main() {
    Solution sol;

    int tests[] = {

    };

    for (auto test : tests) {
        cout << sol.${FUNCTION_NAME}(test) << endl;
    }

    return 0;
}
EOF

# Markdown template
read -r -d '' MD_TEMPLATE << EOF || true
---
strongly-connected:
- "[[]]"
tags:
- problem
favorite: False
---

# ${PLATFORM_FULL} ${PROBLEM_NUMBER}. ${FUNCTION_NAME}



## approach lessons



## cpp optimizations
EOF

# Better C++ template
read -r -d '' BETTER_CPP_TEMPLATE << EOF || true
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
EOF

# Create files
if [[ ("$PLANGUAGE" == "cpp" || "$PLANGUAGE" == "all") && ! -f "$CPP_FILE" ]]; then
    echo "$CPP_TEMPLATE" > "$CPP_FILE"
    echo "main.cpp created"
else
    echo "python selected or main.cpp already exists"
fi

if [[ ("$PLANGUAGE" == "py" || "$PLANGUAGE" == "all") && ! -f "$PY_FILE" ]]; then
    echo "$PY_TEMPLATE" > "$PY_FILE"
    echo "main.py created"
else
    echo "cpp selected or main.py already exists"
fi

if [[ ! -f "$MD_FILE" ]]; then
    echo "$MD_TEMPLATE" > "$MD_FILE"
    echo "tricks_${FUNCTION_NAME}.md created"
else
    echo "tricks_${FUNCTION_NAME}.md already exists"
fi

if [[ "$BETTER_CPP" -eq 1 && ! -f "$BETTER_CPP_FILE" ]]; then
    echo "$BETTER_CPP_TEMPLATE" > "$BETTER_CPP_FILE"
    echo "better.cpp created"
else
    echo "BetterCpp not selected or better.cpp already exists"
fi
