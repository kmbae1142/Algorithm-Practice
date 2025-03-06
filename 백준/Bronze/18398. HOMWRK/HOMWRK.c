#include <stdio.h>

int main() {
	
	int T, n, a, b;
	scanf("%d", &T);

	while (T--) {
		scanf("%d", &n);
		while (n--) {
			scanf("%d %d", &a, &b);
			printf("%d %d\n", a + b, a * b);
		}
	}
}