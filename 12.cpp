#include<iostream>
#include<math.h>
#include<conio.h>

using namespace std;

int nof(long long x)
{
	int i,n=0;
	for(i=1;i*i<x;++i)
		if(x%i==0)
			n+=2;
	if(i*i==x)
		n++;
	return n;
}

int main()
{
	long long x=1,i=1;
	while(true)
	{
		x=i*(i+1)/2;
		i++;
		cout<<x<<" "<<nof(x)<<endl;
		if(nof(x)>=500)
			getch();
	}
}
