#include <stdio.h>

int main() {

    int h, m, m_s = 0;
    int sum = 0;
    int m_div = 0;
    int m_rem = 0;
    int after_h_sum = 0;

    scanf("%d %d\n", &h, &m);
    scanf("%d", &m_s);

    sum = m + m_s;
    m_div = sum/60;
    m_rem = sum%60;
    after_h_sum = h + m_div;

    if (after_h_sum >= 24) {
        printf("%d %d", after_h_sum - 24, m_rem);
    }else {
        printf("%d %d", after_h_sum, m_rem);
    }
}
