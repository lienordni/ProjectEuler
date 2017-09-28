#include <iostream>
#include <math.h>
#include <ctime>
#include <stdlib.h>
#include <vector>

using namespace std;

int SOF[1000001];

long long sof(long long x)
{
	// if(SOF[x]!=-1)
	// 	return SOF[x];
	long long s=1,i;
	for(i=2;i<=(long long) (sqrt(x));++i)
		if(!(x%i)) {
			if(i-x/i)
				s+=i+x/i;
			else
				s+=i;
		}
	// SOF[x]=s;
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
	// for(int i=1;i<=limit;++i)
	// 	SOF[i]=-1;
	// int c;
	// cin>>c;
	// while(true){
	// 	c=sof(c);
	// 	cout<<c<<endl;
	// 	cin.get();
	// }
	int c=0;
	for(int i=1;i<=1000001;++i)
		if(sof(i)>1000000){
			cout<<i<<endl;
			c++;
		}
	cout<<c<<endl;
}