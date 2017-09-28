#include "iostream"

using namespace std;

struct node
{
	int value;
	node* left;
	node* right;
};

node* newnode(int data)
{
	node* x;
	x=new node();
	x->value=data;
	x->left=x->right=NULL;
	return x;
}

void insert(node** root,int x)
{
	if((*root)==NULL)
	{
		(*root)=newnode(x);
		return;
	}

	if(x<=(*root)->value)
	{
		if((*root)->left==NULL)
		{
			node* y=newnode(x);
			(*root)->left=y;
			return;
		}

		insert(&((*root)->left),x);
		return;
	}

	if((*root)->right==NULL)
	{
		node* y=newnode(x);
		(*root)->right=y;
		return;
	}

	insert(&((*root)->right),x);
	return;
}

void preorder_traversal(node* root)
{
	if (root==NULL)
		return;
	cout<<root->value<<"  ";
	preorder_traversal(root->left);
	preorder_traversal(root->right);
}

void inorder_traversal(node* root)
{
	if (root==NULL)
		return;
	inorder_traversal(root->left);
	cout<<root->value<<"  ";
	inorder_traversal(root->right);
}

void postorder_traversal(node* root)
{
	if (root==NULL)
		return;
	postorder_traversal(root->left);
	postorder_traversal(root->right);
	cout<<root->value<<"  ";
}

bool search(node* root,int x)
{
	if(root==NULL)
		return false;

	if(root->value==x)
		return true;

	if(x>root->value)
		return search(root->right,x);

	return search(root->left,x);
}

int 