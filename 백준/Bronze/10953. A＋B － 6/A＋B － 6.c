#include <stdio.h>


int main() {
    
    int a, b;
    int i;
    
    scanf("%d", &i);
    
    for (int j = 0; j < i; j++) {
        scanf("%d,%d\n", &a, &b);
        printf("%d\n", a + b);
    }
    
    return 0;
}