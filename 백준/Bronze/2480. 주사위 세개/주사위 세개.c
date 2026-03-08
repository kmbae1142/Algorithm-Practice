#include <stdio.h>


int main() {

    int e1, e2, e3;
    scanf("%d %d %d", &e1, &e2, &e3);

    if (e1 == e2 && e2 == e3) {
        printf("%d", 10000 + e1 * 1000);
    }
    else if (e1 != e2 && e2 != e3 && e3 != e1) {
        if ((e1 > e2 && e2 > e3) || (e1 > e3 && e3 > e2))
            printf("%d", e1 * 100);
        else if ((e2 > e1 && e1 > e3) || (e2 > e3 && e3 > e1))
            printf("%d", e2 * 100);
        else if ((e3 > e1 && e1 > e2) || (e3 > e2 && e2 > e1))
            printf("%d", e3 * 100);
    }
    else if (e1 == e2 || e2 == e3 || e3 == e1) {
        if (e1 == e2)
            printf("%d", 1000 + e1 * 100);
        else if (e2 == e3)
            printf("%d", 1000 + e2 * 100);
        else if (e3 == e1)
            printf("%d", 1000 + e3 * 100);
    }


}