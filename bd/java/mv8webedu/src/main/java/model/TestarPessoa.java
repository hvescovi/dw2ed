/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.Persistence;

/**
 *
 * @author friend
 */
public class TestarPessoa {
    
    public static void main(String[] args) {
        
        Pessoa p = new Pessoa("João da Cunha", "jocunha@gmail.com", 70.5f);
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
