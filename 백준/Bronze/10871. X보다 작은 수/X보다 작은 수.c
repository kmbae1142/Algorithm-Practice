#include <stdio.h>
#include <stdlib.h> 

int main() {

    int N, num;
    int size1;
    scanf("%d %d", &N, &num);

    size1 = N;

    int* arr_num = (int*)malloc(sizeof(int) * size1);
    int* num_small = (int*)malloc(sizeof(int) * size1);

    for (int i = 0; i < size1; i++) {
        num_small[i] = 0;
    }

    for (int i = 0; i < size1; i++) {
        scanf("%d ", &arr_num[i]);
        if (arr_num[i] < num) {
            num_small[i] = arr_num[i];
        }
    }

    for (int i = 0; i < N; i++) {
        if (num_small[i] == 0) {
            continue;
        }
        else {
            printf("%d ", num_small[i]);
        }
    }

    free(arr_num);
    free(num_small);

    return 0;
}