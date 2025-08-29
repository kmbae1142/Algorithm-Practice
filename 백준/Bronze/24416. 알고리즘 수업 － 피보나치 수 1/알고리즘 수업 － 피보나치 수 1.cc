#include <bits/stdc++.h>

using namespace std;

int main() {

    int n;
    int* dp = new int[40];
    cin >> n;
    
    dp[0] = dp[1] = 1;
    for (int i = 2; i < 40; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    cout << dp[n - 1] << ' ' << n - 2;
    delete[] dp;

}