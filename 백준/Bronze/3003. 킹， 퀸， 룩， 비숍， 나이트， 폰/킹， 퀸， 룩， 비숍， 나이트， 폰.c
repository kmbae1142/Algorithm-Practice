#include <stdio.h>


int main() {

    int chess[6];
    int chess_standard[6] = {1, 1, 2, 2, 2, 8};
    int result[6];
    for (int i = 0; i < 6; i++) {
        scanf("%d ", &chess[i]);
    }

    for (int i = 0; i < 6; i++) {
        result[i] = chess_standard[i] - chess[i];
    }

    for (int i = 0; i < 6; i++) {
        printf("%d ", result[i]);
    }

}
