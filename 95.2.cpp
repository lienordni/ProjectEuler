#include <iostream>
#include <math.h>
#include <ctime>
#include <stdlib.h>
#include <vector>

using namespace std;

int SOF[1000001];

long long sof(long long x)
{
	if(x>1000000){
		long long s=1,i;
		for(i=2;i<=(long long) (sqrt(x));++i)
			if(!(x%i)) {
				if(i-x/i)
					s+=i+x/i;
				else
					s+=i;
			}
		return s;

	}

	if(SOF[x]!=-1)
		return SOF[x];
	long long s=1,i;
	for(i=2;i<=(long long) (sqrt(x));++i)
		if(!(x%i)) {
			if(i-x/i)
				s+=i+x/i;
			else
				s+=i;
		}
	SOF[x]=s;
	return s;
}

int position(int x,vector<int> v)
{
	for(int i=0;i<v.size();++i)
		if(v[i]==x)
			return i;
	return -1;
}
/*
Status 0 : Untouched
Status 1 : Perfect Loop
Status 2 : Imperfect Loop
Status 3 : Prime
Status 4 : Goes Beyond limit
Status 5 : Perfect Number or terminates at a perfect number
*/

int main(int argc,char* argv[])
{
	clock_t start=clock();
	int limit=atoi(argv[1]);
	for(int i=1;i<=limit;++i)
		SOF[i]=-1;
	cout<<"Lienordni"<<endl;
	int c;
	bool fakeshit,party,stupidshit;
	int chainsize=atoi(argv[2]);
	vector<int> array(chainsize);
	int *status=new int[limit+1];
	int p;
	cout<<"Lienordni"<<endl;
	for(int i=2;i<=limit;++i){
		if(status[i])
			continue;		
		cout<<i<<endl;
		if(sof(i)==i || sof(i)==1 || sof(i)>limit){
			status[i]=3;
			continue;
		}

		c=i;
		fakeshit=false;
		party=false;
		stupidshit=false;
		array.clear();
		array.push_back(i);
		cout<<"Lienordni"<<endl;
		while(true){
			c=sof(c);
			if(status[c]==3) {
				status[i]=3;
				fakeshit=true;
				break;
			}

			p=position(c,array);
			if(p!=-1){
				if(p==0) {
					party=true;
					break;
				}
				else {
					fakeshit=true;
					break;
				}
			}

			if(c==1 || c>limit){
				fakeshit=true;
				break;

			}
			array.push_back(c);

		}
		
		if(party){
			for(int j=0;j<array.size();++j)
				cout<<array[j]<<" ";
			cout<<endl;

		}

		if(fakeshit)
			continue;
	}

	int fs,k,i;
	clock_t end=clock();
	double timediff=double(end-start)/CLOCKS_PER_SEC;
	std::cout<<"Time Taken : "<<timediff<<" seconds"<<std::endl;

}