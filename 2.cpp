#include<iostream>
using namespace std;

class fm
{
	public:
	long long a,b,c,d;
	fm()
	{
		a=b=c=1;
		d=0;
	}
	
	fm operator*(fm x)
	{
		fm y;
		y.a=this->a*x.a+this->b*x.c;
		y.b=this->a*x.b+this->b*x.d;
		y.c=this->c*x.a+this->d*x.b;
		y.d=this->c*x.b+this->d*x.d;
		return y;
	}
	
	fm operator^(long long n)
	{
		fm y;
		if(n==0)
		{
			y.a=y.d=1;
			y.b=y.c=0;
			return y;
		}
		
		if(n==1)
		{
			return *this;
		}
		
		if(!n%2)
		{
			fm y;
			y=*this^(n/2);
			return y*y;
		}
		
		return (*this)*(*this^(n-1));
	}	
	
};

class fm2
{
	public:
	long long a,b,c,d;
	long long m;
	
	fm2()
	{
		a=b=c=1;
		d=0;
	}
	
	fm2 operator*(fm2 x)
	{
		fm2 y;
		y.a=(this->a*x.a+this->b*x.c)%m;
		y.b=(this->a*x.b+this->b*x.d)%m;
		y.c=(this->c*x.a+this->d*x.b)%m;
		y.d=(this->c*x.b+this->d*x.d)%m;
		return y;
	}
	
	fm2 operator^(long long n)
	{
		fm2 y;
		if(n==0)
		{
			y.a=y.d=1;
			y.b=y.c=0;
			return y;
		}
		
		if(n==1)
		{
			return *this;
		}
		
		if(!n%2)
		{
			fm2 y;
			y=*this^(n/2);
			return y*y;
		}
		
		return (*this)*(*this^(n-1));
	}	
	
};

long long fib(long long n)
{
	fm x;
	return (x^n).b;
}

long long fib(long long n, long long m)
{
	fm2 x;
	x.m=m;
	return ((x^n).b)%m;
}

int main()
{
	long long x,i,s,y;
	for(s=0,i=1;i<34;++i)
		{
			y=fib(i);
			if(y%2==0)
				s+=y;
		}
	cout<<s;
		

}
