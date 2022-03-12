#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        long long N, X, A, B, C;
        cin >> N;
        cin >> X;
        A = X/3+1;
        B = A*3-X;
        if (B == 3) {
            A--;
            B = 0;
        }
        if (A+B <= N) {
            C = N -A -B;
            cout <<"YES" << endl;
            cout << A <<" "<< B << " " << C << endl;
        }
        else
            cout<<"NO"<<endl;
    }
	return 0;
}
