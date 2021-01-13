#include <stdio.h>

int main()
{
    int i,n;
    scanf("%d", &n);
    int A[n];
    for(i=1;i<=n;i++){
        scanf("%d", &A[i]);
    }
    for(i=n;i>0;i--){
        printf("%d ", A[i]);
    }
