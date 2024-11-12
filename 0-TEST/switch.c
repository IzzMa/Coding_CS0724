#include <stdio.h>

int main()
{
    int scelta;
    printf("\nSalve, qui centro Scassati:\n1 per conoscere le offerte\n2 per parlare con un bravo\n3 se vuoi una tanica di benzina\nPrego, inserisca: ");
    scanf("%d", &scelta);
    switch (scelta)
    {
    case 1:
        printf("\nPer te nello specifico non abbiamo offerte!");
        break;

    case 2:
        printf("\nStai troppo male anche per uno bravo!");
        break;

    case 3:
        printf("\nSiamo in spending review, compratela!");
        break;
    default:
        printf("\nBravo, non rompere, CIAO!");
        break;
    }
    return 0;
}
