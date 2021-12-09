#include <iostream>
using namespace std;

int main() {
    int T;
    cin>>T;
    char first, second, third;
    char x, y;
    while(T--) {
        cin>>first>>second>>third;
        cin>>x>>y;
        if(first==x)
            cout<<x;
        else if(first == y)
            cout<<y;
        else if (second == x)
            cout<<x;
        else if (second == y)
            cout<<y;
        else if (third == x)
            cout<<x;
        else if (third == x)
            cout<<y;
        cout<<endl;
    }
	return 0;
}
