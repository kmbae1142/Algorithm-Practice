#include <stdio.h>

int main() {

	int N, B, i = 0;
	char result[30];
	scanf("%d %d", &N, &B);

	while (N > 0) {
		if (N % B >= 10) result[i++] = (N % B - 10) + 'A';
		else result[i++] = N % B + '0';
		N /= B;
	}

	for (int n = i - 1; n >= 0; n--) {
		printf("%c", result[n]);
	}
    
}