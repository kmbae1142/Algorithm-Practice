#include <stdio.h>

int main() {
    
    int a, b;
    
    while (1) {
        if (scanf("%d %d\n", &a, &b) == EOF)
            break;
        printf("%d\n", a + b);
    }
    
    return 0;
}