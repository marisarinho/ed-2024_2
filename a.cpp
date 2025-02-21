#include <bits/stdc++.h>

using namespace std;

//preferimos long long doq int

int main(){
    int n; // -10*9 ate 10*9
    long long l; //-10*18 a 10*18
    float f; // -10*9 a 10*9, 9 casas ontando com as decimais(maoo usar)
    double d; //-10*18 a 10*18 casas contando as decimais
    char c; //caractere usando aspas simples
    string s; //sequencia de caracteres
    bool b; //true ou false

    //isso eh o input
    cin >> n >> l >> d;
    cin >> l;
    cin >> n;

    //isso eh o prinit
    cout << "";
    cout << "texto aqui: " << n << "\n";
    // \n eh tipo um print vazio, pra quebrar linha (\n tem em python tbm) é so a quebra de linha
    cout << "esse aqiueh o l: " << n << "\n"; // não pode concatenar inteiro com string
     
    if(b){
        cout << "entrou no if\n";
        // > < == >= <= -> exatamente igual
        // !=diferente
        //!b -> not b
        // and ou &&
        //or ou ||
        
    }else if(n < l){
        cout << "entrou no else if\n";
    }else{
        cout << "se nao\n";
    }

    // olha so, vc declarou la em cima como bool e agora atribuiu como inteiro...
    int x = 100, y = 30, z = 40;
    int soma = x+y+z;
    int multi = x*y*z; //cuidado com limite da variavel
    int subtracao = x-y-z;

    //o unico que tem diferenças
    //depende do resultado dela
    double divisao = x / y; //divisao com casas decimais(resto)
    int resto = x%y; //mesmacoisa
    int divisaoInteira = (x - (x%y)) / y;
    
    //arredondando p cima e p baixo
    int divisaoInteira2 = ceil(x/y);
    int divisaoInteira3 = floor(x/y);

    int raiz = sqrt(x);

    return 0;
}