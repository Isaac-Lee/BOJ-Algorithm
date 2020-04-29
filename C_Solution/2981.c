#include <stdio.h>

int array_max(int a[], int size) {
    int max = a[0];
    for(int i=1; i<size; i++) if(a[i]>max) max=a[i];
    return max;
}


int main() {
    int n;
    scanf("%d", &n);

    int[n] num;
    int[n] answer;

    for (int i = 0; i < n; i++) {
    	int k;
    	scanf("%d", &k);
    	num[i] = k;
    }

    int max = array_max(num, n);
    for (int j = 0; j < max; j++){
    	for (int k = 0; k < n; k++){
    		answer[i] = answer[i]%
    	}
    }
    return 0;
}