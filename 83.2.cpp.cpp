#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	fstream one("83.txt", ios::in);
	fstream two("83.2.txt", ios::in);

	std::string a,b;

	while(two){
		one>>a;
		two>>b;

		cout<<a<<endl;
		cout<<b<<endl<<endl;
	}
}