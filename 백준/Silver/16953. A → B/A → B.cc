#include <iostream>

using namespace std;

int main() {

	int A, B, err = 0, cnt = 0;
	cin >> A >> B;

	while (B > A) {
		if (B % 10 == 1) {
			B /= 10;
		}
		else if (B % 2 == 0) {
			B /= 2;
		}
		else {
			break;
		}
		cnt++;
	}

	if (B == A) cout << cnt + 1;
	else cout << -1;

}