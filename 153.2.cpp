#include <iostream>
#include <math.h>
#include <ctime>
#include <stdlib.h>
#include <fstream>

long long farey(long long limit)
{
	long long n=(long long) (sqrt(limit));
	long long aq,bq,a=0,b=1,c=1,d=n,k,i,sos,s;
	long long ss=0;
	while(c<=n)
	{
		k=(n+b)/d;
		aq=c;
		bq=d;
		c=k*c-a;
		d=k*d-b;
		a=aq;
		b=bq;
		sos=a*a+b*b;
		// std::cout<<a<<"  "<<b<<" : "<<sos<<" : "<<std::endl;
		if(sos>limit)
			continue;
		s=0;
		for(i=1;i<=limit/sos;++i)
		{	
			s+=(a-b)?(2*i*(a+b)*(limit/(i*sos))):(2*i*(a)*(limit/(i*sos)));
		}		
		// std::cout<<s<<std::endl;
		ss+=s;

	}
	// std::cout<<"Total Sum : "<<ss<<std::endl;
	return ss;
}

long long sof(long long x)
{
	long long s=0,i;
	for(i=1;i<=(long long) (sqrt(x));++i)
		if(!(x%i)) {
			if(i-x/i)
				s+=i+x/i;
			else
				s+=i;
		}
	return s;
}

long long sosof(long long x)
{
	long long s=0,i;
	for(i=1;i<=x;++i) {
		s+=sof(i);
		std::cout<<i<<std::endl;
	}

	return s;
}

long long sumofsumoffactors(int n)
{
	long long s=0,i;
	for(i=1;i<=n;++i)
	{
		s+=i*(n/i);
	}
	return s;
}

int main(int argc, char* argv[])
{
		long long limit=atoi(argv[1]);
		clock_t begin=clock();
		long long w,q;
		w=farey(limit);
		q=sumofsumoffactors(limit);
		std::cout<<q<<std::endl;
		std::cout<<w<<std::endl;
		std::cout<<q+w<<std::endl;
		clock_t end=clock();
		double timediff=double(end-begin)/CLOCKS_PER_SEC;
		std::cout<<"Time Taken : "<<timediff<<" seconds"<<std::endl;
		// std::cout<<sosof(limit)<<std::endl;
		// std::cout<<sof(5)<<std::endl;
}