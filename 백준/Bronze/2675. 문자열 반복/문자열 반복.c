#include <stdio.h>
#include <string.h>

int main() {

    int num, test_c;
    char str1[21] = "";

    scanf("%d", &test_c);;

    for (int i = 0; i < test_c; i++) {
        scanf("%d %s", &num, str1);


        for (int j = 0; j < strlen(str1); j++) {
            for (int k = 0; k < num; k++) {
                printf("%c", str1[j]);
            }
        }
        printf("\n");  
    }

}