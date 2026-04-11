#include <iostream>

using namespace std;

int main() {
	int N;
	int tshirts[6];
	int T, P;
	int a1 = 0, a2 = 0, a3 = 0;

	cin >> N;
	for (int i = 0; i < 6; i++) cin >> tshirts[i];
	cin >> T >> P;

	for (int i = 0; i < 6; i++) {
		if (tshirts[i] % T) a1 += tshirts[i] / T + 1;
		else a1 += tshirts[i] / T;
	}

	a2 = N / P;
	a3 = N % P;

	cout << a1 << '\n' << a2 << ' ' << a3;
}