#include <iostream>
#include <stdlib.h>
#include <time.h>

typedef long long lien;

int count=1;
lien cunt=0;

class triple {
	lien a;
	lien b;
	lien c;

public:
	triple();
	triple(lien, lien, lien);
	void set(lien, lien, lien);
	lien getA();
	lien getB();
	lien getC();
	void manipulate();
	bool big(lien);
	lien dot(int*);
	void operator=(triple);
};

triple::triple() {
	a=0;
	b=0;
	c=0;
}

triple::triple(lien x, lien y, lien z) {
	a=x;
	b=y;
	c=z;
}

void triple::set(lien x, lien y, lien z){
	a=x;
	b=y;
	c=z;
}

lien triple::getA(){
	return a;
}

lien triple::getB(){
	return b;
}

lien triple::getC(){
	return c;
}

lien triple::dot(int* array) {
	return a*(array[0])+b*(array[1])+c*(array[2]);
}

void triple::operator=(triple x) {
	a=x.getA();
	b=x.getB();
	c=x.getC();
}

triple transform(triple x, int a){
	if(a==1) {
		int r1[3]={1,-2,2};
		int r2[3]={2,-1,2};
		int r3[3]={2,-2,3};
		return triple(x.dot(r1), x.dot(r2), x.dot(r3));
	}

	else if(a==2) {
		int r1[3]={1,2,2};
		int r2[3]={2,1,2};
		int r3[3]={2,2,3};
		return triple(x.dot(r1), x.dot(r2), x.dot(r3));
	}

	else {
		int r1[3]={-1,2,2};
		int r2[3]={-2,1,2};
		int r3[3]={-2,2,3};
		return triple(x.dot(r1), x.dot(r2), x.dot(r3));
	}

}

triple multiply(triple x, int n) {
	return triple((x.getA())*n,(x.getB())*n,(x.getC())*n);
}

void generate(triple x,lien limit){

	if(x.big(limit))
		return;

	x.manipulate();

	int i=2;
	triple z;
	while(true) {
		z=multiply(x,i);
		if(z.big(limit))
			break;

		z.manipulate();
		i++;
	}

	generate(transform(x,1),limit);
	generate(transform(x,2),limit);
	generate(transform(x,3),limit);
}

bool triple::big(lien limit) {
	return ((a+b+c)>=limit);
}

void triple::manipulate() {
	// std::cout<<count++<<"  :  "<<a<<", "<<b<<", "<<c<<" : "<<a+b+c<<std::endl;
	lien x,y;
	x=std::min(a,b);
	y=std::max(a,b);
	// std::cout<<x<<"  "<<y<<"  "<<(c%(y-x)==0)<<std::endl;
	if(c%(y-x)==0)
		cunt+=1;

}

int main(int argc, char* argv[]){
	cunt=0;
	lien limit=atoll(argv[1]);
	triple h(3,4,5);

	int start_s=clock();
	
		generate(h,limit);
	
	int stop_s=clock();

	std::cout<<cunt<<std::endl;
	std::cout<<"Time Taken For Execution : "<<(stop_s-start_s)/double(CLOCKS_PER_SEC)<<" seconds"<<std::endl;
}

