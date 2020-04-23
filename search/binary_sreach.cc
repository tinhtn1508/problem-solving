#include <bits/stdc++.h>

int binary_search(int arr[], int left, int right, int x) {
    if (right >= left) {
        int mid = left + (right - left) / 2;;
        if (arr[mid] == x) return mid;
        if(arr[mid] > x) return binary_search(arr, left, mid - 1, x);
        return binary_search(arr, mid + 1, right, x);
    }
    return -1;
}

/* Execute: 
 * g++ -o main binary_sreach.cc -std=c++17
 * ./main
 */
int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int x = 7;
    int result = binary_search(arr, 0, std::size(arr), x);
    std::cout << "Index of " << x << ": " << result << std::endl;
    return 0;
}
