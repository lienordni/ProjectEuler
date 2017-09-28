#include <iostream>
#include <math.h>

using namespace std;

typedef long long lien;

bool issquare(lien x) {
	lien y=lien(sqrt(x));

	return (y*y==x || (y+1)*(y+1)==x);
}

int main(){
	int i,j,k,n,x,y,z;

	int limit=10000;

	for(x=3;x<=limit;++x){
		for(y=2;y<x;++y){
			for(z=1;z<y;++z){
				if(issquare(x+y) && issquare(x-y) && issquare(y+z)&& issquare(y-z) && issquare(x+z) && issquare(x-z)) {
					cout<<x<<"  "<<y<<"  "<<z<<"  "<<x+y+z<<"\n";
					return 0;
				}
			}
		}
	}

}