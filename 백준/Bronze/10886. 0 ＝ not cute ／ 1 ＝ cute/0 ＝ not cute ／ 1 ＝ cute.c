#include <stdio.h>


int main() {

    int num, num2;
    int agree = 0, disagr = 0;
    
    scanf("%d", &num);
    
    for (int i = 0; i < num; i++) {
        scanf("%d", &num2);
        if (num2 == 0) 
            disagr++;
        else
            agree++;
    }
    
    if (disagr > agree) {
        printf("Junhee is not cute!");
    }else {
        printf("Junhee is cute!");
    }

}