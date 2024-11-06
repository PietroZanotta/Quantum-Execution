#include <stdio.h>

int doStuff(int a)
{
  printf("%d\n", a);
}

int main()
{
  int i;
  int x;
  i = 5;
  {
    x = i * 3;
    doStuff(x);
  }
  i = 4;
  {
    x = i * 3;
    doStuff(x);
  }
  i = 3;
  {
    x = i * 3;
    doStuff(x);
  }
  i = 2;
  {
    x = i * 3;
    doStuff(x);
  }
  return 0;
}