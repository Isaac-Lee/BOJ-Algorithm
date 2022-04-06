#include "stdio.h"

int main()
{
  int n; long memo[91];
  memo[0] = 0;
  memo[1] = 1;
  for (int i=2; i<91; i++) {
    memo[i] = memo[i-1] + memo[i-2];
  }
  scanf("%d", &n);
  printf("%ld", memo[n]);
  return 0;
}
