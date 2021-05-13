package livraria;

import org.freesoft.Pessoa;

public class Livro {
    public String nome;
    public String autores;
    public Pessoa proprietario;
    @Override 
    public String toString() {
        return nome+", "+autores+", "+proprietario;
    }
}
