#include <stdio.h>


int main() {
    
    char str[101] = {0};
    int i = 0;
    
    scanf("%s", &str);
    
    while (str[i] != '\0') {
        i++;
    }
    printf("%d", i);
    
}