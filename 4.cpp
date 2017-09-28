#include<iostream>
#include<conio.h>

using namespace std;

int main()
{
	int i,j,k,l,n,x,y;
	
	for(i=999;i>=100;--i)
		{
			j=i*1000+i/100+10*((i/10)%10)+100*(i%10);
			for(x=999;x>=100;--x)
				{
					if(j%x==0)
						{
							if(j/x>99 && j/x<1000)
								{
									cout<<j<<" = "<<x<<" * "<<j/x<<endl;
									getch();
								}
						}
				}
//			cout<<endl;
		}
}
