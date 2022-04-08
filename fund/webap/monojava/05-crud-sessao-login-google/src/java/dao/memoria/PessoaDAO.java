/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dao.memoria;

/**
 *
 * @author friend
 */
import dao.PessoaDAOInterface;
import java.util.ArrayList;
import modelo.Pessoa;

public class PessoaDAO implements PessoaDAOInterface {

    private ArrayList<Pessoa> pessoas = new ArrayList();

    @Override
    public ArrayList<Pessoa> retornarPessoas() {
        return pessoas;
    }

    @Override
    public boolean incluirPessoa(Pessoa nova) {
        try {
            pessoas.add(nova);
            return true;
        } catch (Exception e) {
            System.out.println("depuração: " + e.getMessage());
            return false;
        }
    }

    @Override
    public boolean removerPessoa(String cpf) {
        try {
            int encontrado = -1; // variável para sinalizar sucesso da busca
            for (int i = 0; i < pessoas.size(); i++) { // percorrer a lista 
                if (pessoas.get(i).getCpf().equals(cpf)) { // achou?
                    encontrado = i; // sinaliza a posição da pessoa encontrada
                    break; // interrompe a busca
                }
            }
            if (encontrado >= 0) { // se achou...
                pessoas.remove(encontrado);
            } else {
                return false;
            }
            return true;
        } catch (Exception e) {
            System.out.println("depuração: " + e.getMessage());
            return false;
        }
    }

    @Override
    public Pessoa buscarPessoa(String cpf) {
        try {
            for (int i = 0; i < pessoas.size(); i++) { // percorrer a lista 
                if (pessoas.get(i).getCpf().equals(cpf)) { // achou?
                    return pessoas.get(i);
                }
            }
            return null;
        } catch (Exception e) {
            System.out.println("depuração: " + e.getMessage());
            return null;
        }
    }

    @Override
    public boolean atualizarPessoa(Pessoa novosDados) {
        try {
            int encontrado = -1; // variável para sinalizar sucesso da busca
            for (int i = 0; i < pessoas.size(); i++) { // percorrer a lista 
                if (pessoas.get(i).getCpf().equals(novosDados.getCpf())) { // achou?
                    encontrado = i; // sinaliza a posição da pessoa encontrada
                    break; // interrompe a busca
                }
            }
            if (encontrado >= 0) { // se achou...
                pessoas.set(encontrado, novosDados); // atualiza a pessoa
                return true;
            } else {
                return false;
            }
        } catch (Exception e) {
            System.out.println("depuração: " + e.getMessage());
            return false;
        }
    }
}
