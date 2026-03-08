#include <stdio.h>


int main() {

    int score[5];
    int sum = 0, average;;
    
    for (int i = 0; i < 5; i++) {
        scanf("%d", &score[i]);
        if (score[i] < 40) {
            score[i] = 40;
        }
    }
    
    for (int i = 0; i < 5; i++) {
        sum += score[i];
    }
    
    average = sum / 5;
    printf("%d", average);

}