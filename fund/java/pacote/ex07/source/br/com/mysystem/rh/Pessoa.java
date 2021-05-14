package br.com.mysystem.rh;

public class Pessoa {
    public String nome;
    public String email;
    @Override
    public String toString(){
        return nome+", "+email;
    }
}
