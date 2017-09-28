#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <ctime>
#include <vector>

int SOF[1000001];

using namespace std;

long long sof(long long x)
{
	bool range=(x<=1000000);
	if(SOF[x]!=-1 && range)
		return SOF[x];
	long long s=1,i;
	for(i=2;i<=(long long) (sqrt(x));++i)
		if(!(x%i)) {
			if(i-x/i)
				s+=i+x/i;
			else
				s+=i;
		}

	if(range)
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

int main(int argc,char* argv[])
{
	int limit=1000000;
	int i,c,p;
		for(i=1;i<=limit;++i)
			SOF[i]=-1;
	// limit=atoi(argv[1]);
	vector<int> nicevalues,temp;

	for(i=1;i<=limit;++i)
	{
		cout<<"-----------"<<i<<"---------"<<endl;
		if(i==sof(i)) {
			// cout<<"Too Perfect"<<endl;
			continue;
		}

		temp.clear();
		temp.push_back(i);
		c=i;
		while(true) 
		{
			c=sof(c);
			// cout<<c<<" : ";
			if(c==1 || c>limit) {
				// cout<<"Out of Range"<<endl;
				break;
			}
			p=position(c,temp);
			temp.push_back(c);
			// for(int j=0;j<temp.size();++j)
			// 	cout<<temp[j]<<", ";
			// cout<<"Position : "<<p<<endl;
			if(p!=-1){
				if(p==0) {
					cout<<c<<endl;
					nicevalues.push_back(c);
				}

				else {
					break;
				}
			}

		}

		// cin.get();
		cout<<endl<<endl;


	}
	cout<<"+++++++++++++++++++++++++++++++++++"<<endl;
	cout<<nicevalues.size()<<endl;
	for(i=0;i<nicevalues.size();++i)
		cout<<nicevalues[i]<<endl;




}