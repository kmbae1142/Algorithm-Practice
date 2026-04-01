#include <stdio.h>

int main() {
	long long R, r;
	scanf("%lld %lld", &R, &r);

	printf("%lld", R * R - 2 * R * r);
	return 0;
}