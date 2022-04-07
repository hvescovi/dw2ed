/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package dao;

import java.util.ArrayList;
import modelo.Pessoa;

public interface PessoaDAOInterface {    
    public ArrayList<Pessoa> retornarPessoas();	
    public boolean incluirPessoa(Pessoa nova);	
    public boolean removerPessoa(String nome);	   
    public Pessoa buscarPessoa(String nome);
    public boolean atualizarPessoa(Pessoa novosDados);
}
