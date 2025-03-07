#include <stdio.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);
    getchar();
    
    for (int i = 0; i < n; i++) {
        char str[1024];
        fgets(str, sizeof(str), stdin);
        
        str[strlen(str) - 1] = '\0';
        
        int len = strlen(str);
        if (len == 0 || str[len - 1] != '.') {
            printf("%s.\n", str);
        } 
        else {
            printf("%s\n", str);
        }
    }
    return 0;
}
