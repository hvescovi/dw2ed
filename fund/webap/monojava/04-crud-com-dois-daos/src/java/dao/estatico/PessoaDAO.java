package dao.estatico;

import dao.PessoaDAOInterface;
import java.util.ArrayList;
import modelo.Pessoa;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

public class PessoaDAO implements PessoaDAOInterface{

    public ArrayList<Pessoa> retornarPessoas() {
        ArrayList<Pessoa> retorno = new ArrayList<Pessoa>();
        retorno.add(new Pessoa("12345678910", "João da Silva", 
                "josilva@gmail.com", "47 9 92332 3332"));
        return retorno;
    }

    public boolean incluirPessoa(Pessoa nova) {
        return true;
    }

    public boolean removerPessoa(String nome) {
        return true;
    }
    
    public Pessoa buscarPessoa(String nome) {
        return new Pessoa("12345678910", "João da Silva", 
                "josilva@gmail.com", "47 9 92332 3332");
    } 
    
    public boolean AtualizarPessoa(String nome) {
        return true;
    }

}