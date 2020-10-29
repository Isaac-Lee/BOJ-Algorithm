#include <stdio.h>

long jos(long n, long k) {
	if (n == 1){
		return 0;
	}
	return (jos(n-1 ,k) + k)%n;
}

int main() {
	long n, k;
	scanf("%ld %ld", &n, &k);
	printf("%ld\n", jos(n, k)+1);
	return 0;
}