#include <stdio.h>
#define SIZE 55

typedef struct stack {
    char num[SIZE];
    int top;
}Stack;

void init_stack(Stack* s) {
    s->top = -1;
}

void push(Stack* s, char n) {
    s->num[++s->top] = n;
}

char pop(Stack* s) {
    return s->num[s->top--];
}

void clear(Stack* s) {
    s->top = -1;
}

int main() {

    Stack s;
    init_stack(&s);
    char str[53];

    scanf("%s", str);

    for (int i = 0; str[i] != '\0'; i++) {
        push(&s, str[i]);
        if (s.top > 0 && s.num[s.top - 1] == '(' && s.num[s.top] == ')') {
            s.top -= 2;
        }
    }

    printf("%d", s.top + 1);
    
}