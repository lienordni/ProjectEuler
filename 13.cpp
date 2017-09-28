#include<iostream>
#include<conio.h>
#include<math.h>
#include<fstream>

using namespace std;

fstream lien(".\\13.txt",ios::in);

class str
{
	public:
	
	char a[100];
	int l;
	
	void get()
	{
		char t;
		int i;
		lien>>this->a;
		for(i=0;this->a[i]!='\0';++i);
		this->l=i;
		for(i=0;i<l/2;++i)
			{
				t=a[i];
				a[i]=a[l-i-1];
				a[l-i-1]=t;
			}
			
		fuck();
	}
	
	void disp(char c='\n')
	{
		unfuck();
		for(int i=0;i<l;++i)
			cout<<a[l-i-1];
		cout<<c;
		fuck();
	}
	
	str()
		{
			for(int i=0;i<100;++i)
				a[i]='\0';
			l=0;
		}

	void fuck()
	{
			for(int i=0;i<l;++i)
				a[i]-=48;
	}

	void unfuck()
	{
			for(int i=0;i<l;++i)
				a[i]+=48;
	}

	str operator+(str x);
	void operator=(str x); 
	str operator+=(str x)
		{
			*this=(*this)+x;
		}
};

void str::operator=(str x) 
{
	this->l=x.l;
	for(int i=0;i<x.l;++i)
		this->a[i]=x.a[i];
}

str str::operator+(str x)
{
	char c='\0';
	int i=0;
	str y;
	while(i<this->l && i<x.l)
		{
			y.a[i]=(char) (((int) (this->a[i]+x.a[i]+c))%10);
			c=(char) (((int) (this->a[i]+x.a[i]+c))/10);
			i++;
			y.l++;
		}
		
	while(i<l)
		{
			y.a[i]=(char) (((int) (this->a[i]+c))%10);
			c=(char) (((int) (this->a[i]+c))/10);
			i++;
			y.l++;
		}

	while(i<x.l)
		{
			y.a[i]=(char) (((int) (x.a[i]+c))%10);
			c=(char) (((int) (x.a[i]+c))/10);
			i++;
			y.l++;
		}
	
	if(c)
		{
			y.a[i]=c;
			y.l++;
		}
	return y;
}


int main()
{
	int i;
	str x,y;
	
	while(lien)
		{
			x.get();
			y+=x;
		}
	
	y.disp();
	
	
}
