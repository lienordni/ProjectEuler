#include <iostream>
#include <math.h>
#include <vector>
#include <iomanip>
#include <stdlib.h>
#include <time.h>

typedef long long lien;
long double q;

struct point {
	lien x;
	lien y;

	point();
	point(lien,lien);
	void set(lien, lien);
	bool on_circle(lien n);
};

typedef std::vector<point> points;

point::point(){
	x=0;
	y=0;
}

point::point(lien a, lien b) {
	x=a;
	y=b;
}

void point::set(lien q, lien w) {
	x=q;
	y=w;
}

bool point::on_circle(lien n) {
	return (x*x+y*y==(n*(x+y)));
}

void print(points p) {
	int i;
	for(i=0;i<p.size();++i)
		std::cout<<"("<<p[i].x<<","<<p[i].y<<") ";
	std::cout<<std::endl;
}

bool perfect_square(lien n){
	lien x=lien(sqrt(n));
	if((n==x*x) || (n==(x+1)*(x+1))){
		std::cout<<n;
		std::cin.get();
	}
	return ((n==x*x) || (n==(x+1)*(x+1)));
}

points lattice_points(lien n) {
	
	points p;
	point t;
	// p.push_back(point(0,0));
	// p.push_back(point(0,n));
	// p.push_back(point(n,0));
	// p.push_back(point(n,n));

	lien peak=n*q;

	lien x,y;
	lien d;
	for(y=n+1;;++y){
		d=n*n+4*y*n-4*y*y;
		if(d<0){
			break;
		}
		// std::cout<<"lien"<<std::endl;
		if(!(perfect_square(d)))
			continue;

		if(d%2==n%2){
			x=(n+int(sqrt(d)))/2;
			t.set(x,y);
			if(t.on_circle(n)==false){
				std::cout<<"FUUUUUUUUUUUUUUUUUUUUUUUUCK"<<std::endl;
				std::cin.get();
			}
			p.push_back(t);
		}
	}

	return p;
}

lien f(lien n) {
	return 4+8*((lattice_points(n)).size());
}

int main(int argc, char* argv[]){
	q=1.2072;
	// std::cout<<std::setprecision(35)<<q<<std::endl;
	int start=clock();
	std::cout<<(f(atoll(argv[1])))<<std::endl;
	int end=clock();
	std::cout<<"Time take for execution : "<<(end-start)/double(CLOCKS_PER_SEC)<<" seconds"<<std::endl;
}