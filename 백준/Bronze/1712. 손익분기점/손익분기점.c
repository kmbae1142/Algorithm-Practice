#include <stdio.h>

int main() {
	int A, B, C;
	scanf("%d %d %d", &A, &B, &C);

	if (B >= C) printf("-1");
	else printf("%d", (int)((double)A / (C - B) + 1));

	return 0;
}