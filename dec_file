#include <bits/stdc++.h>
#define UNASSIGNED -2
#define DONE -1
#define CHEF 0
#define ASSISTANT 1
using namespace std;
int main(){
	int t;
	cin >> t;
	while(t--){
		int n,m,tmp;
		cin >> n >> m;
		vector<int> jobs(n,UNASSIGNED);
		for(int i=0;i<m;i++){
			cin >> tmp;
			jobs[tmp-1] = DONE;
		}
		vector<int> chefAssigned;
		vector<int> assistantAssigned;
		int turn = CHEF;
		for(int i=0;i<n;i++){
			if(jobs[i]==UNASSIGNED){
				if(turn==CHEF){
					chefAssigned.push_back(i+1);
					turn = ASSISTANT;
				}
				else{
					assistantAssigned.push_back(i+1);
					turn = CHEF;
				}
			}
		}
		if(chefAssigned.size()==0)
			cout << endl;
		else{
			for(int i=0;i<chefAssigned.size();i++){
			cout << chefAssigned[i] << " ";
			}
			cout << endl;
		}
		
		if(assistantAssigned.size()==0)
			cout << endl;
		else{
			for(int i=0;i<assistantAssigned.size();i++){
			cout << assistantAssigned[i] << " ";
			}
			cout << endl;
		}
		
	}
	return 0;
}