#include<iostream>
#include<math.h>

using namespace std;

int d[100000];

int D(int n)
{
	if(d[n]!=-1)
		return d[n];
	
	int i,s=0;
	for(i=1;i<n;++i)
		if(n%i==0)
			s+=i;
	d[n]=s;
	return s;
}

bool abundant(int x)
{
	if(D(x)>x)
		return true;
	return false;
}

bool sum(int x)
{
	int i;
	for(i=1;i<=x/2;++i)
		{
			if(abundant(i) && abundant(x-i))
				return true;
		}
	return false;
}
int main()
{
	int i,x=0;
	
	for(i=0;i<100000;++i)
		d[i]=-1;
	d[1]=0;
	d[2]=1;

	for(i=1;i<=28123;++i)
		{
			if(!sum(i))
				{
					cout<<i<<endl;
					x+=i;
				}
		}
	cout<<"x = "<<x;
}
