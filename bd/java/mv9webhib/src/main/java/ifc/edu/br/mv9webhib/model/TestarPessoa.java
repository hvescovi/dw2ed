/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ifc.edu.br.mv9webhib.model;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.Persistence;

public class TestarPessoa {

    public static void main(String[] args) {
        
        Pessoa p = new Pessoa("João da Silva", "josilva@gmail.com", 70.5f);

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("meuPU");
        EntityManager em = emf.createEntityManager();
        
        EntityTransaction tx = em.getTransaction();
        
        tx.begin();
        em.persist(p);
        tx.commit();

        Pessoa a = em.createQuery("from Pessoa", Pessoa.class)
                .getSingleResult();
        System.out.println(a);
        
        em.close();
    }
}
