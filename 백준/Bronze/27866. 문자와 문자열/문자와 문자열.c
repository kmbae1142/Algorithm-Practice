#include <stdio.h>


int main() {
    
    char str[1001] = {0};
    int i;
    
    scanf("%s", &str);
    scanf("%d", &i);
    
    printf("%c", str[i - 1]);
    
}