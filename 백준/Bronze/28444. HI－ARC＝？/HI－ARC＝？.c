#include <stdio.h>

int main() {

    int H, I, A, R, C;
    scanf("%d %d %d %d %d", &H, &I, &A, &R, &C);
    
    printf("%d", H * I - A * R * C);

    return 0;

}