/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ifc.edu.br.mv10combo5.teste;

import ifc.edu.br.mv10combo5.control.dao.Dao;
import ifc.edu.br.mv10combo5.model.Pessoa;
import java.util.ArrayList;

public class TestarDao {
    
    public static void main(String[] args) {
        
        Dao dao = new Dao();
        
        System.out.println("Listando pessoas:");
        ArrayList<Pessoa> pessoas = dao.retornarPessoas();
        for (Pessoa p : pessoas) {
            System.out.println(p);
        }
    }
}
