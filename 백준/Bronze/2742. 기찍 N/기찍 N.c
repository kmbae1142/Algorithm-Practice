#include <stdio.h>


int main() {
    
    int num;
    int sub;
    scanf("%d", &num);
    
    sub = num;
    
    for (int i = 0; i < num; i++) {
        printf("%d\n", sub);
        sub--;
    }
    
    return 0;
}