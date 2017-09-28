#include "iostream"
#include "fstream"
#include "ctype.h"
using namespace std;

/*
High Card : 100
One Pair : 200
Two Pair : 300
Three of a kind : 400
Straight : 500
Full House : 700
Four of a kind : 800
*/

class card
{
public:
	int value;
	char suit;
};

void sort(int a[5])
{
	int i,j,t;
	for(i=0;i<5;++i)
		for(j=0;j<5-i-1;++j)
			if(a[j+1]<a[j])
			{
				t=a[j+1];
				a[j+1]=a[j];
				a[j]=t;
			}
}

int eight(card a[5])
{
	int i,j,m;
	int v[5];
	for(i=0;i<5;++i)
	{
		v[i]=a[i].value;
	}

	sort(v);
	bool f=true;
	for(i=2;i<5;++i)
	{
		if(v[i]!=v[1])
			f=false;
	}

	if(f)
		return 800+v[1];

	for(i=1;i<4;++i)
	{
		if(v[i]!=v[0])
			f=true;
	}

	if(!f)
		return 800+v[0];
	return 0;


}

int hand(card a[5])
{
	int i,j,m;

	for(i=1;i<5;++i)
		if(a[i].suit!=a[0].suit)
			goto not_flush;

	for(i=1;i<5;++i)
	{
		if(a[i].value-a[0].value!=i)
			{
				m=0;
				for(j=0;j<5;++j)
					if(a[j].value>m)
						m=a[j].value;

				return 600+m;
			}
	}
	
	if(a[0].value==10)
		return 1000;

	m=0;
	for(j=0;j<5;++j)
		if(a[j].value>m)
			m=a[j].value;
	return 900+m;
	
	not_flush:;


	
}

int main()
{
	int a[5]={3,6,2,7,5};
	int i;
	fstream fin("./54.txt",ios::in);
	char ch[2];
	card h1[5],h2[5];
	while(!fin.eof())
	{
		for(i=0;i<5;++i)
		{
			fin>>ch;
			if(isnum(ch[0]))
				h1[i].value=ch[0];
			else
			{
				switch(ch[0])
				{
					case 'T' :  h1[i].value=10;
								break;
					case 'J' :  h1[i].value=11;
								break;
					case 'Q' :  h1[i].value=12;
								break;
					case 'K' :  h1[i].value=13;
								break;
					case 'A' :  h1[i].value=14;
								break;
				}
			}

			h1[i].suit=ch[1]
		}
		
		for(i=0;i<5;++i)
		{
			fin>>ch;
			if(isnum(ch[0]))
				h2[i].value=ch[0];
			else
			{
				switch(ch[0])
				{
					case 'T' :  h2[i].value=10;
								break;
					case 'J' :  h2[i].value=11;
								break;
					case 'Q' :  h2[i].value=12;
								break;
					case 'K' :  h2[i].value=13;
								break;
					case 'A' :  h2[i].value=14;
								break;
				}
			}

			h2[i].suit=ch[1]
		}

		
	}
}
