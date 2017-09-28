#include <iostream>
#include <math.h>
#include <stdlib.h>

using namespace std;

bool ps(long double n)
{
	return sqrt(5*n*n+14*n+1)==int(sqrt(5*n*n+14*n+1));
}

int main(int argc, char* argv[])
{
	// long long x=atoll(argv[1]);
	int count=1;
	long long n=1,s=0;
	while(true){
		if(ps(n)){
			cout<<count<<"  "<<n<<endl;
			s+=n;
			count++;
			if(count==201)
				break;
		}
		n++;
	}
	cout<<s<<endl;
}