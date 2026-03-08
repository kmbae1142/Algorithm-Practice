#include <stdio.h>

int main() {

    int t, i;
    int num1, num2;

    scanf("%d\n", &t);

    for (i = 0; i < t; ++i) {
        scanf("%d %d\n", &num1, &num2);
        printf("Case #%d: %d + %d = %d\n", i + 1, num1, num2, num1 + num2);
    }

    
    return 0;

}