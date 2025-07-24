#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int n, num, cur = 1;
	vector<int> v;
	stack<int> s;
	vector<char> result;
	cin >> n;

	while (n--) {
		cin >> num;
		v.push_back(num);
	}

	for (auto i : v) {
		while (s.empty() || s.top() < i) {
			s.push(cur++);
			result.push_back('+');
		}

		if (s.top() == i) {
			s.pop();
			result.push_back('-');
		}
		else {
			cout << "NO\n";
			return 0;
		}
	}

	for (auto i : result) {
		cout << i << '\n';
	}

	return 0;

}