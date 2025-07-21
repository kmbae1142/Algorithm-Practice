#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct cmp {
	bool operator()(int a, int b) {
		if (abs(a) > abs(b)) return true;
		else if (abs(a) == abs(b)) {
			if (a > b) return true;
			else return false;
		}
		return false;
	}
};

int main() {

	ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	priority_queue<int, vector<int>, cmp> q;
	int n, x;

	cin >> n;
	while (n--) {
		cin >> x;
		if (!x) {
			if (q.empty())
				cout << "0" << '\n';
			else {
				cout << q.top() << '\n';
				q.pop();
			}
		}
		else {
			q.push(x);
		}
	}

	return 0;

}