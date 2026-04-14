#include <stdio.h>

int main() {
	
	int house[15][14];
	int sum[15][14] = { 1, };

	for (int i = 0; i < 14; i++) house[0][i] = i + 1;
	for (int i = 1; i < 14; i++) sum[0][i] = house[0][i] + sum[0][i - 1];

	for (int i = 1; i < 15; i++) {
		for (int j = 0; j < 14; j++) 
			house[i][j] = sum[i - 1][j];
		
		sum[i][0] = house[i][0];
		for (int j = 1; j < 14; j++) 
			sum[i][j] = house[i][j] + sum[i][j - 1];
	}

	int T;
	scanf("%d", &T);

	while (T--) {
		int k, n;
		scanf("%d\n%d", &k, &n);
		printf("%d\n", house[k][n - 1]);
	}

	return 0;
    
}