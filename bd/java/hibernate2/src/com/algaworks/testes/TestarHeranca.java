package com.algaworks.testes;

import java.math.BigDecimal;
import java.util.ArrayList;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;

import com.algaworks.dominio.Cliente;
import com.algaworks.dominio.Funcionario;
import com.algaworks.dominio.Pessoa;
import com.algaworks.utils.JpaUtil;

public class TestarHeranca {

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
		
		// listando dados de forma polimórfica
		ArrayList<Pessoa> pessoas = new ArrayList();
		pessoas.add(fun);
		pessoas.add(cli);
		
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