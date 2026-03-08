#include <stdio.h>

int main() {
    int num, even = 0, odd = 0;
    scanf("%d", &num);
    int nums[num];
    
    for (int i = 0; i < num; i++) {
        scanf("%d ", &nums[i]);
    }
    for (int i = 0; i < num; i++) {
        if (nums[i] % 2 == 0) {
            even++;
        }
        else {
            odd++;
        }
    }
    
    if (even > odd)
        printf("Happy");
    else
        printf("Sad");
    
    
}