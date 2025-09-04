#include <stdio.h>

#define MAX 1 << 20

char buf[MAX];
int len, p;

static inline char read_char() {
    if (p == len) {
        len = fread(buf, 1, MAX, stdin);
        p = 0;
    }
    return buf[p++];
}

static inline void read_int(int* n) {
    int ch;
    *n = read_char() - '0';

    while ((ch = read_char()) != '\n') {
        *n = (*n) * 10 + (ch - '0');
    }
}

int main() {

    int N, num;
    long long sum = 0;

    read_int(&N);
    for (int i = 0; i < N; i++) {
        read_int(&num);
        sum += num;
    }

    printf("%d\n%lld", N, sum);
    return 0;
    
}