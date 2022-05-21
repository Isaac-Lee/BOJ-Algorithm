#include <iostream>

int main(void){
  int n, r;
  std::cin >> n >> r;
  
  unsigned long long Combination[1000000][1000000] = {};
  
  Combination[1][0] = 1;    
  Combination[1][1] = 1;
  for (int i = 2; i <= n; i++) {
    Combination[i][0] = 1;
    for (int j = 1; j <= r; j++) {
      Combination[i][j] = Combination[i - 1][j - 1] + Combination[i - 1][j];
    }
  }

  std::cout << Combination[n][r] << std::endl;
  return 0;
}