package livraria;

import br.com.mysystem.rh.Pessoa;

public class TestarLivro {
    public static void main(String args[]) {
        Pessoa hyl = new Pessoa();
        hyl.nome = "Hylson";
        hyl.email = "hvescovi@gmail.com";
        
        Livro desperte = new Livro();
        desperte.nome = "Desperte o seu gigante interior";
        desperte.autores = "Tony Robbins";
        desperte.proprietario = hyl;

        System.out.println(desperte);
    }
}
