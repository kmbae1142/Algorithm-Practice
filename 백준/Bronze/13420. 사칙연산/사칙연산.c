#include <stdio.h>

int main() {
	int T;
	scanf("%d", &T);

	while (T--) {
		long long a, b, ans;
		char op, eq;
		scanf("%lld %c %lld %c %lld", &a, &op, &b, &eq, &ans);

		char* str = NULL;
		if (op == '*') {
			str = (a * b == ans) ? "correct" : "wrong answer";
		}
		else if (op == '/') {
			str = (a / b == ans) ? "correct" : "wrong answer";
		}
		else if (op == '+') {
			str = (a + b == ans) ? "correct" : "wrong answer";
		}
		else if (op == '-') {
			str = (a - b == ans) ? "correct" : "wrong answer";
		}

		puts(str);
	}
    
    return 0;
}