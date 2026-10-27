#include <bits/stdc++.h>
using namespace std;


int num_test_cases = 0;

struct cat{
    int should_go_to;
    int num_pots;
    vector<int> pots;
};

struct test_case {
    int num_cats;
    int num_pots; 
    vector<cat> cats;
};


int main(){

    freopen("data/25_F/sample-1.in", "r", stdin);
    scanf("%d", &num_test_cases);

    vector<test_case> tca(num_test_cases);


    for(int tc = 0; tc < num_test_cases; tc++){

        scanf("%d %d", &tca[tc].num_cats, &tca[tc].num_pots);


        //loop over cats
        for(int c = 0; c < tca[tc].num_cats; c++){

            int should_go = 0;
            int num_pots = 0;
            vector<int> pots;

            scanf("%d %d", &should_go, &num_pots);

            for(int pot = 0; pot < num_pots; pot++){
                int cur_p = 0;
                scanf("%d", &cur_p);
                
            }

            tca[tc].cats.push_back(cat{should_go, num_pots, pots});
        }
    }

    printf("%d\n", tca[1].cats[1].should_go_to);

  return 0;

}