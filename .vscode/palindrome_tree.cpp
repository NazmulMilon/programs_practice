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
    //cout<<root->val<<endl;
    print(root->rightchild);

}

void inorder_traverse(Node* root, string &chk)
{
    if(root==NULL)
    {
        return;
    }
    inorder_traverse(root->leftchild, chk);
    chk=chk+to_string(root->val);
    inorder_traverse(root->rightchild, chk);
}

void printPaths(Node* root);
void printPathsRecur(Node* root, int path[], int pathLen);
void printArray(int ints[], int len);

int cnt=0;
int isPalindrome(string S)
{
    string P = S;
 
    reverse(P.begin(), P.end());
 
    if (S == P) {
        return cnt+1;
    }
    
    else {
        return cnt+0;
    }
}

void printPaths(Node* root)
{
    int path[1000];
    printPathsRecur(root, path, 0);
}

void printPathsRecur(Node* root, int path[], int pathLen)
{
    if (root == NULL)
        return;

    path[pathLen] = root->val;
    pathLen++;

    if (root->leftchild == NULL && root->rightchild == NULL)
    {
        printArray(path, pathLen);
    }
    else
    {
        printPathsRecur(root->leftchild, path, pathLen);
        printPathsRecur(root->rightchild, path, pathLen);
    }
}


void printArray(int ints[], int len)
{
    int i;
    string str="";
    for (i = 0; i < len; i++)
    {
        //cout << char(ints[i]);
        str+=char(ints[i]);
    }
    //cout<<str<<endl;
    //cout<<" p: "<<isPalindrome(str)<<" : al"<<endl;
    cnt=isPalindrome(str);
    //cout<<cnt<<endl;
    //if(isPalindrome(str)) cnt++;
}

int main()
{
    string s;
    cin>>s;

    int a;
    cin>>a;

    Node *root = new Node(s[a]);

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
        if(x!= -1) {n1=new Node(s[x]);}
        if(y!=-1) {n2 = new Node(s[y]);}
        presentRoot->leftchild = n1;
        presentRoot->rightchild= n2;

        if(n1 != NULL) {q.push(n1);}
        if(n2 != NULL) {q.push(n2);}

    }

    //cout<<"print root to leaf: "<<endl;
    printPaths(root);

    //cout<<endl;
    print(root);
    string str="";
    inorder_traverse(root, str);
    //cout<<"Inorder Traverse: "<<str<<endl;
    cout<<cnt<<endl;


    return 0;
}


/*
A
B C
A -1 -1 A
-1 -1 -1 -1


ABCDE
0
1 2
3 -1 -1 4
-1 -1 -1 -1


ABCAA
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