#include <stdio.h>

void scanf_arr(int a[], int i) {

    for (int j = 0; j < i; j++) {
        scanf("%d", &a[j]);
    }

}

int main() {

    int ming[4];
    int mans[4];
    int ming_sum = 0, mans_sum = 0;

    scanf_arr(ming, 4);
    scanf_arr(mans, 4);

    for (int i = 0; i < 4; i++) {
        ming_sum += ming[i];
    }

    for (int i = 0; i < 4; i++) {
        mans_sum += mans[i];
    }

    if (ming_sum >= mans_sum) {
        printf("%d", ming_sum);
    }
    else {
        printf("%d", mans_sum);
    }

}