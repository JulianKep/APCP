#include <bits/stdc++.h>
#include <vector>
using namespace std;


int first_number = 0;

std::vector<int> test_cases(2);


int main(){

    freopen("data/25_F/sample-1.in", "r", stdin);

    scanf("%d", &first_number);

    for (int i = 0; i < first_number; i++) {
        std::vector<int> test_case(2);
        scanf("%d %d", &test_case[0], &test_case[1]);
    }

    printf("%d\n", test_cases[1]);

  return 0;

}