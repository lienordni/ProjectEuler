#include <iostream>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <fstream>
#include <ctime>
#include <map>
#include <utility>

typedef long long lien;
typedef std::vector<lien> lienvector;

std::map<lien,lienvector> Inverse_Totient;
lien e=2.7182818;

lien gcd(lien a,lien b) {
	lien r=b;
	lien s=a,q,t;
	while(r!=0){
		q=int(s/r);
		t=r;
		r=s-q*t;
		s=t;
	}
	return s;
}

lien noob_totient(lien n){
	lien count=0;
	for(lien i=1;i<n;++i){
		if(gcd(i,n)==1)
			count++;
	}
	return count;
}

void print(lienvector v)
{
	for(int i=0;i<v.size();++i)
		std::cout<<v[i]<<" ";
	std::cout<<std::endl;
}

void initialize_map()
{
	lien x=1;
	lienvector v;
	v.push_back(1);
	v.push_back(2);
	Inverse_Totient.insert(std::pair<lien,lienvector>(x,v));
}

lien power(lien a,lien b) {
	if(b==0)
		return 1;

	if(b==1)
		return a;

	lien x;
	x=power(a,b/2);

	if(b%2==0){
		return x*x;
	}

	return x*x*a;
}

std::vector<int> lienordni(lien n) { // Awesome Lienordni Function (ALF)
	if(n<2047) {
		std::vector<int> v;
		v.push_back(2);
		return v;
	};
	if(n<1373653) {
		std::vector<int> v;
		v.push_back(2);
		v.push_back(3);
		return v;
	}
	if(n<9080191) {
		std::vector<int> v;
		v.push_back(31);
		v.push_back(73);
		return v;
	}
	if(n<25326001) {
		std::vector<int> v;
		v.push_back(2);
		v.push_back(3);
		v.push_back(5);
		return v;
	}
	if(n<4759123141) {
		std::vector<int> v;
		v.push_back(2);
		v.push_back(7);
		v.push_back(61);
		return v;
	}
	if(n<1122004669633) {
		std::vector<int> v;
		v.push_back(2);
		v.push_back(13);
		v.push_back(23);
		v.push_back(1662803);
		return v;
	}
	if(n<2152302898747) {
		std::vector<int> v;
		v.push_back(2);
		v.push_back(3);
		v.push_back(5);
		v.push_back(7);
		v.push_back(11);
		return v;
	}
	if(n<3474749660383) {
		std::vector<int> v;
		v.push_back(2);
		v.push_back(3);
		v.push_back(5);
		v.push_back(7);
		v.push_back(11);
		v.push_back(13);
		return v;
	}
	if(n<341550071728321) {
		std::vector<int> v;
		v.push_back(2);
		v.push_back(3);
		v.push_back(5);
		v.push_back(7);
		v.push_back(11);
		v.push_back(13);
		v.push_back(17);
		return v;
	}
}

lien power_modulo(lien x,lien y,lien n) {
	lien z;
	if(y==0)
		return 1;
	if(y==1)
		return x%n;
	if(y%2==0){
		lien z=power_modulo(x,y/2,n);
		return (z*z)%n;
	}
	return (x*power_modulo(x,y-1,n))%n;
}

bool isPrime(lien n) {
	if(n<2)
		return false;

	if(n==2)
		return true;

	lien d=n-1;
	int s=0;
	while(d%2==0){
		d/=2;
		s++;
	}
	
	lien x;
	bool over;
	std::vector<int> list=lienordni(n);
	
	for(int i=0;i<list.size();++i) {
		x=power_modulo(list[i],d,n);
		if(x==1)
			continue;
		over=false;
		for(int r=0;r<s;++r) {
			if(x==n-1){
				over=true;
				break;
			}
			x=(x*x)%n;
		}

		if(over)
			continue;

		return false;
	}

	return true;
}

lienvector cut(lienvector v,int l,int h){
	lienvector x;
	for(int i=l;i<h;++i)
		x.push_back(v[i]);
	return x;
}

lienvector combine(lienvector l,lienvector r,char ch) {
	lienvector v;
	int i=0,j=0;

	if(ch=='d') {
		while(i<l.size() && j<r.size()){
			if(l[i]>=r[j]) {
				v.push_back(l[i]);
				i++;
			}
			else {
				v.push_back(r[j]);
				j++;
			}
		}

		while(i<l.size()){
			v.push_back(l[i]);
			i++;
		}

		while(j<r.size()){
			v.push_back(r[j]);
			j++;
		}

		return v;
	}

	if(ch=='a') {
		while(i<l.size() && j<r.size()){
			if(l[i]<=r[j]) {
				v.push_back(l[i]);
				i++;
			}
			else {
				v.push_back(r[j]);
				j++;
			}
		}

		while(i<l.size()){
			v.push_back(l[i]);
			i++;
		}

		while(j<r.size()){
			v.push_back(r[j]);
			j++;
		}

		return v;
	}

}

lienvector merge_sort(lienvector v,char ch){ // O(v.size()*log(v.size()))
	// return v;
	if(v.size()==1)
		return v;
	int mid=v.size()/2;

	lienvector left,right;
	left=cut(v,0,mid);
	right=cut(v,mid,v.size());

	left=merge_sort(left,ch);
	right=merge_sort(right,ch);

	return combine(left,right,ch);	
}

lienvector factors(lien x){ // O(x^1/2)
	lienvector v;
	for(int i=1;i<=int(sqrt(x));++i){
		if(x%i==0){
			if(i*i!=x) {
				v.push_back(i);
				v.push_back(x/i);
			}
			else
				v.push_back(i);
		}
	}

	return merge_sort(v,'d');
}

lienvector primelist(lien x){
	lienvector v=factors(x);
	lienvector p;
	for(int i=0;i<v.size();++i)
		if(isPrime(v[i]+1))
			p.push_back(v[i]+1);
	return p;
}

lien least_prime_factor(lien x) { //could be optimized
	if(isPrime(x))
		return x;
	for(lien i=2;;++i)
		if(x%i==0)
			return i;
}

lienvector inverse_totient(lien m) {
	if(Inverse_Totient.find(m)!=Inverse_Totient.end()){
		return Inverse_Totient[m];
	}

	lienvector p=primelist(m);
	lienvector final;
	lien k,c,d,x;
	lienvector temp;
	int i,j;
	for(i=0;i<p.size()-1;++i){
		k=0;
		c=m;
		while(c%p[i]==0){
			c/=p[i];
			k+=1;
		}

		for(d=1;d<k+2;++d){
			x=m/((p[i]-1)*power(p[i],d-1));
			if(x%2==1 && x>1)
				continue;
			temp.clear();
			temp=inverse_totient(x);
			for(j=0;j<temp.size();++j)  {
				if(temp[j]==1)
					final.push_back(power(p[i],d));
				else if (least_prime_factor(temp[j])>p[i])
					final.push_back(temp[j]*power(p[i],d));
			}
		}
	}

	int q=final.size();
	for(i=0;i<q;++i)
		final.push_back(2*final[i]);

	lienvector t=final;
	Inverse_Totient.insert(std::pair<lien,lienvector>(m,t));
	return t;
}

lien factorial(int n) {
	lien p=1;
	for(int i=2;i<=n;++i)
		p*=i;
	return p;
}

lienvector totient_inverse(lien m) {
	std::vector<lien> v;
	lien low=m+1;
	lien high=m*20;
	
	for(lien i=low;i<=high;++i)
	{
		if(noob_totient(i)==m)
			v.push_back(i);
	}

	return v;
}

int main(int argc,char* argv[]) {
	initialize_map();

	print(totient_inverse(576));
	print(inverse_totient(576));
	return 0;



	// clock_t start=clock();
		// print(inverse_totient(atoi(argv[1])));
		// print(inverse_totient((atoi(argv[1]))));
		// totient_inverse(atoi(argv[1]));
	// clock_t end=clock();
	lienvector v;
	lien max;
	for(lien i=1;i<=100;++i){
		v=inverse_totient(i);
		std::cout<<i<<"  "<<v[v.size()-1]<<"  "<<v[v.size()-1]/i<<std::endl;
		if(max<v[v.size()-1]/i)
			max=v[v.size()-1]/i;
	}

	// std::cout<<"Time Taken : "<<double(end-start)/CLOCKS_PER_SEC<<" s"<<std::endl;
}