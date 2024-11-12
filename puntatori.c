#include <stdio.h>

void scriviVettore(int *ptr)
{
    for(int i = 0; i < 10; i++) {
        printf("\nInserisci n[%d]: ", i);
        scanf("%d", ptr);
        ptr++;
    }
}

void leggiVettore(int *ptr)
{
    for(int i = 0; i < 10; i++) {
        printf("\nElemento n[%d] = %d (zona memoria %p)", i, *ptr, (void*)ptr);
        ptr++;
    }
}

int main()
{
    int n[10] = {0};
    int *n_ptr;

    n_ptr = &n[0];

    scriviVettore(n_ptr);
    leggiVettore(n_ptr);

    return 0;
}