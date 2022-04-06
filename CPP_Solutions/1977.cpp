#include <iostream>

int main() {
  int n, m, sum = 0, min=10001;
  std::cin >> m >> n;
  for (int i = 1; i < 101; i++) {
    if (i*i > n) break;
    if (i*i >= m) {
      sum += i*i;
      if (i*i < min) min = i*i;
    }
  }

  if (sum > 0) {
    std::cout << sum << std::endl;
  }

  if (min != 10001) {
    std::cout << min << std::endl;
  } else {
    std::cout << -1 << std::endl;
  }

  return 0;
}
