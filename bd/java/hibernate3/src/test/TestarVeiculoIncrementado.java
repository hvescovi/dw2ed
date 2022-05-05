package test;

import java.math.BigDecimal;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;

import model.Acessorio;
import model.VeiculoIncrementado;
import utils.JpaUtil;

public class TestarVeiculoIncrementado {

	public static void main(String args[]) {
		// conexão
		EntityManager manager = JpaUtil.getEntityManager();

		// iniciando transação
		EntityTransaction tx = manager.getTransaction();
		tx.begin();

		Acessorio a1 = new Acessorio();
		a1.setDescricao("alarme");
		manager.persist(a1);
		
		Acessorio a2 = new Acessorio();
		a2.setDescricao("bancos de couro");
		manager.persist(a2);
				
		VeiculoIncrementado v1 = new VeiculoIncrementado();
		v1.setFabricante("Honda");
		v1.setModelo("Civic");
		v1.setAnoFabricacao(2012);
		v1.setAnoModelo(2013);
		v1.setValor(new BigDecimal(71300));
		v1.getAcessorios().add(a1);
		v1.getAcessorios().add(a2);
		manager.persist(v1);

		tx.commit();
		
		System.out.println("Carro: ");

		for (Acessorio acs : v1.getAcessorios()) {
			System.out.print("(");
			System.out.print(acs.getCodigo());
			System.out.println(") " + acs.getDescricao());			
		}

		manager.close();
		JpaUtil.close();
	}
}
