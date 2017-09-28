import math

def count(r):
	l=[[0]*20]*20
	for i in range(0,10):
		l[0][i]=0;
	for(;i<=9+(9/r);)
		l[0][i++]=1;
	while(i<=18)
		l[0][i++]=0;
	for(i=1;i<=14;++i) {
		for(j=0;j<19;++j) {
			if(l[i-1][j]==0)
				continue;
			low=9+ceil(-j/r);
			high=9+ceil((9-j)/r);
			for(k=low;k<=high;++k)
				l[i][k]+=l[i-1][j];
		}
	}
	s=0;
	for(i=9;i<19;++i)
		s+=l[14][i];
	return s;
}

int main() {
	int r,i;
	long long s,x;
	for(r=1;r<10;++r) {
		x=count(r);
		cout<<r<<" "<<x<<endl;
		s+=x;
	}
	cout<<"Sum : "<<s;
}