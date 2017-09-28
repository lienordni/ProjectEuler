#include <iostream>
#include <math.h>

using namespace std;

unsigned long long count(int r) {
	int i,j,k,low,high;
	unsigned long long s,list[15][19];
	for(i=0;i<=2;++i)
		for(j=0;j<19;++j)
			list[i][j]=0;
	for(i=0;i<9;++i)
		list[0][i]=0;
	for(;i<=9+(9/r);)
		list[0][i++]=1;
	while(i<=18)
		list[0][i++]=0;
	for(i=1;i<=2;++i){
		for(j=0;j<19;++j) {
			if(list[i-1][j]==0)
				continue;
			low=9+ceil((9-j)/r);
			high=9+ceil((18-j)/r);
			for(k=low;k<=high;++k) {
				list[i][k]+=list[i-1][j];
				// list[i][k]%=11;
			}
		}
	}
	s=0;
	for(i=9;i<19;++i)
		s+=list[2][i];
	for(i=0;i<=2;++i) {
		for(j=0;j<19;++j) {
			if(list[i][j]<10)
				cout<<" ";
			cout<<list[i][j]<<"  ";
		}
		cout<<endl;
	}


	return s;
}

int main() {
	int r,i;
	unsigned long long s=floor(100000/11),x;
	for(r=2;r<3;++r) {
		x=count(r);
		cout<<r<<" "<<x<<endl;
		s+=x;
	}
	cout<<"Sum : "<<s<<endl;
}