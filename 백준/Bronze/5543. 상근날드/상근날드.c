#include <stdio.h>

int smallest(int a[], int i) {

    int j, min = a[0];
    

    for (j = 1; j < i; j++) {
        if (a[j] < min)
            min = a[j];
    }
    return min;

}



int main() {

    
    int burger[3];
    int drink[2];
    int price_smallest_burger = 0, price_smallest_drink = 0;

    for (int i = 0; i < 3; i++) {
        scanf("%d", &burger[i]);
    }
    for (int i = 0; i < 2; i++) {
        scanf("%d", &drink[i]);
    }

    price_smallest_burger = smallest(burger, 3);
    price_smallest_drink = smallest(drink, 2);

    printf("%d", price_smallest_burger + price_smallest_drink - 50);


}