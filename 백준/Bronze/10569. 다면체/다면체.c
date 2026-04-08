#include <stdio.h>

int main() {

	int T; 
	scanf("%d", &T);

	while (T--) {
		int V, E;
		scanf("%d %d", &V, &E);
		printf("%d\n", 2 - V + E);
	}

	return 0;

}