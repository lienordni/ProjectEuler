#include <iostream>
#include <fstream>
#include "../AVL/avl.h"
#include <vector>

const int size=80;

void fuck() {
	std::cout<<"lien"<<std::endl;
}

int numbers[size][size];

struct leaf{
	int i;
	int j;
	int minsum;
	bool visited;
	std::vector<leaf> neighbours;
	void findneighbours();

	leaf();
	void set(int i, int j);

	void add(int x);

	void operator=(leaf z);
	bool operator==(leaf z);
	bool operator<(leaf z);
	bool operator>(leaf z);

	friend std::ostream &operator<<(std::ostream &output, const leaf &D) { 
		output<<D.i<<" "<<D.j<<" "<<numbers[D.i][D.j]<<" "<<D.minsum;
		return output;            
	}

	leaf up();
	leaf down();
	leaf right();
	leaf left();

} array[size][size];

bool outside(int i,int j){
	if(i<0 || j<0 || i>=size || j>=size)
		return true;
	return false;
}

leaf::leaf() {
	minsum=1e9;
	visited=false;
}

void leaf::set(int x, int y) {
	i=x;
	j=y;
	minsum=1e9;
	visited=false;
}

void leaf::add(int x) {
	int n=(x+numbers[i][j]);
	minsum=(n<minsum)?(n):(minsum);
}

void leaf::operator=(leaf z) {
	i=z.i;
	j=z.j;
	minsum=z.minsum;
	visited=z.visited;
}

bool leaf::operator==(leaf z) {
	return ((i==z.i) && (j==z.j));
}

bool leaf::operator<(leaf z) {
	return minsum<z.minsum;
}

bool leaf::operator>(leaf z) {
	return minsum>z.minsum;
}

leaf leaf::up(){
	return array[i-1][j];
}

leaf leaf::down(){
	return array[i+1][j];
}

leaf leaf::right(){
	return array[i][j+1];
}

leaf leaf::left(){
	return array[i][j-1];
}

void leaf::findneighbours() {
	if(!outside(i-1,j))
		if(!up().visited)
			neighbours.push_back(up());

	if(!outside(i+1,j))
		if(!down().visited)
			neighbours.push_back(down());

	if(!outside(i,j-1))
		if(!left().visited)
			neighbours.push_back(left());

	if(!outside(i,j+1))
		if(!right().visited)
			neighbours.push_back(right());


}

avl_tree<leaf> Q;

void burn() {
	leaf top;

	// while(true) {

		top=Q.min();

		std::cout<<"____"<<top<<"____\n";

		if(top.i==size-1 && top.j==size-1){
			std::cout<<top.minsum<<std::endl;
			return;
		}

		array[top.i][top.j].visited=true;
		top.findneighbours();

		int z;

		Q.removemin();
		// std::cout<<"\nQueue...\n";
		// Q.print();
		// std::cout<<"############\n\n";
		for(z=0;z<top.neighbours.size();++z) {
			top.neighbours[z].add(top.minsum);
			// std::cout<<"    "<<top.neighbours[z]<<'\n';
			Q.insert(top.neighbours[z]);
		}


	// int i, j;

	// for(i=0;i<5;++i){
	// 	for(j=0;j<5;++j){
	// 		std::cout<<array[i][j].visited<<" ";
	// 	}
	// 	std::cout<<"\n";
	// }

	// std::cin.get();
	burn();
	// }
}

int main() {
	int i,j;

#include "83.3.txt"



	for(int i=0;i<size;++i) {
		for(j=0;j<size;++j) {
			array[i][j].set(i,j);
		}
	}

	array[0][0].minsum=numbers[0][0];
	Q.insert(array[0][0]);

	burn();
}