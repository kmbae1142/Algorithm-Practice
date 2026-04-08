#include <stdio.h>

int main() {
	int a, b, c, d;
	scanf("%d\n%d\n%d\n%d", &a, &b, &c, &d);
	char* ans = (a + b + c + d) <= 1500 ? "Yes" : "No";
	puts(ans);
	return 0;
}