#include <string>
#include <queue>
#include <iostream>
#include <vector>
#include "utils.h"

using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int charsNote[27] = {0}, charsMag[27] = {0};

        for (auto c : magazine) charsMag[c - 'a']++;
        for (auto c : ransomNote) charsNote[c - 'a']++;

        for (int i = 0; i < 26; i++) {
            if (charsNote[i] > charsMag[i])
                return false;
        }

        return 1;
    }
};
