#include<iostream>
#include<conio.h>

using namespace std;

int main()
{
	long long i,j,k,n,x,y,m=1,lm=1;
	
	for(n=1;n<1000000;++n)
		{
			i=n;
			x=1;
			while(i-1)
				{
					if(i%2)
						i=3*i+1;
					else
						i/=2;
					x++;
				}
				
					cout<<n<<" ";
					cout<<x<<" ";
					cout<<endl;
			if(lm<x)
				{
//					cout<<(float) x/n<<endl;
					m=n;
					lm=x;
					getch();
				}
			
		}
	
}
