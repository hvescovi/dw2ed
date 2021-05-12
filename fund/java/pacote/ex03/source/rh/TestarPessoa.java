package rh;

public class TestarPessoa {
    public static void main (String args[]) {
        Pessoa joao = new Pessoa();
        joao.nome = "João da Silva";
        joao.email = "josilva@gmail.com";
        System.out.println(joao.nome + ", " + joao.email);
    }
    
}