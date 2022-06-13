/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ifc.edu.br.mv10combo5.teste;

import ifc.edu.br.mv10combo5.model.Pessoa;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.Persistence;

public class TestarIncluirPessoa {

    public static void main(String[] args) {

        Pessoa p = new Pessoa();
        p.setNome("João da Silva");
        p.setEmail("josilva@gmail.com");
        p.setTelefone("123123123");

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("meupu");
        EntityManager em = emf.createEntityManager();
        
        EntityTransaction tx = em.getTransaction();
        
        tx.begin();
        em.persist(p);
        tx.commit();
        
        em.close();
        
        System.out.println("Pessoa inserida no BD!");
    }
}
