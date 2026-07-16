#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        int offset = 1;
        for (int i = 1; i <= n; i++) {
            cout << i + offset << " ";
            offset *= -1;
        }

        cout << endl;
    }

    return 0;
}
