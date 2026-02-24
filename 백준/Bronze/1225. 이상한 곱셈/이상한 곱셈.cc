#include <iostream>
#include <string>

using namespace std;

int main() {
	string a, b;
	cin >> a >> b;
	long long sum = 0;

	for (auto i : a) {
		for (auto j : b) {
			sum += (long long)((i - '0') * (j - '0'));
		}
	}

	cout << sum;
	return 0;
}