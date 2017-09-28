#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main (int argc, char *argv[]) {
	ifstream lien("/home/lienordni/Desktop/Code/ProjectEuler/primes2.txt",ios::in);
	int x=0,i;

	int limit=atoi(argv[1]);
	// int limit=100;	
	char* c=new char[15];

	while(1) {
		lien>>c;
		x=atoi(c);
		if(x>limit)
			break;
		cout<<x<<endl;
	}
	return 0;
}
