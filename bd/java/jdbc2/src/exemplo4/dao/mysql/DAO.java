package exemplo4.dao.mysql;

import java.sql.SQLException;

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
	
	public void retornarAutores() {
		String query =  
				"SELECT * from Authors";
		try {
			rowSet.execute();
			while (rowSet.next()) {
				Author a = new Author();
				a.AuthorID = rowSet.
			}
			return 
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
}
