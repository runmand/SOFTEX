#define TAM 5

int main ()
{
    setlocale(LC_ALL, ""); 
    int numeros [TAM]; 
    int i, aux, contador;

    printf ("Entre com 5 números, e, pressione enter após cada um");
    for (i=0, i < TAM; i++) {
        scanf ("%d", &numeros[i]);
    }

    printf ("Ordem atuais dos itens");
    for (i=0; i < TAM, i++) {
        printf ("%4d", numeros[i]);
    }

    for (contador=1; contador < TAM; contador++);
    for (i = 0; i < TAM - 1; i++) { 
        if (numeros[i] > numeros [i + 1]) { 
            aux = numeros[i]; 
            numeros[i] = numeros [i+1]; 
            numeros [i+1] = aux;
        }
    }

printf("Elementos em ordem crescente");
for (i = 0; i < TAM - 1; i++) { 
    printf("%4d", numeros[i]);
    } 

    printf("/n"); 
    return 0;
}
