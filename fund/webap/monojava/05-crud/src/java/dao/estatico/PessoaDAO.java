package dao.estatico;

import dao.PessoaDAOInterface;
import java.util.ArrayList;
import modelo.Pessoa;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

public class PessoaDAO implements PessoaDAOInterface{

    @Override
    public ArrayList<Pessoa> retornarPessoas() {
        ArrayList<Pessoa> retorno = new ArrayList<Pessoa>();
        retorno.add(new Pessoa("12345678910", "João da Silva", 
                "josilva@gmail.com", "47 9 92332 3332"));
        return retorno;
    }

    @Override
    public boolean incluirPessoa(Pessoa nova) {
        return true;
    }

    @Override
    public boolean removerPessoa(String cpf) {
        return true;
    }
    
    @Override
    public Pessoa buscarPessoa(String cpf) {
        return new Pessoa("12345678910", "João da Silva", 
                "josilva@gmail.com", "47 9 92332 3332");
    } 
    
    @Override
    public boolean atualizarPessoa(Pessoa novosDados) {
        return true;
    }

}