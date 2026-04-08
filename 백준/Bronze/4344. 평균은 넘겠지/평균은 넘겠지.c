#include <stdio.h>

int main() {

	int C;
	scanf("%d", &C);

	while (C--) {
		int N, sum = 0, cnt = 0;
		int score[1000];
		scanf("%d", &N);

		for (int i = 0; i < N; i++) {
			scanf("%d", &score[i]);
			sum += score[i];
		}

		double avg = (double)sum / N;
		for (int i = 0; i < N; i++) {
			if ((double)score[i] > avg) {
				cnt++;
			}
		}

		printf("%.3lf%%\n", (double)cnt / N * 100);
	}

	return 0;

}