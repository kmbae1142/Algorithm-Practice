#include <stdio.h>
#include <string.h>

int main() {

	char str[3][10] = { 0, };
	int num[3] = { 0, };
	
	for (int i = 0; i < 3; i++) {
		scanf("%s", str[i]);
		if (strcmp(str[i], "Fizz") &&
			strcmp(str[i], "Buzz") &&
			strcmp(str[i], "FizzBuzz")) {
			num[i] = atoi(str[i]);
		}
	}

	if (num[0]) num[2] = num[0] + 2;
	if (num[1]) num[2] = num[1] + 1;

	int next = num[2] + 1;

	if (next % 3 == 0 && next % 5 == 0) printf("FizzBuzz");
	else if (next % 3 == 0 && next % 5 != 0) printf("Fizz");
	else if (next % 3 != 0 && next % 5 == 0) printf("Buzz");
	else printf("%d", next);

	return 0;

}