#include<iostream>
#include<conio.h>
#include<math.h>

using namespace std;

int main()
{
	int x,n,i,c;
	
	for(x=2;x<=1000;++x)
		{
			cout<<x<<" : ";
			c=x;
			while(2*(c/2)==c)
				c/=2;
			while(5*(c/5)==c)
				c/=5;
			cout<<c<<endl;
			continue;
			if(c==1)
				{
					cout<<"Non-recurring"<<endl;
					continue;
				}
			n=1;
			while(int(log10(c*n+1))!=log10(c*n+1))
				n++;
			cout<<n;
			cout<<endl;
			getch();
			
		}
}
