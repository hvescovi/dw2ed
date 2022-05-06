package test;

import java.math.BigDecimal;
import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;
import javax.persistence.Query;

import model.Veiculo;
import utils.JpaUtil;

public class TestarVeiculoDesanexado {

	public static void main(String[] args) {
		// conexão
		EntityManager manager = JpaUtil.getEntityManager();
		
		// listando todos
		System.out.println("LISTANDO");
		Long maiorCodigo = 0L;
		Query q = manager.createQuery("from Veiculo");
		List<Veiculo> veiculos = q.getResultList();
		for (Veiculo veic : veiculos) {
			System.out.println("("+veic.getCodigo()+
					") "+veic.getModelo());
			maiorCodigo = veic.getCodigo();
		}
				
		// carregando o último objeto listado em um objeto
		Veiculo v = manager.getReference(Veiculo.class, maiorCodigo);
				
		// fechando a conexão
		manager.close();
		
		// alterando o objeto: a operação 
		// não será sincronizada
		v.setValor(new BigDecimal(13000));
		
		// atualizar o objeto: é preciso reanexar!
		manager = JpaUtil.getEntityManager();
		EntityTransaction tx = manager.getTransaction();
		
		Veiculo novoVeic = manager.merge(v);
		
		tx.commit();
		
		manager.close();
		JpaUtil.close();
	}
}