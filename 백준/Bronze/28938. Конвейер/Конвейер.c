#include <stdio.h>

int main() {
    int num, sum = 0;
    scanf("%d", &num);
    int arr[num];
    
    for (int i = 0; i < num; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    
    if (sum > 0)
        printf("Right");
    else if (sum == 0)
        printf("Stay");
    else
        printf("Left");
    
    
}