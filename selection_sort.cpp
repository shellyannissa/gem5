#include <iostream>
#include <cstdlib>
#include <ctime>

struct Node {
    int data;
    Node* next;
};

void append(Node** head_ref, int new_data) {
    Node* new_node = new Node();
    Node* last = *head_ref;
    new_node->data = new_data;
    new_node->next = nullptr;
    if (*head_ref == nullptr) {
        *head_ref = new_node;
        return;
    }
    while (last->next != nullptr) {
        last = last->next;
    }
    last->next = new_node;
}

void selectionSort(Node* head) {
    Node* temp = head;
    while (temp) {
        Node* min = temp;
        Node* r = temp->next;
        while (r) {
            if (min->data > r->data) {
                min = r;
            }
            r = r->next;
        }
        std::swap(temp->data, min->data);
        temp = temp->next;
    }
}

void printList(Node* node) {
    while (node != nullptr) {
        std::cout << node->data << " ";
        node = node->next;
    }
    std::cout << std::endl;
}

int main() {
    Node* head = nullptr;
    std::srand(std::time(0));
    for (int i = 0; i < 10; ++i) {
        append(&head, std::rand() % 10000);
    }

    std::cout << "Unsorted list: ";
    printList(head);

    selectionSort(head);

    std::cout << "Sorted list: ";
    printList(head);

    return 0;
}