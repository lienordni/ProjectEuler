#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <vector>

typedef long long lien;

void print(std::vector<lien> v)
{
	for(int i=0;i<v.size();++i)
		std::cout<<v[i]<<" ";
	std::cout<<std::endl;
}

bool palindrome(lien x)
{
	std::vector<lien> v;
	lien c=x;

	while(c)
	{
		// std::cout<<
		v.push_back(c%10);
		c/=10;
	}
	// return true;
	// prin	t(v);

	for(int i=0;i<v.size()/2;++i)
	{
		if(v[i]!=v[v.size()-i-1])
			return false;
	}

	return true;
}

int main(int argc, char* argv[])
{
	lien limit=atoll(argv[1]);
	int start,end;
	lien sum;
	lien ssum=0;
	// bool that;
	std::vector<lien> lienordni;
	for(start=1;start<=int(sqrt(limit))-1;++start)
	{
		// that=true;
		sum=start*start;
		for(end=start+1;end<=int(sqrt(limit));++end)
		{
			sum+=end*end;
			if(sum>limit){
				// that=false;
				break;
			}
			if(palindrome(sum)){
				std::cout<<start<<"  "<<end<<"  "<<sum<<std::endl;
				lienordni.push_back(sum);
				// ssum+=sum;

			}
		}

	}

	print(lienordni);
}