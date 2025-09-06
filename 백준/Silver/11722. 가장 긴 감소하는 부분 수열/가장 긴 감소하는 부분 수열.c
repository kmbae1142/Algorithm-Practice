#include <stdio.h>

#define max(a, b) ((a) > (b)) ? (a) : (b)

int A[1000], dp[1000];

int main() {

    int N, max_len = 0;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
        int cur = 0;
        for (int j = 0; j < i; j++) {
            if (A[j] > A[i])
                cur = max(cur, dp[j]);
        }
        dp[i] = cur + 1;
        max_len = max(max_len, dp[i]);
    }

    printf("%d", max_len);
    return 0;

}