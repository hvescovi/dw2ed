/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package test;
import java.math.BigDecimal;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;

import model.Cliente;
import model.Funcionario;
import utils.JpaUtil;

public class TestarHerancaInserir {

	public static void main(String[] args) {
		// conexão
		EntityManager manager = JpaUtil.getEntityManager();
				
		// transação (para incluir dados)
		EntityTransaction tx = manager.getTransaction();
		tx.begin();
			
		Cliente cli = new Cliente();
		cli.setNome("João da Silva");
		cli.setTipoSanguineo("O+");
		cli.setRendaMensal(new BigDecimal(5000));
		cli.setBloqueado(false);
		cli.setLimiteCredito(new BigDecimal(10000));
		manager.persist(cli);
		
		Funcionario fun = new Funcionario();
		fun.setNome("Maria Oliveira");
		fun.setTipoSanguineo("AB-");
		fun.setSalario(new BigDecimal(7850));
		fun.setCargo("Cientista de Dados");
		manager.persist(fun);
		
		// efetivar a gravação dos dados
		tx.commit();
		
		System.out.println("Dados teste de herança inseridos");
		
		manager.close();
		JpaUtil.close();                
	}
}