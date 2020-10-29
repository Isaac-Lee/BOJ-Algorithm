#include <stdio.h>

long long pow(long long a, long long b){
	long long answer = a;
	for (int i = 0; i < b; i++) {
		answer *= a;
	}
	return answer;
}

int main() {
	long long a,b,c;
	scanf("%d %d %d", &a, &b, &c);
	printf("%lf\n", pow(a,b)%c);
}