// Using C++ (g++ 8.4.5, -std=c++11 -O2 -lm)
// Dynamic Programming solution

#include<bits/stdc++.h>

using namespace std;


int main()
{
	int n, k;
	cin>>n;
	cin>>k;
	
	while(n + k != 0)
	{
		int va = n - k;
		for (int i = 1 ; i < n-va ; i++)
		{
			cout<<i<<' ';
		}
		for (int i = n ; i >= n-va+1 ; i--)
		{
			cout<<i<<' ';
		}
		cout << n-va << endl;
	
		cin>>n;
		cin>>k;
	}
}
