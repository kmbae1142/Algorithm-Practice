#include <stdio.h>
#include <string.h>


int main() {

    int num;
    char str[1002] = {0};
    scanf("%d", &num);

    for (int i = 0; i < num; i++) {
        scanf("%s", str);
        printf("%c%c\n", str[0], str[strlen(str) - 1]);
    }

    return 0;

}