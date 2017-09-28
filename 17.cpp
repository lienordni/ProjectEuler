#include<iostream>
#include<string.h>
using namespace std;

string units[20]={"\0","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"};
string tens[10]={"\0","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"};
string s=" ";
string h="hundred";
string a="and";
string word(int x)
{

	if(x==1000)
		return "one thousand";
	
	if(x<20)
		return units[x];
	
	if(x<100)
		return tens[x/10]+s+units[x%10];
	
	if(x%100==0)
		return units[x/100]+s+h;
	
	if(x%10==0)
		return units[x/100]+s+h+s+a+s+tens[(x/10)%10];
		
	if(x<1000)
		return units[x/100]+s+h+s+a+s+word(x%100);
	
}

int count(string x)
{
	int i,c=0;
	for(i=0;x[i]!='\0';++i)
		if(x[i]!=' ')
			c++;
			
	return c;
}

int main()
{
	int s=0,x;
	for(x=1;x<=100;++x)
		{
			cout<<x<<endl<<word(x)<<endl<<count(word(x))<<endl<<endl;
			s+=count(word(x));
//			getch();
		}
	cout<<s;
}
