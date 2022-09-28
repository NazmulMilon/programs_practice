#include<bits/stdc++.h>
using namespace std;

void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(int arr[], int n, int current)
{
    int largest = current;
    int leftchild = 2*current +1;
    int rightchild = 2*current+2;

    if(leftchild < n && arr[leftchild]>arr[largest])
    {
        largest = leftchild;
    }
    if(rightchild < n && arr[rightchild]> arr[largest])
    {
        largest = rightchild;
    }

    if(largest != current)
    {
        swap(arr[current], arr[largest]);
        heapify(arr, n, largest);
    }
}

void printarray(int arr[], int size)
{
    cout<<endl;
    for(int i=0; i<size; i++)
        {
            cout<<arr[i]<<" ";
        }
        cout<<endl;
}

void heapsort(int arr[], int size)
{
    for(int i=size-1; i>0; i--)
    {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

int main()
{
    int n;
    cin>>n;

    int arr[n];
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

    cout<<"Before Heapify: "<<endl;
    printarray(arr, n);

    //heapify
    int nonleafstart = (n/2)-1;

    for(int i=nonleafstart; i>=0; i--)
    {
        heapify(arr, n, i);
    }

    cout<<" After Heapify: "<<endl;
    printarray(arr, n);

    cout<<endl;
    heapsort(arr, n);
    cout<<"After The heap Sort" <<endl;
    printarray(arr, n);
}
