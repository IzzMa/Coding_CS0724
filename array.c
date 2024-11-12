#include <stdio.h>

int main()
{
    int numeri [5];
    numeri[0] = 1;
    numeri[1] = 4;
    numeri[2] = 89;
    printf("0x%x = %d\n", &numeri[2], numeri[2]);

    int anum[] = {1,4,3,57,6,3};
    printf("0x%x = %d\n", &anum[4], anum[4]);

    float dec[] = {1.5, .75, 3.14};
    printf("0x%x = %f\n", &dec[0], dec[0]);

    return 0;
}