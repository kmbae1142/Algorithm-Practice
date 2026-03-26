#include <iostream>
#include <string>

using namespace std;

int main() {
	string p;
	cin >> p;

	string temp = "";
	int rank = 0;
	for (auto i : p) {
		if (i == 'x') {
			if (temp == "") rank = 1;
			else if (temp == "-") rank = -1;
			else rank = stoi(temp);
			temp = "";
			break;
		}
		if ((i >= '0' && i <= '9') || (i == '+' || i == '-')) temp += i;
	}

	if (temp != "") {
		cout << "0";
	}
	else {
		cout << rank;
	}
	
	return 0;
}