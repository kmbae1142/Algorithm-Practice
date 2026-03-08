#include <stdio.h>
#include <string.h>


int main() {

    int num, num2;
    char str[1002] = {0};
    char str2[1002] = {0};

    scanf("%s", str);
    scanf("%s", str2);

    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == 'h') {
            num = i;
        }
    }

    for (int i = 0; i < strlen(str2); i++) {
        if (str2[i] == 'h') {
            num2 = i;
        }
    }

    if (num < num2)
        printf("no");
    else
        printf("go");

    return 0;

}