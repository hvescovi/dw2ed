package exemplo4.testes;

import exemplo4.dao.mysql.DAO;
//import exemplo4.dao.estatico.DAO;
import exemplo4.modelo.Author;

public class TestarDAO {

	// criar um DAO
	DAO dao = new DAO();

	public void listarPessoas() {
		for (Author a : dao.retornarAutores()) {
			// exibir a pessoa (método toString será invocado automaticamente)
			System.out.println(a);
		}
	}
	
	public static void main(String[] args) {
		// instanciar a classe de teste
		TestarDAO tdao = new TestarDAO();
		
		// testar o método de exibir pessoas
		System.out.println("Pessoas no sistema:");
		tdao.listarPessoas();		
		
		// testar o método de incluir pessoa
		Author novo = new Author();
		novo.FirstName = "Jackson";
		novo.LastName = "Storm";
		tdao.dao.incluirAutor(novo);
		
		// lista as pessoas de novo, para ver a nova pessoa
		System.out.println("Pessoa incluída:");
		tdao.listarPessoas();
		
		// exclui a pessoa incluída, para deixar o teste idempotente
		// (apesar de que o ID da nova pessoa vai "crescendo"
		tdao.dao.excluirAutorPeloNome("Jackson", "Storm");
		
		// listar novamente, para conferir exclusão
		System.out.println("Após exclusão:");
		tdao.listarPessoas();
		
		tdao.dao.fechar();
	}	
}
