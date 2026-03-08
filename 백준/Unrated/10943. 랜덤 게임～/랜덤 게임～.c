#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main () {
    int num[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    srand((unsigned int)time(NULL));
    printf("%d\n", num[rand()%10]);
    return 0;
}