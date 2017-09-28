#include <iostream>
#include <math.h>
#include <cstring>
#include <stdlib.h>
int main(int argc, char* argv[]) {
	long long r,c,i,limit;
	limit=atoi(argv[1]);
	for(r=1;r<=limit/2;++r) {
		for(c=0;r*r+c*c<limit*limit/2;++c) {
			std::cout<<r<<" + i * "<<c<<std::endl;
		}
	}
}
