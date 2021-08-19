#include <stdio.h>
void convert(int n){
    if(n<=0) return;
    else{
        convert(n/2);
        printf("%d", n%2);
    }
}

int main() {
   convert(5);
   return 0;
}
