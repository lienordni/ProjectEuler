#include<iostream>
#include<conio.h>
using namespace std;

class frac
{
	public:
	int num;
	int den;
	float value;
	void simp()
		{
			int i;
			for(i=2;i<=num;)
				if(num%i==0 && den%i==0)
					{
						num/=i;
						den/=i;
					}
				else i++;
		}
	
	void eq(int i,int j)
		{
			num=i;
			den=j;
		}
		
	void disp(char c='\0')
		{
			cout<<num<<"/"<<den<<c;
		}
	
};

int main()
{
	frac f,g;
	int i,j,n,x,a,b,c,d,e,fi;
	for(i=10;i<100;++i)
		{
			for(j=10;j<100;++j)
				{
					if((i%10==0 && j%10==0) || i==j)
						continue;
					f.eq(i,j);
					g.eq(i,j);
					f.simp();
					if(f.den<10)
						{
							a=g.num/10;
							b=g.num%10;
							c=g.den/10;
							d=g.den%10;
							e=f.num;
							fi=f.den;
							if((a==c && b*fi==e*d) || (a==d && b*fi==e*c) || (b==c && a*fi==d*e) || (b==d && a*fi==c*e))
							{
								g.disp('=');
								f.disp('\n');
								getch();
							}
						}
				}
		}
}
