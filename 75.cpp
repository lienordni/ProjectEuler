#include <iostream>
#include <stdlib.h>
#include <fstream>

typedef long long lien;

int count=1;
std::fstream out("./75.txt",std::ios::out | std::ios::app);

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
	void disp();
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

void triple::disp() {

	// if(search(root,c))
	// 	return;

	// root=insert(root,c);

	std::cout<<count++<<"  :  "<<a<<", "<<b<<", "<<c<<" : "<<a+b+c<<std::endl;
	out<<a+b+c<<",";
}

bool triple::big(lien limit) {
	return ((a+b+c)>limit);
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

void print(triple x,lien limit){

	if(x.big(limit))
		return;
	

	x.disp();

	int i=2;
	triple z;
	while(true) {
		z=multiply(x,i);
		if(z.big(limit))
			break;

		z.disp();
		i++;
	}

	print(transform(x,1),limit);
	print(transform(x,2),limit);
	print(transform(x,3),limit);
}

int main(int argc, char* argv[]){
	lien limit=atoll(argv[1]);
	triple h(3,4,5);
	print(h,limit);
}