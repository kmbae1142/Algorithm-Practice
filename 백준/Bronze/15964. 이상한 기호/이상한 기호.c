#include <stdio.h>


int main() {

    
    long long a, b;
    long long new;
    scanf("%lld %lld", &a, &b);

    new = a * a - b * b;
    
    printf("%lld", new);

}