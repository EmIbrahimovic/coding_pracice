#include <iostream>
#include <vector>
#include <unordered_map>
#include "utils.h"

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> elements;
        vector<int> answer;
        for (int i = 0; i < nums.size(); i++) {
            int other = target - nums[i];
            if (elements.find(other) != elements.end()) {
                answer.push_back(i);
                answer.push_back(elements[other]);
                break;
            }
            
            elements[nums[i]] = i;
        }

        return answer;
    }
};

int main(){
    Solution sol;

    vector<int> input1 = {0, 1, 2, 4, 5};
    int target = 5;
    vector<int> result = sol.twoSum(input1, target);

    print_vector(result);
    cout << "debug msg" << endl;

    return 0;
}
