#include <stdio.h>

int main() {
	int a, b;

	while (a!=0 && b!=0){
		scanf("%d %d", &a, &b);
		printf("%d\n", a+b);
	}

	return 0;
}