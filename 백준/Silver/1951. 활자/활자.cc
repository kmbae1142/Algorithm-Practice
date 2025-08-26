#include <bits/stdc++.h>

using namespace std;

int main() {
    
    string num;
    long long result = 0;
    cin >> num;
    int len = num.length();

    if (len <= 1) {
        cout << num << '\n';
    }
    else {
        result += (pow(10, len - 1) * (9 * (len - 1) - 1) + 1) / 9;
        result += len * (stoi(num) - pow(10, len - 1) + 1);
        cout << result % 1234567;
    }
    
    return 0;
    
}