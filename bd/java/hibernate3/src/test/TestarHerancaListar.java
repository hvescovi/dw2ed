/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package test;

import java.util.List;
import javax.persistence.EntityManager;
import model.Cliente;
import model.Funcionario;
import model.Pessoa;
import utils.JpaUtil;

public class TestarHerancaListar {

	public static void main(String[] args) {
		// conexão
		EntityManager manager = JpaUtil.getEntityManager();
				
		// listando dados de forma polimórfica
		List<Pessoa> pessoas = manager.createQuery("from Pessoa").getResultList();
                
		for (Pessoa p : pessoas) {
			System.out.println("Pessoa: "+p.getNome());
			if (p instanceof Cliente) {
				System.out.print("Renda mensal: ");
				System.out.println(((Cliente) p).getRendaMensal());
			} else { // por enquanto, só pode ser um funcionário
				System.out.print("Salário: ");
				System.out.println(((Funcionario) p).getSalario());
			}
		}
		
		manager.close();
		JpaUtil.close();
	}
}