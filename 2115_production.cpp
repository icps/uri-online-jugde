// Using C++ (g++ 8.4.5, -std=c++11 -O2 -lm)
// Greedy Solution

#include<bits/stdc++.h>

using namespace std;

#define pii pair<int,int>

main()
{
	
	int N;
	vector < pii > jobs;
	
	int ans = 1;
	int time = 1;
	while(cin >> N)
	{
		ans = 1;
		time = 1;
		jobs.clear();
		for(int i = 0 ; i < N ; i++)
		{
			pii aux;
			cin>>aux.first;
			cin>>aux.second;
			jobs.push_back(aux);
		}

		sort(jobs.begin(), jobs.end());
		//printf("%d", jobs[0].first);
		for(int i = 0 ; i < N ; i++)
		{
			pii curr = jobs[i];
			if (curr.first > time)
			{
				time += (curr.first - time) + curr.second;
			}
						
			else
			{
				time += curr.second;
			}
		}
		cout<<time<<endl;
	}
}
