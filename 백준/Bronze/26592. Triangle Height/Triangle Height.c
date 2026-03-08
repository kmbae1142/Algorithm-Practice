#include <stdio.h>

int main() {

	int N;
	double a, b;
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%lf %lf", &a, &b);
		printf("The height of the triangle is %.2lf units\n", 2 * a / b);
	}

}