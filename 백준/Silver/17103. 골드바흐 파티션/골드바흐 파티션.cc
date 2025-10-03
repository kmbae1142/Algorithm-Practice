#include <iostream>
#define LEN 1000001

using namespace std;

int main() {

	cin.tie(NULL), cout.tie(NULL), ios::sync_with_stdio(0);
	bool* primes = new bool[LEN];
	fill(primes, primes + LEN, true);
	primes[1] = false;
	primes[2] = true;

	for (int i = 2; i * i < LEN; i++) {
		if (!primes[i]) continue;
		for (int j = i * i; j < LEN; j += i) {
			primes[j] = false;
		}
	}

	int T;
	cin >> T;

	while (T--) {
		int N, cnt = 0;
		cin >> N;

		for (int i = 2; i <= N; i++) {
			if (primes[i] && primes[N - i]) {
				cnt++;
			}
		}

		if (primes[N / 2]) cnt = cnt / 2 + 1;
		else cnt /= 2;

		cout << cnt << '\n';
	}

	return 0;

}