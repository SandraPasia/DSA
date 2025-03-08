#include <iostream>

using namespace std; 

typedef struct Node{
    string songName;
    Node *link;
}Node; 

//Node *sample = new Node;
//sample->song = "Heaven Knows by Orange and Lemon";

//cout << sample->songName <<endl;

Node *createNode(string data){
    Node *newNode = new Node;
    newNode->songName = data;
    newNode->link = NULL;
    return newNode;
}

void traverse(Node *head){ 
    Node *temp = new Node;
    temp = head; 

    cout << "My Playlist" << endl; 
    while(temp != NULL){ 
        cout << temp->songName<< "->"<<endl; 
        if(temp->link == NULL){
            cout << "NULL"<<endl;
            }
            temp = temp->link;
    }
}

Node *insertAtEnd(string data, Node *head){
    if (head == NULL){
        Node *newNode = createNode(data);
        head = newNode;
        cout << "A new node has been inserted at the End \n";
        return head;
    }
    Node *temp = new Node;
    temp = head;

    while(temp->link != NULL){
        temp = temp->link;
    }
    Node *newNode = createNode(data);
    temp->link = newNode;

    cout << "A new node has been inserted at the end \n" << endl;
    return head;
}

Node *insertAtBegging(string data, Node *head){
    Node *newNode = createNode(data);
    newNode->link = head;
    cout << "A new node has been inserted at the beginning \n" <<endl; 
    return head;
}
string insertAfter(string after, string data, Note *head){
    Node *temp = new Node;
    temp = head;

    while(temp-> )
}

int main(){
    Node *head = createNode ("Sanctuary by joji");

    head = insertAtEnd("Sunday Morning by Maroon 5", head);
    traverse(head);


    return 0;
}

