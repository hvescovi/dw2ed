package test;

import java.math.BigDecimal;
import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;
import javax.persistence.Query;

import model.Veiculo;
import utils.JpaUtil;

public class TestarVeiculo {

	public static void main(String args[]) {
		// conexão
		EntityManager manager = JpaUtil.getEntityManager();
		
		// inclusão de dados
		System.out.println("INCLUINDO");
		EntityTransaction tx = manager.getTransaction();
		tx.begin();
		
		Veiculo v = new Veiculo();
		v.setFabricante("Honda");
		v.setModelo("Civic");
		v.setAnoFabricacao(2012);
		v.setAnoModelo(2013);
		v.setValor(new BigDecimal(71300));
		manager.persist(v);
		
		// inserindo outro para melhor listagem (a seguir)
		v = new Veiculo();
		v.setFabricante("Ford");
		v.setModelo("KA");
		v.setAnoFabricacao(2003);
		v.setAnoModelo(2004);
		v.setValor(new BigDecimal(14000));
		manager.persist(v);
		
/* comandos executados pelo hibernate:
Hibernate: select next_val as id_val from hibernate_sequence for update
Hibernate: update hibernate_sequence set next_val= ? where next_val=?
Hibernate: insert into tab_veiculo 
    (ano_fabricacao, ano_modelo, fabricante, modelo, valor, codigo) 
    values (?, ?, ?, ?, ?, ?)
*/
		
		// confirmando as inclusões: é neste comando que
		// o registro é inserido na tabela (sincronização)
		tx.commit();
		// caso queira sincronizar o objeto e o registro/tabela
		// antes do commit, pode-se utilizar o comando
		// manager.flush()
		
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
				
		// busca de dados
		v = manager.getReference(Veiculo.class, maiorCodigo);
		System.out.println("CONSULTANDO: Veículo código "+v.getCodigo()+
				", "+v.getModelo());
		// essa busca não aparece no log do hibernate pois
		// o objeto já está carregado no contexto
		// (cache de primeiro nível)
		// caso fosse necessário descarregar o objeto do
		// cache, usaríamos manager.detach(v)
		
		// atualizando um dado
		System.out.println("ALTERANDO");
		tx = manager.getTransaction();
		tx.begin(); // transação também para encontrar registros
		v = manager.find(Veiculo.class, maiorCodigo);
		System.out.println("Valor antigo: " + v.getValor());
		v.setValor(new BigDecimal(500));
		tx.commit();
		System.out.println("Novo valor: " + v.getValor());
		
		// excluindo
		System.out.println("EXCLUINDO");
		tx.begin();
		v = manager.find(Veiculo.class, maiorCodigo);
		manager.remove(v);
		tx.commit();
		
		manager.close();
		JpaUtil.close();
	}
}