#include <iostream>

using namespace std;

int main() {
	int N, sum = 0;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int C, K;
		cin >> C >> K;
		sum += C * K;
	}

	cout << sum;
	return 0;
}