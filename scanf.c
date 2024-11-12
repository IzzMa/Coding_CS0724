#include <stdio.h>

int main()
{
    int primo;
    int secondo;
    int risultatoA;
    int risultatoB;
    int risultatoC;
    int risultatoD;

    printf("Inserisci Primo Numero: ");
    scanf("%d", &primo);

    printf("Inserisci Secondo Numero: ");
    scanf("%d", &secondo);

    risultatoA = primo+secondo;
    risultatoB = primo-secondo;
    risultatoC = primo*secondo;
    risultatoD = primo/secondo;

    printf("\n%d + %d = %d", primo, secondo, risultatoA);
    printf("\n%d - %d = %d", primo, secondo, risultatoB);
    printf("\n%d * %d = %d", primo, secondo, risultatoC);
    printf("\n%d / %d = %d", primo, secondo, risultatoD);

    return 0;
}