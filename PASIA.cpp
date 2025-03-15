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
            cout << "NULL" <<endl;
            cout << "Blue by yung kai" <<endl;
            cout << "Get You by Daniel Caesar" <<endl;
            cout << "You by Jacquees" <<endl;
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

Node *insertAtBeginning(string data, Node *head){
    Node *newNode = createNode(data);
    newNode->link = head;
    cout << "A new node has been inserted at the beginning \n" <<endl; 
    return head;
}

string insertAfter(string after, string data, Node *head){
    Node *temp = new Node;
    temp = head;

    while(temp->songName.compare(after) != 0){
        if(temp == NULL){
            return "No such song exist, please try again later."; 
        }
        temp = temp->link;
  } 
Node *newNode = createNode(data);
newNode->link = temp->link; 
temp->link = newNode; 
return "An new node has been addd after " + after + "\n";
}
string deleteAtEnd(Node *head){
    if (head == NULL) {
        return "The linked list is empty \n";
    }
    if (head->link == NULL) {
        delete head;
        return "The head has been deleted";
    }
    Node *temp = head;
    Node *prev = NULL;

    while (temp->link != NULL) {
        prev = temp;
        temp = temp->link;
    }

    prev->link = NULL;
    delete temp;
    return "A node has been deleted at the end";
    return "A node has been deleted at the end \n";
}
Node *deleteFromBeginning(Node *head){
    if(head == NULL){
        cout << "The linked list is empty \n";
        return NULL;
    }
    if(head->link == NULL){
        delete head;
    }
    head = head->link;
    cout << "A node has been delete from the beginning \n" << endl;
    return head;
}
Node *deleteFromGivenNode(string givenNode, Node *head){
    if(head == NULL){
        cout << "The linked list is empty. \n" << endl;
        return NULL;
    }
    if(head->songName.compare(givenNode) == 0){
        head = deleteFromBeginning(head);
        cout << "The Node " + givenNode + " has been deleted. \n" << endl;
        return head; 
    }
    Node *temp = new Node; 
    Node *next = new Node;
    temp = head;
    next = temp->link;

    while(next->songName.compare(givenNode) != 0){
        if(temp == NULL){
            cout << "No such node exist. \n" << endl;
            return head;
        }
        next = next->link;
        temp = temp->link;
    }
    temp->link = next->link;
    cout << "The Node " + givenNode + " has been deleted. \n" << endl;
    return head;
}

int main(){
     Node *head = createNode("Sanctuary by Joji");

    head = insertAtEnd("Blue by yung kai", head);
    head = insertAtEnd("Get You by Daniel Caesar", head);
    head = insertAtEnd("You by Jacquees", head);
    head = insertAtBeginning("Life Puzzle by Arthur Nery", head);
    head = insertAtBeginning("Unang Sayaw by NOBITA", head);
    head = insertAtBeginning("The Day You Said Goodnight by Hale", head);
    head = insertAtBeginning("Double take by Dhruv", head);

    

    string result = insertAfter("Double take by Dhruv","You'll be safe here", head);

cout << result;
string result1 = insertAfter("Get You by Daniel Caesar","Sleep Tonight", head);
cout << result1;

string result2 = insertAfter("Blue by yung kai","Pano", head);
cout << result2;



string End = deleteAtEnd(head);
cout << End;

head = deleteFromBeginning(head);

head = deleteFromGivenNode("Double take by Dhruv", head);

traverse(head);
return 0;
}
