#include <stdio.h>

int main() {
    
    int num[101] = {0};
    int i, num2, result = 0;
    
    scanf("%d\n", &i);
    
    for (int j = 0; j < i; j++) {
        scanf("%d ", &num[j]);
    }
    
    scanf("%d\n", &num2);
    
    for (int k = 0; k < i; k++) {
        if (num[k] == num2) {
            result++;
        }
    }
    
    printf("%d\n", result);
    return 0;
}