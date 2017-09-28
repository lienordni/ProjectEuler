#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;

bool isq(int x)
{
	if(x==0 || x==1)
		return true;
	
	return int(sqrt(x))==sqrt(x);
}

int main()
{
	int i,j,k,x;
	for(i=2;i<999;++i)
		{
			for(j=2;j<1000-i;++j)
				{
					if(isq(i*i+j*j) && i+j+sqrt(i*i+j*j)==1000)
						{
							cout<<i<<"^2 + "<<j<<"^2 = "<<i*i+j*j<<endl<<i<<"+"<<j<<"+"<<sqrt(i*i+j*j)<<"="<<i+j+sqrt(i*i+j*j)<<endl<<endl;
							cout<<i*j*sqrt(i*i+j*j);
							getch();
						}
							
					
				}
		}
}
