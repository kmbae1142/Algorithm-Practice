#include <iostream>
#include <vector>

#define max(a, b) (((a) > (b)) ? (a) : (b))

using namespace std;

int main() {

	string s1, s2;
	cin >> s1 >> s2;
	size_t len1 = s1.length();
	size_t len2 = s2.length();

	vector<vector<int>> lcs(len1 + 1, vector<int>(len2 + 1));

	for (size_t i = 1; i <= len1; i++) {
		for (size_t j = 1; j <= len2; j++) {
			if (s1[i - 1] == s2[j - 1]) {
				lcs[i][j] = lcs[i - 1][j - 1] + 1;
			}
			else {
				lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1]);
			}
		}
	}

	cout << lcs[len1][len2];
    return 0;

}