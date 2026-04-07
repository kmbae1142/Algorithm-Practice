#include <stdio.h>

int main() {

	long long x1, y1;
	long long x2, y2;
	long long x3, y3;

	scanf("%lld %lld", &x1, &y1);
	scanf("%lld %lld", &x2, &y2);
	scanf("%lld %lld", &x3, &y3);

	long long cpt = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1);

	if (cpt == 0) {
		printf("0");
	}
	else if (cpt < 0) {
		printf("-1");
	}
	else {
		printf("1");
	}

	return 0;

}