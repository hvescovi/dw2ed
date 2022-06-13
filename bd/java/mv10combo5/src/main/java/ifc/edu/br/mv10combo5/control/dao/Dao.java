/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ifc.edu.br.mv10combo5.control.dao;

import ifc.edu.br.mv10combo5.model.Pessoa;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;
import java.util.ArrayList;

public class Dao {
    
    public ArrayList<Pessoa> retornarPessoas() {
        
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("meupu");
        EntityManager em = emf.createEntityManager();
        
        ArrayList<Pessoa> pessoas = (ArrayList) em.createQuery("from Pessoa", Pessoa.class).getResultList();
        
        em.close();
        
        return pessoas;        
    }
    
}
