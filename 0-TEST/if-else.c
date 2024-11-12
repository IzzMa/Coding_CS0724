#include <stdio.h>

int main()
{
    int primo;
    int secondo;
    float risultato;

    printf("Inserisci Primo Numero: ");
    scanf("%d", &primo);

    printf("Inserisci Secondo Numero: ");
    scanf("%d", &secondo);

    if (secondo != 0)
    {
        risultato = (float)primo / secondo * 100;  
        printf("\n%d è il %.2f%% di %d\n", primo, risultato, secondo);

        if (risultato < 50)
        {
            printf("Male, Malissimo!\n");
        }
        else if (risultato >= 50 && risultato <= 75)
        {
            printf("Bravo ma non troppo!\n");
        }
        else if (risultato > 75 && risultato <= 100)
        {
            printf("Ohhhh, ora ci siamo quasi!\n");
        }
        else
        {
            printf("MA GNI FI CO!\n");
        }
    }
    else
    {
        printf("Errore: Divisione per zero non consentita.\n");
    }

    return 0;
}