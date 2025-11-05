#include <stdio.h>

int arr[1024][1024];

int main() {
	
	int N, M;
	scanf("%d %d", &N, &M);

	for (int i = 0; i < N; ++i) {
		int sum = 0;
		for (int j = 0; j < N; ++j) {
			scanf("%d", &arr[i][j]);
			int temp = arr[i][j];
			arr[i][j] += sum;
			sum += temp;
		}
	}

	int x1, y1, x2, y2;
	for (int i = 0; i < M; i++) {
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		int result = 0;

		if (y1 - 2 >= 0) {
			for (int row = x1 - 1; row <= x2 - 1; row++) {
				result += arr[row][y2 - 1] - arr[row][y1 - 2];
			}
		}
		else {
			for (int row = x1 - 1; row <= x2 - 1; row++) {
				result += arr[row][y2 - 1];
			}
		}
		printf("%d\n", result);
	}

	return 0;

}