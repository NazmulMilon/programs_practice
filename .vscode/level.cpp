#include<bits/stdc++.h>
using namespace std;

class Node
{
public:
    int val;
    Node* leftchild;
    Node* rightchild;
    Node(int val)
    {
        this->val=val;
        this->leftchild=NULL;
        this->rightchild=NULL;
    }
};

void print(Node* root)
{
    if(root==NULL) return;
    print(root->leftchild);
    cout<<root->val<<" ";
    //cnt=cnt+1;
    print(root->rightchild);

}

void inorder_traverse(Node* root, int chk)
{
    if(root==NULL)
    {
        return;
    }
    inorder_traverse(root->leftchild, chk);
    chk=(root->val);
    inorder_traverse(root->rightchild, chk);
}

void preorder_traverse(Node* root, string &chk)
{
    if(root==NULL)
    {
        return;
    }
    chk=chk+to_string(root->val);
    preorder_traverse(root->leftchild, chk);
    preorder_traverse(root->rightchild, chk);

}

void postorder_traverse(Node* root, string &chk)
{
    if(root==NULL)
    {
        return;
    }
    postorder_traverse(root->leftchild, chk);
    postorder_traverse(root->rightchild, chk);
    chk=chk+to_string(root->val);
}

void printArr(int arr[], int n)
{
    for (int i = 1; i <=n; i++)
        cout << arr[i] <<" ";
}



int main()
{

    int a;
    cin>>a;

    Node *root = new Node(a);

    queue<Node* > q;
    q.push(root);
    while(!q.empty())
    {
        Node* presentRoot=q.front();
        q.pop();
        int x,y;
        cin>>x>>y;
        Node* n1=NULL;
        Node* n2=NULL;
        if(x!= -1) {n1=new Node(x);}
        if(y!=-1) {n2 = new Node(y);}
        presentRoot->leftchild = n1;
        presentRoot->rightchild= n2;

        if(n1 != NULL) {q.push(n1);}
        if(n2 != NULL) {q.push(n2);}

    }
    int k, cnt;
    cin>>k;


    int v[100];
    print(root);
    cnt++;
    cout<<cnt<<endl;

    for(int i=0; i<cnt; i++)
    {
        
    }
    return 0;
}

/*
1
1 1
2 2 2 2
-1 -1 -1 -1 -1 -1 -1 -1


0
1 2
3 -1 -1 4
-1 -1 -1 -1


15
11 26
8 12 20 30
6 9 -1 14 -1 -1 -1 35
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1

1
2 3
-1 -1 -1 -1

*/