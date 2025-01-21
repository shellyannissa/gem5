#include <bits/stdc++.h>
using namespace std;

// Node class
class Node {
public:
    int data;
    Node* next;
};

// Insert a new node at the beginning
void push(Node** head_ref, int new_data) {
    Node* new_node = new Node();
    new_node->data = new_data;
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

// Insert a new node after a given node
void insertAfter(Node* prev_node, int new_data) {
    if (prev_node == NULL) {
        cout << "The given previous node cannot be NULL";
        return;
    }
    Node* new_node = new Node();
    new_node->data = new_data;
    new_node->next = prev_node->next;
    prev_node->next = new_node;
}

// Insert a new node at the end
void append(Node** head_ref, int new_data) {
    Node* new_node = new Node();
    Node* last = *head_ref;
    new_node->data = new_data;
    new_node->next = NULL;
    if (*head_ref == NULL) {
        *head_ref = new_node;
        return;
    }
    while (last->next != NULL) {
        last = last->next;
    }
    last->next = new_node;
    return;
}

// Delete a node
void deleteNode(Node** head_ref, int key) {
    Node* temp = *head_ref;
    Node* prev = NULL;
    if (temp != NULL && temp->data == key) {
        *head_ref = temp->next;
        delete temp;
        return;
    }
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) {
        return;
    }
    prev->next = temp->next;
    delete temp;
}

// generate random linked list of size n
void generateRandomLinkedList(Node** head_ref, int n) {
    for (int i = 0; i < n; i++) {
        append(head_ref, rand() % 100000);
    }
}

int main() {
    // Seed the random number generator
    srand(time(0));

    // Generate a random linked list
    int n = 1000;
    Node* head = NULL;
    generateRandomLinkedList(&head, n);

    // random operations
    for (int i = 0; i < n * 300; i++) {
        int operation = rand() % 4;
        int data = rand() % 100000;
        switch (operation) {
            case 0:
                push(&head, data);
                break;
            case 1:
                insertAfter(head->next, data);
                break;
            case 2:
                append(&head, data);
                break;
            case 3:
                deleteNode(&head, data);
                break;
        }
    }

    return 0;
}