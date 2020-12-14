#include <algorithm>
#include <iostream>
#include <cstring>
// 9223372036854775807 9223372036854775808

int to_int(char s) {
  if (s == '1') {
    return 1;
  } else if (s == '2') {
    return 2;
  } else if (s == '3') {
    return 3;
  } else if (s == '4') {
    return 4;
  } else if (s == '5') {
    return 5;
  } else if (s == '6') {
    return 6;
  } else if (s == '7') {
    return 7;
  } else if (s == '8') {
    return 8;
  } else if (s == '9') {
    return 9;
  } else if (s == '0') {
    return 0;
  }
}

int main() {
  std::string num1, num2, result;
  std::cin >> num1 >> num2;
  
  int n1Len, n2Len, N;
  n1Len = num1.length();
  n2Len = num2.length();

  reverse(num1.begin(), num1.end());
  reverse(num2.begin(), num2.end());

  std::cout << n1Len << std::endl;
  std::cout << n2Len << std::endl;

  N = (n1Len > n2Len) ? n1Len : n2Len;

  char n1, n2;
  int carry=0, a, b, sum;
  for (int i = 0; i < N+1; i++) {
    if (i == N) {
      if (carry > 0) {
        sum = carry;
      } else {
        break;
      }
    } else if (i > n1Len-1) {
      b = to_int(num2[i]);
      sum = b + carry;
      carry = 0;
    } else if (i > n2Len-1) {
      a = to_int(num1[i]);
      sum = a + carry;
      carry = 0;
    } else {
      a = to_int(num1[i]);
      b = to_int(num2[i]);
      sum = a + b + carry;
      carry = 0;
    }
    if (sum >= 10) {
        sum -= 10;
        carry = 1;
    }
    std::string s = std::to_string(sum);
    std::cout << s << std::endl;
    result.insert(0, s);
  }
  std::cout << result;
  return 0;
}
