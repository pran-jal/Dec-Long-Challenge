#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        long long N;
        cin >> N;
        long long d = N/7;
        N = N%7;
        if (N >= 6)
            d+=1;
        cout << d << endl; 
    }
	// your code goes here
	return 0;
}
