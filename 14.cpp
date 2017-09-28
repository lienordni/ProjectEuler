#include<iostream>
#include<conio.h>
long long a[5000000];
using namespace std;
long long length(long long x)
{
	if(a[x]!=-1)
		{
//			cout<<endl<<x<<"!";
			return a[x];
		}
	
	if(x==1)
		return 1;
	
	if(x%2)
		{
//			cout<<endl<<3*x+1;
			a[x]=1+length(3*x+1);
			return 1+length(3*x+1);
		}
	
//	cout<<endl<<x/2;
	a[x]=1+length(x/2);
	return 1+length(x/2);
}

int main()
{
	long long i;
	for(i=0;i<5000000;++i)
		a[i]=-1;
	a[1]=1;
//	std::cout<<length(4255);
//	exit(0);
	long long m=0,lm=0;
	for(i=1;i<1000000;++i)
		{
			std::cout<<i<<" "<<length(i)<<std::endl;
			if(lm<length(i))
				{
					m=i;
					lm=length(i);
					getch();
				}
			
		}
}
