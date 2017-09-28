#include <iostream>
#include <fstream>
#include <limits>
#include <string>

using namespace std;

int main()
{
	fstream file("./70.txt",ios::in);
	char s[100],a[9],b[9];

	int i=0;
	while(!file.eof())
	{
		if(file.tellg()==-1)
			break;
		file.getline(a,' ');
		file.getline(b,' ');
		file.ignore();
		file.getline(s,20);
		cout<<a<<"  "<<b<<"  "<<s<<endl;
	}
	// while(file)
	// {
	// 	file>>a;
	// 	file>>b;
	// 	file.ignore('\n');
	// 	cout<<a<<"  "<<b<<endl;
	// }
}