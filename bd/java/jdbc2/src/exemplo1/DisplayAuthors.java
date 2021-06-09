package exemplo1;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;

public class DisplayAuthors {

	public static void main(String[] args) {
		
		final String DATABASE_URL = "jdbc:mysql://localhost/books";
		final String USERNAME = "root";
		final String PASSWORD = "testando";
		
		final String SELECT_QUERY = "SELECT authorID, firstName, lastName FROM Authors";
		
		try {
			Connection con = DriverManager.getConnection(DATABASE_URL, USERNAME, PASSWORD);
			Statement st = con.createStatement();			
			ResultSet result = st.executeQuery(SELECT_QUERY);
			
			ResultSetMetaData md = result.getMetaData();
			int cols = md.getColumnCount();
			
			System.out.println("Autores:");
			
			for (int i = 1; i <= cols; i++) {
				System.out.printf("%-8s\t", md.getColumnName(i));
			}
			System.out.println();
			
			while (result.next()) {
				for (int i = 1; i <= cols; i++) {
					System.out.printf("%-8s\t", result.getObject(i));
				}
				System.out.println();
			}
			
		} catch (SQLException ex) {
			ex.printStackTrace();
		}
		
	}

}
