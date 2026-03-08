#include <stdio.h>

int largest(int a[], int n) {

    int i, max = a[0];

    for (i = 1; i < n; i++) {
        if (a[i] > max)
            max = a[i];
    }

    return max;
}

int main() {
    
    int num[10] = {0};
    int max;
    int sc;
    
    for (int i = 0; i < 9; i++) {
        scanf("%d\n", &num[i]);
    }
    max = largest(num, 10);
    for (int i = 0; i < 9; i++) {
        if(num[i] == max) {
            sc = i + 1;
        }
    }
    
    printf("%d\n", max);
    printf("%d", sc);

    return 0;
}