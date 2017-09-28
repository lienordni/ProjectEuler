#include <iostream>
#include <math.h>
#include <ctime>
#include <stdlib.h>

using namespace std;

int SOF[1000001];

long long sof(long long x)
{
	if(SOF[x]!=-1)
		return SOF[x];
	long long s=1,i;
	for(i=2;i<=(long long) (sqrt(x));++i)
		if(!(x%i)) {
			if(i-x/i)
				s+=i+x/i;
			else
				s+=i;
		}
	SOF[x]=s;
	return s;
}

class node {
	
private:
	int value;
	node* next;
	int status;
	node** baaps;

public:
	int getValue();
	node(int);
	node();
	// void setNext(node* ptr);
	node* getNext();
	void set(int,node*);
	void display(char);
	void display(char*);
	void setStatus(int);
	int getStatus();

};

int node::getStatus() {
	return status;
}

void node::setStatus(int x) {
	status=x;
}

node* node::getNext() {
	return next;
}

void node::display(char ch='\n') {
	std::cout<<value<<ch;
}

void node::display(char *ch) {
	std::cout<<value<<ch;
}

void node::set(int x,node* ptr) {
	value=x;
	next=ptr;
}

int node::getValue() {
	return value;
}

node::node(int x) {
	value=x;
	next=NULL;
	status=0;
}

node::node() {
	value=0;
	next=NULL;
	status=0;
}

/*

Status 0 : Untouched
Status 1 : Perfect Loop
Status 2 : Imperfect Loop
Status 3 : Prime
Status 4 : Goes Beyond limit
Status 5 : Perfect Number or terminates at a perfect number

*/

int main(int argc,char* argv[])
{
	clock_t start=clock();
	int limit=atoi(argv[1]);
	for(int i=1;i<=limit;++i)
		SOF[i]=-1;
	int fs,k,i;
	node* lien=new node[limit+1];
	int maxlength=30;
	for(i=1;i<=limit;++i) {

		for(k=0;k<=maxlength;++k){
			
		}

		lien[i].set(i,&lien[fs]);
	}


	int count=0;
	for(i=1;i<=limit;++i) {
		if(lien[i].getStatus()<=2) {
			std::cout<<i<<" : "<<sof(i)<<" : ";
//			if(lien[i].getStatus()<=2) 
			lien[i].getNext()->display('\0');
			count++;
			std::cout<<"        |      Status : "<<lien[i].getStatus()<<std::endl;
		}
	}
	std::cout<<count<<std::endl;
	clock_t end=clock();
	double timediff=double(end-start)/CLOCKS_PER_SEC;
	std::cout<<"Time Taken : "<<timediff<<" seconds"<<std::endl;

}