#include <stdio.h>
#include <stdlib.h>

int readint(int* dest){
  char c;
  int rv = 0;
  int nread=0;
  while((c=getchar())!=EOF&&(c >= '0')&&(c <= '9')){
    nread++;
    rv *= 10;
    rv += c - '0';
  }
  ungetc(c, stdin);
  if(c==EOF) return -1;
  *dest=rv;
  return nread;
}

unsigned long int psum(int len, int i)
{
  char c;
  unsigned long int rv=0;
  for(;0<len;len--){
    c = getchar();
    if(c == '('){
      int dread = 0;
      int nlen;
      dread += readint(&nlen);
      getchar();dread++;
      int ni;
      dread += readint(&ni);
      getchar();dread++;
      rv += psum(nlen, ni) * i;
      len -= nlen+dread;
    }else{rv += i;}
  }
  return rv;
}

int main(int argc, char** argv)
{
  unsigned long int count = 0;
  char c;
  while((c=getchar())!= EOF){
    if(c=='('){
      int len;
      readint(&len);
      getchar();//discard x
      int i;
      readint(&i);
      getchar();//discard )
      count += psum(len, i);
    }else{count++;}
  }
  printf("%lu\n", count-1); //don't count eof
  return 0;
}
