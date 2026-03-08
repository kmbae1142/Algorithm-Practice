#include <stdio.h>


int main() {

    int n, i, j;
    int prime_num = 0;
    scanf("%d", &n);
    int numbers[n];

    for (i = 0; i < n; i++) {
        scanf("%d ", &numbers[i]);
    }

    for (i = 0; i < n; i++) {
        for (j = 2; j < numbers[i]; j++) {
            if (numbers[i] % j == 0)
                break;
        }
        if (numbers[i] == j)
            prime_num++;
    }

    printf("%d", prime_num);

}