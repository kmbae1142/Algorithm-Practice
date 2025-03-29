#include <stdio.h>

int main() {

	int N, x, y;
	int max_x = -10001, min_x = 10001;
	int max_y = -10001, min_y = 10001;
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%d %d", &x, &y);
		if (max_x < x) max_x = x;
		if (min_x > x) min_x = x;
		if (max_y < y) max_y = y;
		if (min_y > y) min_y = y;
	}

	printf("%d", (max_x - min_x) * (max_y - min_y));

}