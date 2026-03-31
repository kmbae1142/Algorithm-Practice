#include <stdio.h>

#define swap(a, b)       \
	{			         \
		double temp = a; \
		a = b;           \
		b = temp;        \
	}

int main() {

	int N;
	double matrix[6][7];
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N + 1; j++) {
			scanf("%lf", &matrix[i][j]);
		}
	}

	for (int i = 0; i < N; i++) {
		if (matrix[i][i] == 0) {
			int j = i + 1;
			while (matrix[j][i] == 0) j++;
			for (int k = 0; k < N + 1; k++) swap(matrix[i][k], matrix[j][k]);
		}
        
		double p = matrix[i][i];
		for (int j = i; j < N + 1; j++) matrix[i][j] /= p;

		for (int row = i + 1; row < N; row++) {
			p = matrix[row][i];
			for (int col = 0; col < N + 1; col++) {
				matrix[row][col] -= (matrix[i][col] * p);
			}
		}
	}

	double ans[6]; ans[N - 1] = matrix[N - 1][N];

	for (int row = N - 2; row >= 0; row--) {
		double sum = 0;
		for (int col = N - 1; col >= row + 1; col--) {
			sum += matrix[row][col] * ans[col];
		}
		ans[row] = matrix[row][N] - sum;
	}

	for (int i = 0; i < N; i++) printf("%.0lf ", ans[i]);

}