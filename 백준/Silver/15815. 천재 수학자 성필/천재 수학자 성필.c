#include <stdio.h>
#define SIZE 100

typedef struct stack {
    int num[SIZE];
    int top;
}Stack;

void init_stack(Stack* s) {
    s->top = -1;
}

void push(Stack* s, char n) {
    s->num[++s->top] = n;
}

int main() {

    Stack s;
    init_stack(&s);
    int ch;

    while ((ch = getchar()) != '\n') {
        if (ch == '*') {
            s.num[--s.top] = s.num[s.top - 1] * s.num[s.top];
        }
        else if (ch == '/') {
            s.num[--s.top] = s.num[s.top - 1] / s.num[s.top];
        }
        else if (ch == '+') {
            s.num[--s.top] = s.num[s.top - 1] + s.num[s.top];
        }
        else if (ch == '-') {
            s.num[--s.top] = s.num[s.top - 1] - s.num[s.top];
        }
        else {
            ch -= '0';
            push(&s, ch);
        }
    }
    
    printf("%d", s.num[0]);
    
}