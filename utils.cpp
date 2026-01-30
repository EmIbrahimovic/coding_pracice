#include <iostream>
#include <vector>
#include <unordered_map>
#include "utils.h"

using namespace std;

void print_vector(vector<int>& vec) {
    cout << "{ ";
    for (int i = 0; i < vec.size() - 1; i++)
        cout << vec[i] << ", ";
    if (vec.size() > 0) cout << vec.back();
    cout << "}" << endl;
}
