#include <stdio.h>

int main() {
	int people = 0, max = -1;

	for (int i = 0; i < 10; i++) {
		int out, in;
		scanf("%d %d", &out, &in);

		people += in - out;
		max = max < people ? people : max;
	}

	printf("%d", max);
	return 0;
}