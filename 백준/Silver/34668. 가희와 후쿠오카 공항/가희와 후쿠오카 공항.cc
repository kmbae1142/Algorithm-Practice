#include <iostream>
#include <string>

using namespace std;

int main() {
	cin.tie(NULL), cout.tie(NULL), ios::sync_with_stdio(0);
	int Q;
	cin >> Q;

	while (Q--)
	{
		int M;
		cin >> M;
		int hh_s = 6;
		int mm_s = 6;
		int time = M / 50 * 12;
		int hh = time / 60;
		int mm = time % 60;
		
		hh_s += (mm + mm_s) / 60 + hh;
		mm_s = (mm + mm_s) % 60;
		
		if ((hh_s >= 0 && hh_s < 24) && (mm_s >= 0 && mm_s < 60)) {
			string result_hh = "", result_mm = "";
			if (hh_s / 10 == 0) result_hh += '0' + to_string(hh_s);
			else result_hh += to_string(hh_s);

			if (mm_s / 10 == 0) result_mm += '0' + to_string(mm_s);
			else result_mm += to_string(mm_s);

			cout << result_hh << ':' << result_mm << '\n';
		}
		else {
			cout << "-1\n";
		}
	}

	return 0;
}