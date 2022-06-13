/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ifc.edu.br.mv10combo5.teste;

import ifc.edu.br.mv10combo5.model.Pessoa;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

public class TestarConsultarPessoa {

    public static void main(String[] args) {

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("meupu");
        EntityManager em = emf.createEntityManager();
        
        Pessoa a = em.createQuery("from Pessoa", Pessoa.class).getSingleResult();
        System.out.println(a);
        
        em.close();
        
        System.out.println("Pessoa consultada no BD!");
    }
}
