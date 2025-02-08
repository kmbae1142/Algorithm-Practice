#include <stdio.h>

int main() {

	int n, count = 0, error = 0;
	int temp = 0;
	int num[30], from[30];
	int check[30] = { 0, };
	int input[30];
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &num[i]);
	}

	from[0] = 0;
	check[0] = 1;
	for (int i = 1; i < n; i++) {
		from[i] = (from[i - 1] + num[i - 1]) % n;
		if (check[from[i]] == 1) {
			while (check[from[i]] != 0) {
				from[i] = (from[i] + 1) % n;
			}
			check[from[i]] = 1;
		}
		else {
			check[from[i]] = 1;
		}
	}

	for (int i = 0; i < n; i++) {
		if (check[i] == 0) {
			error = 1;
		}
	}

	if (error) {
		printf("-1");
	}
	else {
		while (count < n) {
			input[from[count]] = num[count];
			count++;
		}

		printf("%d\n", n);
		for (int i = 0; i < n; i++) {
			printf("%d ", input[i]);
		}
	}

}