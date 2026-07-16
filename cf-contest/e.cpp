#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>

using namespace std;

void outputit(string verdict, string config) {
    cout << verdict << endl;
    if (verdict == "possible") {
        cout << config << endl;
    }
}

int main() {
    int n;
    cin >> n;

    vector<int> nerv(n);
    for (int i = 0; i < n; i++) {
        cin >> nerv[i];
    }

    string verdict = "possible";
    string config = "";
    bool certain = 0;
    if (n == 0) {
        verdict = "possible";
    } else if (n == 1) {
        verdict = (nerv[0] == 0) ? "possible" : "impossible";
        config = ">";
    } else if (n == 2) {
        if (nerv[0] == nerv[1] && nerv[0] == 1) {
            config = "><";
        } else if (nerv[0] == nerv[1] && nerv[0] == 0) {
            config = "<>";
        } else if (nerv[0] == 1 && nerv[1] == 0) {
            config = "<<";
        } else if (nerv[0] == 0 && nerv[1] == 1) {
            config = "<<";
        } else {
            verdict = "impossible";
        }
    } else {
        int i = 2;
        int menright = 0;
        int left = 0;

        if (nerv[0] == nerv[1]) {
            int x = nerv[0];
            config = "><";
            if (nerv[2] - 1 /* ppl to the right of 2*/ == ) {
                config += "<";
                left = 1;
                menright = nerv[2] - 1; // which is nerv[1] - 2
            } else if (nerv[2] - 1 == nerv[1]) {
                config += ">";
                left = 2;
                menright = nerv[2] - 1; // which is nerv[1] - 1
            } else if {
                
            }
            else {
                verdict = "impossible";
            }
            i = 3;
        }
        else if (nerv[0] == nerv[1] + 1) {
            config = "<<";

            i = 2;
            left = 0;
            menright = nerv[1];
        }
        else if (nerv[0] == nerv[1] - 1) {
            config = ">>";

            i = 2;
            left = 2;
            menright = nerv[0];
        } else {
            verdict = "impossible";
        }

        if (verdict == "impossible") {
            outputit(verdict, config);
            return 0;
        }

        while (!certain)

        for (i; i < n; i++) {
            if (nerv[i] == menright + left) {
                config += ">";
                menright = menright;
                left += 1;
            } else if (nerv[i] == menright + left - 1) {
                config += "<";
                menright -= 1;
                left = left;
            } else {
                verdict = "impossible";
                outputit(verdict, config);
                return 0;
            }
        }

        if (menright > 0) {
            verdict = "impossible";
            outputit(verdict, config);
            return 0;
        }
        verdict = "possible";
    }

    outputit(verdict, config);

    return 0;
}
