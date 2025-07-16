#include <iostream>
#include <string>

using namespace std;

int main() {

	ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	string str;

	cin >> str;

	for (auto &c : str) {
		if (isupper(c)) c = tolower(c);
		else c = toupper(c);
	}

	cout << str << '\n';

	return 0;

}