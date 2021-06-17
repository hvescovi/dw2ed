package com.algaworks.testes;

import java.math.BigDecimal;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;

import com.algaworks.dominio.Proprietario;
import com.algaworks.dominio.Veiculo;
import com.algaworks.utils.JpaUtil;

public class TestarProprietario {

	public static void main(String args[]) {
		// conexão
		EntityManager manager = JpaUtil.getEntityManager();
		
		// iniciando transação
		EntityTransaction tx = manager.getTransaction();
		tx.begin();
		
		// inclusão de dados
		Proprietario p = new Proprietario();
		p.setNome("João da Silva");
		p.setTelefone("34 1234-5678");
		manager.persist(p);
		System.out.println("Proprietario: " + p.getNome());
		
		Veiculo v = new Veiculo();
		v.setFabricante("Honda");
		v.setModelo("Civic");
		v.setAnoFabricacao(2012);
		v.setAnoModelo(2013);
		v.setValor(new BigDecimal(71300));
		manager.persist(v);
		
		v = new Veiculo();
		v.setFabricante("Ford");
		v.setModelo("KA");
		v.setAnoFabricacao(2003);
		v.setAnoModelo(2004);
		v.setValor(new BigDecimal(14000));
		manager.persist(v);
		
		for (Veiculo veic : p.getVeiculos()) {
			System.out.println(veic.getCodigo() + 
					" - " + veic.getModelo());
		}
		
		manager.close();
		JpaUtil.close();
	}
}
