#include "iostream"

using namespace std;

long long totient(int n)
{
	int* phi;
	int i,j;
	phi=new int[n+1];
	for(i=2;i<=n;++i)
	{
		phi[i]=i;
	}
	long long res=0;
	for(i=2;i<=n;++i)
	{
		if(phi[i]==i)
		{
			for(j=i;j<=n;j+=i)
				phi[j]=(phi[j]/i)*(i-1);
		}
		res+=phi[i];
	}

	// for(i=2;i<=n;++i)
	// {
	// 	cout<<i<<"  "<<phi[i]<<endl;
	// }
	return res;
}

int main()
{
	cout<<totient(1000000)<<endl;
	return 0;
}