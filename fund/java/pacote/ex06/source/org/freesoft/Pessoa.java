package org.freesoft;

public class Pessoa {
    public String nome;
    public String telefone;
    @Override
    public String toString(){
        return nome+", "+telefone;
    }
}
