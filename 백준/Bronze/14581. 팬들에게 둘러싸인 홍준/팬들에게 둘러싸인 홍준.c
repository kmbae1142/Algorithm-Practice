#include <stdio.h>
#include <string.h>


int main() {

    char str[22];

    fgets(str, sizeof(str), stdin);
    str[strlen(str) - 1] = '\0';
    
    printf(":fan::fan::fan:\n");  
    printf(":fan::%s::fan:\n", str);
    printf(":fan::fan::fan:");

}