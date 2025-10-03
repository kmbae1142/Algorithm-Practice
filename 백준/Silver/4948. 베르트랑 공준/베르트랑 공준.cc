#include <iostream>
#define LEN 246913

using namespace std;

int main() {
    
    cin.tie(NULL), cout.tie(NULL); ios::sync_with_stdio(0);
	int n;
	bool* primes = new bool[LEN];
	fill(primes, primes + LEN, true);
	primes[2] = true;

	for (int i = 2; i * i < LEN; i++) {
		if (!primes[i]) continue;
		for (int j = i * i; j < LEN; j += i) {
			primes[j] = false;
		}
	}

	while (true) {
		int cnt = 0;
		cin >> n;
		if (!n) break;

		for (int i = n + 1; i <= 2 * n; ++i) {
			if (primes[i]) cnt++;
		}
		cout << cnt << '\n';
	}
    
    return 0;

}