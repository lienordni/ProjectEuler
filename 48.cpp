#include<iostream>
#include<conio.h>

using namespace std;

long long m=10000000000;
long long ans(int n)
{
	long long x=1,i;
	for(i=0;i<n;++i)
		{
			x*=n;
			x%=m;
		}
	return x;
}

int main()
{
	long long x,y=0,n;
	int i;
	for(i=1;i<=1000;++i)
		{
			y+=ans(i);
			y%=m;
		}
	cout<<y;
}
