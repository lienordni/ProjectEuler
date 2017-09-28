#include<iostream>
#include<math.h>
#include<conio.h>

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

int main()
{
	int i,n,j,x;
	for(i=0;i<100000;++i)
		d[i]=-1;
	d[1]=0;
	d[2]=1;
	x=0;
	for(i=0;i<10000;++i)
		{
			if(D(i)==i)
				continue;
			
			if(D(D(i))==i)
				{
					cout<<i<<"  "<<D(i)<<endl;
					x+=i;
				}
		}
	cout<<endl<<x;
}
