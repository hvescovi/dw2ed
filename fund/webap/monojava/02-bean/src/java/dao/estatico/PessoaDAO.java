/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dao.estatico;

import model.Pessoa;

/**
 *
 * @author friend
 */
public class PessoaDAO {

    public Pessoa retornarPessoa(String cpf) {
        Pessoa p1 = new Pessoa();
        p1.setCpf("12345678910");
        p1.setNome("João da Silva");
        p1.setTelefone("47-92939293");
        p1.setEmail("josilva@gmail.com");
        return p1;
    }
}
