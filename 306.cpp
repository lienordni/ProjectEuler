#include <iostream>
#include <stdlib.h>

class lien {
public:
	bool win;
	bool lose;
	bool flag;
	
	lien();
	lien(int, int);
	
	lien operator*(lien);
	lien operator+(lien);
	void operator=(lien);
	bool operator==(lien);
	void operator+=(lien);
};

void print(lien);

lien::lien() {
	win=false;
	lose=false;
	flag=false;
}

lien::lien(int x, int y) {
	win=(bool) x;
	lose=(bool) y;
	flag=false;
}

lien lien::operator*(lien y) {
	lien w(1,0), l(0,1), wl(1,1), x(0,0);
	if(*this==w){
		if(y==w){
			return w;
		}

		else if(y==l) {
			return l;
		}

		else if(y==wl) {
			return x;
		}
	}

	else if(*this==l) {
		if(y==w){
			return l;
		}

		else if(y==l) {
			return w;
		}

		else if(y==wl) {
			return x;
		}
	}

	else if(*this==wl) {
		if(y==w){
			return x;
		}

		else if(y==l) {
			return x;
		}

		else if(y==wl) {
			return l;
		}
	}

	std::cout<<"Got fucked"<<std::endl<<std::endl;
	std::cin.get();
	return w;
}

lien lien::operator+(lien x) {
	lien y(this->win || x.win, this->lose || x.lose);
	return y;
}

void lien::operator=(lien x) {
	this->win=x.win;
	this->lose=x.lose;
}

bool lien::operator==(lien x) {
	return ((win==x.win) && (lose==x.lose));
}

void lien::operator+=(lien x) {
	(*this)=(*this)+x;
}

void print(lien x) {
	std::cout<<(int) x.win<<" "<<(int) x.lose<<std::endl;
}

lien w(1,0), l(0,1), wl(1,1), x(0,0);
lien array[10000001];

lien func(int n) {

	if(array[n].flag)
		return array[n];

	if(n<2)
		return l;

	if(n<4)
		return w;

	lien s=x,p;
	for(int i=0;i<=(n-2)/2;++i) {
		p=func(i)*(func(n-2-i));
		// std::cout<<"P : ";
		// print(p);
		s+=p;
		if(s==wl)
			break;
	}

	array[n].flag=true;
	array[n]=s;
	return s;
}

int main(int argc, char* argv[]) {
	lien y;
	int i;
	
	int count=0;

	for(i=0;i<=atoi(argv[1]);++i) {
		std::cout<<i<<"  ";
		y=func(i);
		if(y.win)
			count++;
		print(y);
		if(y==x)
			std::cin.get();
	}

	std::cout<<count<<std::endl;
}

