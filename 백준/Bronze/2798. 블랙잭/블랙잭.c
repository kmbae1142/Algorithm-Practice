#include <stdio.h>

int main() {

    int N, M;
    int i, j, k;
    int max = 0;
    scanf("%d %d", &N, &M);
    int num[N];

    for (i = 0; i < N; i++) {
        scanf("%d ", &num[i]);
    }

    for (i = 0; i < N - 2; i++) {
        for (j = i+1; j < N - 1; j++) {
            for (k = j+1; k < N; k++) {
                if (num[i] + num[j] + num[k] <= M) {
                    if (max < num[i] + num[j] + num[k]) {
                        max = num[i] + num[j] + num[k];
                    }
                }
            }
        }
    }

    printf("%d", max);

}