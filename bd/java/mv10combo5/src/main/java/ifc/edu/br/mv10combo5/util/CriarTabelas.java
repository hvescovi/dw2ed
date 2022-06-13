/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ifc.edu.br.mv10combo5.util;

import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

public class CriarTabelas {
    
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("meupu");
    }
}
