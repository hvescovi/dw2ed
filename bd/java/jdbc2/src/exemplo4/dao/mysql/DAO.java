package exemplo4.dao.mysql;

import java.sql.SQLException;
import java.util.ArrayList;

import javax.sql.rowset.JdbcRowSet;
import javax.sql.rowset.RowSetProvider;

import exemplo4.modelo.Author;

public class DAO {

	final String DATABASE_URL = "jdbc:mysql://localhost/books";
	final String USERNAME = "root";
	final String PASSWORD = "testando";
	
	JdbcRowSet rowSet;

	public DAO() {
		try {
			rowSet = RowSetProvider.newFactory().createJdbcRowSet();
			rowSet.setUrl(DATABASE_URL);
			rowSet.setUsername(USERNAME);
			rowSet.setPassword(PASSWORD);
		} catch (SQLException ex) {
			ex.printStackTrace();
		}		
	}
	
	public void fechar() {
		try {
			rowSet.close();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
	public ArrayList<Author> retornarAutores() {
		ArrayList<Author> retorno = new ArrayList<Author>();
		String query =  
				"SELECT * from Authors";
		try {
			rowSet.setCommand(query);
			rowSet.execute();
			while (rowSet.next()) {
				Author a = new Author();
				a.AuthorID = rowSet.getInt("AuthorID");
				a.FirstName = rowSet.getString("FirstName");
				a.LastName = rowSet.getString("LastName");
				retorno.add(a);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return retorno;
	}

	public void incluirAutor(Author novo) {
// https://docs.oracle.com/javase/tutorial/jdbc/basics/jdbcrowset.html#inserting-row
		try {
			rowSet.moveToInsertRow();
			rowSet.updateString("FirstName", novo.FirstName);
			rowSet.updateString("LastName", novo.LastName);
			rowSet.insertRow();
		} catch (SQLException e) {
			e.printStackTrace();
		}		
	}
	
	public void excluirAutorPeloNome(String primeiroNome, String ultimoNome) {
		String query =
				"SELECT * from Authors WHERE FirstName = ? AND LastName = ?";
		try {
			rowSet.setCommand(query);
			rowSet.setString(1, primeiroNome);
			rowSet.setString(2, ultimoNome);
			rowSet.execute();
			if (rowSet.first()) {
				rowSet.deleteRow();
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
}
