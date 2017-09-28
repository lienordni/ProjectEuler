#include <iostream>
#include <math.h>
#include <stdlib.h>

using namespace std;

double a,b;

class point {

private:
	double x;
	double y;

public:
	point(){
		x=0;
		y=0;
	}
	point(double,double);
	void operator=(point);
	point operator+(point);
	bool operator==(point);
	bool operator!=(point);
	bool test();
	void set(double,double);
	void print();
	void print(int);
	double distance(point);
	double getx();
};

double point::getx()
{
	return x;
}

double point::distance(point q)
{
	return sqrt((q.x-x)*(q.x-x)+(q.y-y)*(q.y-y));
}

void point::print()
{
	cout<<"("<<x<<","<<y<<")"<<endl;
}

void point::print(int i)
{
	cout<<i<<" : ("<<x<<","<<y<<")"<<endl;
}

void point::set(double a, double b)
{
	x=a;
	y=b;
}

point::point(double a, double b)
{
	x=a;
	y=b;
}

void point::operator=(point p)
{
	x=p.x;
	y=p.y;
}

point point::operator+(point w)
{
	double p,q,r,s,min,mt,mr;
	double alpha,beta,gamma;
	double e,f;
	double h1,h2,k1,k2;
	point z1,z2;

	p=this->x;
	q=this->y;
	r=w.x;
	s=w.y;

	min=(s-q)/(r-p);
	mt=-(b*b*r)/(a*a*s);

	// cout<<"Incident Slope : "<<min<<endl;
	// cout<<"Tangential Slope : "<<mt<<endl;

	alpha=2*mt/(1-mt*mt);
	mr=(alpha-min)/(1+alpha*min);

	// cout<<"Reflected Slope : "<<mr<<endl;

	e=s-mr*r;
	f=mr;

	alpha=a*a*f*f+b*b;
	beta=2*a*a*e*f;
	gamma=a*a*e*e-a*a*b*b;

	h1=(-beta+sqrt(beta*beta-4*alpha*gamma))/(2*alpha);
	h2=(-beta-sqrt(beta*beta-4*alpha*gamma))/(2*alpha);

	k1=e+f*h1;
	k2=e+f*h2;

	z1.set(h1,k1);
	z2.set(h2,k2);

	if(z1!=w && z2!=w){
		z1.print();
		z2.print();
		cout<<z1.distance(w)<<endl;
		cout<<z2.distance(w)<<endl;
		cout<<"FUUUUUCK"<<endl;
	}

	if(z1==w)
		return z2;
	return z1;
}

bool point::operator==(point p)
{
	return distance(p)<=0.0000000001;
}

bool point::operator!=(point p)
{
	return !((*this)==p);
}

bool point::test()
{
	return (y>0 && fabs(x)<=0.001);
}

int main()
{
	a=5;
	b=10;
	point x,y,z;
	x.set(0,10.1);
	y.set(1.4,-9.6);
	int i=1;
	while(true){
		z=x+y;
		z.print(i++);
		if(z.test())
			cin.get();
		x=y;
		y=z;
	}

}