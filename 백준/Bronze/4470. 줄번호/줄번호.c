#include <stdio.h>
#include <string.h>

void Clear(void) {
    while (getchar() != '\n');
}

int main() {

    int num, i;
    char str[52];

    scanf("%d", &num);
    Clear();
    
    for (i = 1; i <= num; i++) {
        fgets(str, sizeof(str), stdin);
        printf("%d. %s", i, str);
    }


}