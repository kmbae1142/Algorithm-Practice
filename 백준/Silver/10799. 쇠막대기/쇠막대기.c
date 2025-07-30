#include <stdio.h>
#include <string.h>

char str[100002];

int main() {

	int left = 0, ans = 0;
	scanf("%s", str);
	for (int i = 0; str[i] != '\0'; i++) {
		if (str[i] == '(') left++;

		else {
			left--;
			if (str[i - 1] == '(') ans += left;
			else ans++;
		}
	}

	printf("%d", ans);

}