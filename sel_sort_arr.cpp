#include <iostream>
#include <cstdlib>
#include <ctime>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; ++i) {
        int min_idx = i;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        std::swap(arr[i], arr[min_idx]);
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    const int size = 1000;
    int arr[size];

    std::srand(std::time(0));
    for (int i = 0; i < size; ++i) {
        arr[i] = std::rand() % 1000;
    }

    std::cout << "Unsorted array: ";
    printArray(arr, size);

    selectionSort(arr, size);

    std::cout << "Sorted array: ";
    printArray(arr, size);

    return 0;
}