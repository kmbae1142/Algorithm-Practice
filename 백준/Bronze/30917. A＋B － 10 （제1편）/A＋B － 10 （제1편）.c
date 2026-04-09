#include <stdio.h>
int main() {
    int resp;
    for (int a = 1; a <= 9; a++) {
        printf("? A %d\n", a);
        fflush(stdout);

        scanf("%d", &resp);

        if (resp == 1) {
            int b = 1;
            for (; b <= 9; b++) {
                printf("? B %d\n", b);
                fflush(stdout);
                scanf("%d", &resp);

                if (resp == 1) break;
            }
            printf("! %d", a + b);
            break;
        }
    }
}