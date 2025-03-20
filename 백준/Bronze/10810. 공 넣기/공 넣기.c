#include <stdio.h>

int main() {

    int N, M, i, j, k;
    int arr[100] = { 0, };
    scanf("%d %d", &N, &M);

    while (M--) {
        scanf("%d %d %d", &i, &j, &k);
        for (; i <= j; i++) {
            arr[i - 1] = k;
        }
    }

    for (int i = 0; i < N; i++) {
        printf("%d ", arr[i]);
    }

}