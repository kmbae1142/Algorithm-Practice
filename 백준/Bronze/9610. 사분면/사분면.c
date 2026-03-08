#include <stdio.h>

int main() {
    
	int a, b;
    int q1 = 0, q2 = 0, q3 = 0, q4 = 0, axis = 0;
    int i = 0, j = 0, num;
    scanf("%d", &num);
    int arr[num * 2];
    
    while (i < num) {
        scanf("%d %d", &arr[j], &arr[j + 1]);
        j += 2;
        i++;
    }
    
    i = 0;
    j = 0;
    
    while (i < num) {
        if (arr[j] == 0 || arr[j + 1] == 0)
            axis++;
        else if (arr[j] > 0 && arr[j + 1] > 0)
            q1++;
        else if (arr[j] < 0 && arr[j + 1] > 0)
            q2++;
        else if (arr[j] < 0 && arr[j + 1] < 0)
            q3++;
        else if (arr[j] > 0 && arr[j + 1] < 0)
            q4++;
             
        j += 2;
        i++;
    }
    
    printf("Q1: %d\n", q1);
    printf("Q2: %d\n", q2);
    printf("Q3: %d\n", q3);
    printf("Q4: %d\n", q4);
    printf("AXIS: %d\n", axis);
    
}