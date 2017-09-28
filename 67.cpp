#include<iostream>
#include<fstream>
#include<conio.h>
#include<math.h>

using namespace std;

int main()
{
	fstream xin(".\\67.txt",ios::in);
//	fstream xout(".\\18.txt",ios::out | ios::app);
	int i,j,k,l,x,y,n;
	
	int a[5050];
	for(i=0;i<5050;++i)
		xin>>a[i];
/*
	for(i=1;i<=15;++i)
		{
			for(j=0;j<i;++j)
				{
					if(a[j+(i*(i-1)/2)]<10)
						cout<<" ";
					if(a[j+(i*(i-1)/2)]<100)
						cout<<" ";
					
					cout<<a[j+(i*(i-1)/2)]<<" ";
				}
			cout<<endl;
		}
*/	
	for(i=5050-100-1;i>=0;--i)
		{

			a[i]+=(a[i+int((sqrt(1+8*i)-1)/2)+1]>a[i+int((sqrt(1+8*i)-1)/2)+2])?(a[i+int((sqrt(1+8*i)-1)/2)+1]):(a[i+int((sqrt(1+8*i)-1)/2)+2]);
/*			
			for(k=1;k<=15;++k)
				{
					for(j=0;j<k;++j)
						{
							if(a[j+(k*(k-1)/2)]<10)
								cout<<" ";
							if(a[j+(k*(k-1)/2)]<100)
								cout<<" ";
							
							cout<<a[j+(k*(k-1)/2)]<<" ";
						}
					cout<<endl;
				}
			getch();
			system("cls");
*/
		}
	cout<<a[0];
	
}
