#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    while(n > 0){
        for (int i = 2; i < n+1; i++){
            if (n%i == 0){
                n = n/i;
                printf("%d\n", i);
                break;
            }
        }
        if (n == 1){
            break;
        }
    }
    return 0;
}