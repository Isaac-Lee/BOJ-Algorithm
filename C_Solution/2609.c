#include <stdio.h>

int Gcd(int a, int b){
    if (b == 0){
        return a;
    } else {
        return Gcd(b, a%b);
    }
}

int main() {
    int a, b, gcd, lcm;
    scanf("%d %d", &a, &b);

    
    gcd = Gcd(a, b);
    lcm = a*b / gcd;
    printf("%d\n", gcd);
    printf("%d\n", lcm);
    return 0;
}