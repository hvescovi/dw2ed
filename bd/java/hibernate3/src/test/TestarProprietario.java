package test;

import java.math.BigDecimal;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;

import model.Proprietario;
import model.VeiculoComDono;
import utils.JpaUtil;

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
		p.setEmail("josilva@gmail.com");
		p.setTelefone("34 1234-5678");
		// persistir para gerar o ID do proprietário
		manager.persist(p);
		System.out.print("PropID: ");
		System.out.println(p.getCodigo());

		VeiculoComDono v1 = new VeiculoComDono();
		v1.setFabricante("Honda");
		v1.setModelo("Civic");
		v1.setAnoFabricacao(2012);
		v1.setAnoModelo(2013);
		v1.setValor(new BigDecimal(71300));
		v1.setProprietario(p);
		manager.persist(v1);

		VeiculoComDono v2 = new VeiculoComDono();
		v2.setFabricante("Ford");
		v2.setModelo("KA");
		v2.setAnoFabricacao(2003);
		v2.setAnoModelo(2004);
		v2.setValor(new BigDecimal(14000));
		v2.setProprietario(p);
		manager.persist(v2);

		tx.commit();

		// carregar a listas de veículos!!
		// senão a lista de veículos vem NULA!
		manager.refresh(p);

		System.out.println("Proprietario: " + p.getNome());
		System.out.println("Carros: ");

		for (VeiculoComDono mv : p.getVeiculos()) {
			// System.out.print(mv.getCodigo());
			System.out.print("(");
			System.out.print(mv.getCodigo());
			System.out.println(") " + mv.getModelo());			
		}

		manager.close();
		JpaUtil.close();
	}
}
