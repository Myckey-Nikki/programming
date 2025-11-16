//this code is efficient in terms of time but not in terms of space 
//uses extra space 
// prints the number repeated twice  
#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
     int arr[n];
     int visted[n];
for (int i = 0; i < n; i++)
{
    visted[i]=0;

    scanf("%d",&arr[i]);
}
for (int i = 0; i < n; i++)
{
   
        visted[arr[i]]+=1;
    
    
}
for (int i = 0; i < n; i++)
{
    if(visted[i]>1) printf("%d",i);
}

    return 0;
}