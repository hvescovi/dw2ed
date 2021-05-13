package livraria;

import org.freesoft.Pessoa;

public class TestarLivro {
    public static void main(String args[]) {
        Pessoa hyl = new Pessoa();
        hyl.nome = "Hylson";
        hyl.telefone = "27-9121-1314";
        
        Livro desperte = new Livro();
        desperte.nome = "Desperte o seu gigante interior";
        desperte.autores = "Tony Robbins";
        desperte.proprietario = hyl;

        System.out.println(desperte);
    }
}
