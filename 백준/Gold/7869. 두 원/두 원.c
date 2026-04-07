#include <stdio.h>
#include <math.h>

int main() {

	double x1, y1, r1, x2, y2, r2;
	double pi = 3.141592653589793;
	scanf("%lf %lf %lf %lf %lf %lf", &x1, &y1, &r1, &x2, &y2, &r2);

	double d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));

	if (d >= (r1 + r2)) {
		printf("0.000");
	}
	else if (d > fabs(r1 - r2) && d < r1 + r2) {
		double theta1 = 2 * acos((r1 * r1 + d * d - r2 * r2) / (2 * r1 * d));
		double theta2 = 2 * acos((r2 * r2 + d * d - r1 * r1) / (2 * r2 * d));

		double area1 = 0.5 * r1 * r1 * (theta1 - sin(theta1));
		double area2 = 0.5 * r2 * r2 * (theta2 - sin(theta2));

		printf("%.3lf", area1 + area2);
	}
	else {
		double r = (r1 > r2) ? r2 : r1;
		printf("%.3lf", pi * r * r);
	}

	return 0;

}