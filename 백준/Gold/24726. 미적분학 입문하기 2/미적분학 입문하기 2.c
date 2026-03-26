#include <stdio.h>
#include <stdlib.h>

int main() {
	
	int x1, y1, x2, y2, x3, y3;
	scanf("%d %d %d %d %d %d", &x1, &y1, &x2, &y2, &x3, &y3);

	double r_x = (double)(x1 + x2 + x3) / 3;
	double r_y = (double)(y1 + y2 + y3) / 3;
	double A = 0.5 * abs(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3);
	double pi = 3.14159265358979;
	
	printf("%.9f %.9f", 2 * pi * r_y * A, 2 * pi * r_x * A);
	return 0;

}