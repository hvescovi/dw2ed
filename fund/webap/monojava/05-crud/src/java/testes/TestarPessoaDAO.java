/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package testes;

import dao.PessoaDAO;
import modelo.Pessoa;

/**
 *
 * @author friend
 */
public class TestarPessoaDAO {

    PessoaDAO pdao = new PessoaDAO();
    
    public void listarPessoas(){
        System.out.println("Lista de pessoas:");
        for (Pessoa p : pdao.retornarPessoas()){
            System.out.println(p);
        }        
        System.out.println("Fim da lista de pessoas");
    }
    public static void main(String[] args) {
        TestarPessoaDAO teste = new TestarPessoaDAO();
        
        System.out.println("* Listar pessoas");
        teste.listarPessoas();
        
        System.out.println("* Incluir pessoa");
        System.out.println(teste.pdao.incluirPessoa(new Pessoa("12345678910", "João da Silva", 
                "josilva@gmail.com", "47 9 92332 3332")));
        teste.listarPessoas();
        
        System.out.println("* Alterar pessoa");
        Pessoa alguem = teste.pdao.buscarPessoa("12345678910");
        alguem.setEmail("alterado@gmail.com");
        System.out.println(teste.pdao.atualizarPessoa(alguem));
        teste.listarPessoas();        
        
        System.out.println("* Remover pessoa");
        System.out.println(teste.pdao.removerPessoa("12345678910"));
        teste.listarPessoas();       
        
        System.out.println("FIM DOS TESTES");
    }
}
