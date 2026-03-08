#include <stdio.h>
#include <time.h>

int main() {

    time_t current;
    time(&current);

    struct tm* t = localtime(&current);

    printf("%d\n%02d\n%02d", 1900 + t->tm_year, t->tm_mon + 1, t->tm_mday);

}