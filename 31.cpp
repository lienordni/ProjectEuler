#include<iostream>
#include<conio.h>

using namespace std;

int main()
{
	int n[8],v[8]={1,2,5,10,20,50,100,200},i,j,c=0;
	for(n[0]=0;n[0]<=200;++n[0])
		{
		for(n[1]=0;n[1]<=100;++n[1])
			for(n[2]=0;n[2]<=40;++n[2])
				for(n[3]=0;n[3]<=20;++n[3])
					for(n[4]=0;n[4]<=10;++n[4])
						for(n[5]=0;n[5]<=4;++n[5])
							for(n[6]=0;n[6]<=2;++n[6])
								for(n[7]=0;n[7]<=1;++n[7])
									{
										j=0;
										for(i=0;i<8;++i)
											j+=n[i]*v[i];
										if(j==200)
											{
//												for(i=0;i<8;++i)
//													cout<<n[i]<<" * "<<v[i]<<"  ";
//												cout<<endl;
												c++;
//												getch();
											}
										
									}
			cout<<n[0]<<endl;
		}
	cout<<endl<<endl<<"c = "<<c;
	getch();
}
