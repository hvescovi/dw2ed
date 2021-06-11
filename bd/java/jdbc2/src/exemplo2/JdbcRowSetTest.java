package exemplo2;

import java.sql.ResultSetMetaData;
import java.sql.SQLException;

import javax.sql.rowset.JdbcRowSet;
import javax.sql.rowset.RowSetProvider;

public class JdbcRowSetTest {

    public static void main(String[] args) {
		
		final String DATABASE_URL = "jdbc:mysql://localhost/books";
		final String USERNAME = "root";
		final String PASSWORD = "testando";
		
		final String SELECT_QUERY = 
				"SELECT LastName, FirstName, Title"
				+ " FROM Authors"
				+ " INNER JOIN AuthorISBN"
				+ " ON Authors.AuthorID = AuthorISBN.AuthorID"
				+ " INNER JOIN Titles"
				+ " ON AuthorISBN.ISBN = Titles.ISBN"
				+ " ORDER BY Titles.Title";
		
		try {
			// JdbcRowSet => conexão persistente
			// CacheRowSet => conexão eventual
			JdbcRowSet rowSet = RowSetProvider.newFactory().createJdbcRowSet();
			rowSet.setUrl(DATABASE_URL);
			rowSet.setUsername(USERNAME);
			rowSet.setPassword(PASSWORD);
			
			rowSet.setCommand(SELECT_QUERY);
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
}
