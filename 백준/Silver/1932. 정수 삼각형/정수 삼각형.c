#include <stdio.h>
#define max(a, b) ((a) > (b) ? (a) : (b))

int dp[500][500];

int main() {
	
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) {
			scanf("%d", &dp[i][j]);
		}
	}

	for (int i = 1; i < n; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0) {
				dp[i][j] = dp[i][j] + dp[i - 1][j];
			}
			else if (i == j) {
				dp[i][j] = dp[i][j] + dp[i - 1][j - 1];
			}
			else {
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + dp[i][j];
			}
		}
	}

	int result = dp[n - 1][0];
	for (int j = 0; j < n; j++) {
		if (result < dp[n - 1][j]) {
			result = dp[n - 1][j];
		}
	}

	printf("%d", result);
	return 0;

}