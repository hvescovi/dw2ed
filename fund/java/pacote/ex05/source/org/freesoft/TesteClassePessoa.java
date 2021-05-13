package org.freesoft;

public class TesteClassePessoa {
    public static void main (String args[]) {
        Pessoa joao = new Pessoa();
        joao.nome = "João da Silva";
        joao.telefone = "27-9221-1213";
        System.out.println(joao.nome + ", " + joao.telefone);
    }
    
}
