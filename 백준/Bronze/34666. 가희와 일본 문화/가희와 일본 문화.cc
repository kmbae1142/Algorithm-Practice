#include <iostream>

using namespace std;

int main() {
	cin.tie(NULL), cout.tie(NULL), ios::sync_with_stdio(0);
	int Q;
	int G, J, R, L;
	int sc[5] = { 100, 90, 95, 90, 80 };

	cin >> Q;
	while (Q--)
	{
		cin >> G >> J >> R >> L;
		if (G < 3) {
			if (L >= 50) {
				int c1 = J * 3 < sc[G - 1] ? 1 : 0;
				int c2 = R * 3 < sc[G - 1] ? 1 : 0;
				int confirm1 = c1 & c2;
				int confirm2 = (J < 22) || (R < 22) || (L < 22);
				if (confirm1 || confirm2) {
					cout << "YES\n";
				}
				else {
					cout << "NO\n";
				}
			}
			else {
				cout << "NO\n";
			}
		}
		else {
			cout << "NO\n";
		}
	}
}