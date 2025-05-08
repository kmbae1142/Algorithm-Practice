#include <stdio.h>

int main() {

    int n;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        char str[52];
        scanf("%s", str);

        for (int i = 0; str[i] != '\0'; i++) {
            str[i] = ((str[i] + 1) - 65) % 26 + 65;
        }

        printf("String #%d\n", i);
        printf("%s\n", str);
        printf("\n");
    }
    

}