#include <stdio.h>

int main() {
    int score;

    scanf("%d",&score);

    if (100>=score && score>=90)
        printf("A\n"); 
    else if(89>=score && score>=80)
        printf("B\n"); 
    else if(79>=score && score>=70)
        printf("C\n");
    else if(69>=score && score>=60)
        printf("D\n");
    else
        printf("F\n");
    
    
    
    return 0;
}