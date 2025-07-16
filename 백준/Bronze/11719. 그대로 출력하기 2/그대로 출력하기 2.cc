#include <iostream>
#include <string>

using namespace std;

int main() {

	ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	string str;

	while (getline(cin, str)) {
		cout << str << "\n";
	}

	return 0;

}