#include <bits/stdc++.h>
using namespace std;

// selection sort function
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]);
    }
}


// generate random array of size n
void generateRandomArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 100;
    }
}

// print array
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}


int main() {
    // Seed the random number generator
    srand(time(0));

    // Generate a random array of size 10
    int n = 100000;
    int arr[n];
    generateRandomArray(arr, n);

    // Print the unsorted array
    // cout << "Unsorted array: ";
    // printArray(arr, n);

    // Sort the array using selection sort
    selectionSort(arr, n);

    // Print the sorted array
    // cout << "Sorted array: ";
    // printArray(arr, n);

    return 0;
}#include <iostream>
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
    for (int i = 0; i < 100; ++i) {
        append(&head, std::rand() % 1000);
    }

    std::cout << "Unsorted list: ";
    printList(head);

    selectionSort(head);

    std::cout << "Sorted list: ";
    printList(head);

    return 0;
}