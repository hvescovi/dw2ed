package exemplo3;

import java.sql.ResultSetMetaData;
import java.sql.SQLException;

import javax.sql.rowset.JdbcRowSet;
import javax.sql.rowset.RowSetProvider;

public class PreparedStatementComRowSet {
	// JdbcRowSet: banco de dados sempre conectado
	// CachedRowSet: conexão apenas na operação
	
	final String DATABASE_URL = "jdbc:mysql://localhost/books";
	final String USERNAME = "root";
	final String PASSWORD = "testando";

	final String SELECT_QUERY = 
			"SELECT LastName, FirstName, Title"
			+ " FROM Authors INNER JOIN AuthorISBN"
			+ " ON Authors.AuthorID = AuthorISBN.AuthorID"
			+ " INNER JOIN Titles"
			+ " ON AuthorISBN.ISBN = Titles.ISBN ";
	
	public void exibir(String filtro, Object[] valores) {
		try {
			JdbcRowSet rowSet = RowSetProvider.newFactory().createJdbcRowSet();
			rowSet.setUrl(DATABASE_URL);
			rowSet.setUsername(USERNAME);
			rowSet.setPassword(PASSWORD);
			rowSet.setCommand(SELECT_QUERY + filtro);
			
			// suporte a valores do tipo String e Integer
			for (int i = 0; i < valores.length; i++) {
				if (valores[i] instanceof String) {
					rowSet.setString(i+1, (String) valores[i]);					
				} else if (valores[i] instanceof Integer) {
					rowSet.setInt(i+1, (Integer) valores[i]);
				}
			}
			
			rowSet.execute();
			
			ResultSetMetaData md = rowSet.getMetaData();
			int cols = md.getColumnCount();
			
			System.out.println("Autores:");
			
			for (int i = 1; i <= cols; i++) {
				System.out.printf("%-8s\t", md.getColumnName(i));
			}
			System.out.println();
			
			while (rowSet.next()) {
				for (int i = 1; i <= cols; i++) {
					System.out.printf("%-8s\t", rowSet.getObject(i));
				}
				System.out.println();
			}
			
		} catch (SQLException ex) {
			ex.printStackTrace();
		}
	}
	
    public static void main(String[] args) { 
		PreparedStatementComRowSet gen = new PreparedStatementComRowSet();
		
        gen.exibir("", new String[0]);
		gen.exibir("WHERE FirstName = ?", new Object[] {"Abbey"});
	}	
}