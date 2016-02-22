#include <u.h>

char in(port)    { asm(LL,8); asm(BIN); }
out(char c)  { asm(LL,8); asm(PSHA); asm(POPB); asm(LI,1); asm(BOUT); }

main()
{
  char c;
  char enter = '\n';
  while (1)
  {
    c = in(0);
    if (c != -1)
    {
      out(c);
      out(enter);
      out(c);
      out(enter);
      break;
    }
  }
  asm(HALT);
}
