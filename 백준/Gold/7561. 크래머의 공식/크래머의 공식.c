#include <stdio.h>

// Determinant of Cofator Matrix
long long CDet(int (*A)[3], int num) {
	if (num == 1) {
		return A[1][1] * A[2][2] - A[1][2] * A[2][1];
	}
	else if (num == 2) {
		return A[1][0] * A[2][2] - A[1][2] * A[2][0];
	}
	else {
		return A[1][0] * A[2][1] - A[1][1] * A[2][0];
	}
}

long long det(int (*A)[3]) {
	return A[0][0] * CDet(A, 1) - A[0][1] * CDet(A, 2) + A[0][2] * CDet(A, 3);
}

int main() {

	int T, i, j;
	scanf("%d", &T);

	while (T--) {

		int A[3][3] = { 0, };
		int A1[3][3], A2[3][3], A3[3][3];
		int b[3];

		for (i = 0; i < 3; i++) {
			for (j = 0; j < 3; j++) {
				scanf("%d", &A[i][j]);
				A1[i][j] = A[i][j];
				A2[i][j] = A[i][j];
				A3[i][j] = A[i][j];
			}
			scanf("%d", &b[i]);
		}

		for (int i = 0; i < 3; i++) {
			A1[i][0] = b[i];
			A2[i][1] = b[i];
			A3[i][2] = b[i];
		}

		long long detA = det(A), detA1 = det(A1), detA2 = det(A2), detA3 = det(A3);
		printf("%lld %lld %lld %lld\n", detA1, detA2, detA3, detA);

		if (detA != 0) {

			double x1 = (double)detA1 / detA;
			double x2 = (double)detA2 / detA;
			double x3 = (double)detA3 / detA;

			if (-0.0005 < x1 && x1 < 0.0005) x1 = 0.0;
			if (-0.0005 < x2 && x2 < 0.0005) x2 = 0.0;
			if (-0.0005 < x3 && x3 < 0.0005) x3 = 0.0;

			printf("Unique solution: %.3lf %.3lf %.3lf\n", x1, x2, x3);
		}

		else {
			printf("No unique solution\n");
		}

		printf("\n");

	}

}