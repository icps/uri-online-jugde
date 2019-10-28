// Using C++ (g++ 8.4.5, -std=c++11 -O2 -lm)

#include<bits/stdc++.h>

using namespace std;

int tab[200][100010], numbers[200], n;

int solve(int idx, int sum_v, int total){
    
    if(tab[idx][sum_v] != -1)
    {
	return tab[idx][sum_v];
    }

    if(idx == n)
    {
        return abs(2 * sum_v - total);
    }

    return tab[idx][sum_v] = min(solve(idx+1,sum_v+numbers[idx], total),solve(idx+1,sum_v, total));

}

int main(){
    for (;cin>>n;)
    {
        int total = 0;

        for(int i=0;i<n;i++)
	{
		cin>>numbers[i];
	}

	for(int i=0;i<n;i++)
	{
		total+=numbers[i];
	} 

        memset(tab, -1, sizeof tab);

        cout<< solve(0,0, total)<<endl;
    }

}
