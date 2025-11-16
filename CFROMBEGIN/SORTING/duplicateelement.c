
// prints the arr[i],prints i's in which are repeated
//efficient in space 
#include <stdio.h>


int main() {
    
    int n;
    scanf("%d", &n);

    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }


    for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
         if (arr[i] == arr[j]) {
      printf("%d %d\n", i, j);
        }
        }
    }

    return 0;
}