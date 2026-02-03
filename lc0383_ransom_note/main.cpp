#include <string>
#include <queue>
#include <iostream>
#include <vector>
#include "utils.h"

using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int charsMag[27] = {0};

        for (auto c : magazine) charsMag[c - 'a']++;
        for (auto c : ransomNote) {
            charsMag[c - 'a']--;
            if (charsMag[c - 'a'] < 0)
                return false;
        }

        return 1;
    }
};
