#include <stdio.h>

int main()
{
    int primo;
    int secondo;
    int risultato;
    float media;

    printf("\nInserisci il primo numero: ");
    scanf("%d", &primo);

    printf("\nInserisci il secondo Nnumero: ");
    scanf("%d", &secondo);

    risultato = primo * secondo;
    media = (primo + secondo) / 2.0;

    printf("\n%d * %d = %d", primo, secondo, risultato);
    printf("\nMedia aritmetica tra i due numeri digitati: %.1f", media);

    return 0;
}