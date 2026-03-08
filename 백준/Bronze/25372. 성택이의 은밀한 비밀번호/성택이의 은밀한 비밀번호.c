#include <stdio.h>
#include <string.h>

int main() {

    char str[22] = { 0 };
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%s", str);
        if (strlen(str) > 5 && strlen(str) < 10)
            printf("yes\n");
        else
            printf("no\n");
    }


}