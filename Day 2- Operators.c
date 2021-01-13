#include <stdio.h>
#include <math.h>

int main()
{
    float cost, tip, tax, sum;
    int finalcost;
    scanf("%f %f %f",&cost, &tip, &tax);
    
    tip = (tip/100)*cost;
    tax = (tax/100)*cost;
    sum = tip + tax + cost;
    
  finalcost = round(sum);
   printf("%d", finalcost);
    return 0;
}