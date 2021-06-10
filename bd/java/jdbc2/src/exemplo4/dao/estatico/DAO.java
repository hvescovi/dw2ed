package exemplo4.dao.estatico;

import java.util.ArrayList;
import exemplo4.modelo.Author;

public class DAO {

	
	
	
		
		public void fechar() {
		}
		
		public ArrayList<Author> retornarAutores() {
			ArrayList<Author> retorno = new ArrayList<Author>();
			
			Author novo = new Author();
			novo.AuthorID = 1;
			novo.FirstName = "John";
			novo.LastName = "Back";
			
			retorno.add(novo);
			
			novo = new Author();
			novo.AuthorID = 2;
			novo.FirstName = "Mary";
			novo.LastName = "Jane";
			
			retorno.add(novo);
			
			return retorno;
		}

		public void incluirAutor(Author novo) {
		}
		
		public void excluirAutorPeloNome(String primeiroNome, String ultimoNome) {
		}
}