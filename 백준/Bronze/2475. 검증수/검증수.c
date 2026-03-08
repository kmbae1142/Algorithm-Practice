#include <stdio.h>
#include <math.h>

int main() {

    int a1, a2, a3, a4, a5;
    int result;
    scanf("%d %d %d %d %d", &a1, &a2, &a3, &a4, &a5);

    result = (int)(pow(a1, 2) + pow(a2, 2) + pow(a3, 2) + pow(a4, 2) + pow(a5, 2)) % 10;

    printf("%d", result);
}