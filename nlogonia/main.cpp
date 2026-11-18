#include <bits/stdc++.h>
using namespace std;

int main() {
    int num_examples = 0;
    while (cin >> num_examples) {
/*         int num_examples;
        cin >> num_examples; */

        if (num_examples == 0)
            break;

        int cx, cy;
        cin >> cx >> cy;

        for (int i = 0; i < num_examples; i++) {
            int x, y;
            cin >> x >> y;

            if (x > cx && y > cy)
                cout << "NE\n";
            else if (x > cx && y < cy)
                cout << "SE\n";
            else if (x < cx && y > cy)
                cout << "NO\n";
            else if (x < cx && y < cy)
                cout << "SO\n";
            else
                cout << "divisa\n";
        }
    }
}