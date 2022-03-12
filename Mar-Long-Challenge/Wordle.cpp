#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    while(T--){
        char S[5], t[5], M[5];
        cin >> S;
        cin >> t;
        for (int i=0; i<5; i++) {
            if (S[i] == t[i])
                M[i] = 'G';
            else
                M[i] = 'B';
        }
        cout << M << endl;
    }
	// your code goes here
	return 0;
}
