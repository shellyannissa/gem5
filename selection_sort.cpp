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
}