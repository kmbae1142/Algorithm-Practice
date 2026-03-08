#include <stdio.h>

int smallest(int a[], int n) {

    int i, min = a[0];
    for (i = 1; i < n; i++) {
        if (min > a[i])
            min = a[i];
    }
    return min;
}

int main() {

    int x, y, w, h;
    int len[4];
    scanf("%d %d %d %d", &x, &y, &w, &h);

    len[0] = x;
    len[1] = w - x;
    len[2] = y;
    len[3] = h - y;

    printf("%d", smallest(len, 4));

}