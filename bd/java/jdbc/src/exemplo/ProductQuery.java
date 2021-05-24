package exemplo;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class ProductQuery extends Application {

	public static final String URL = "jdbc:mysql://localhost/ElectricalStore?useSSL=true";
	public static final String USERNAME = "root";
	public static final String PASSWORD = "testando";
	
	@Override
	public void start(Stage stage) {
		VBox data1 = new VBox();
		VBox data2 = new VBox();
		VBox data3 = new VBox();
		VBox data4 = new VBox();
		
		data1.getChildren().add(new Text("Número serial: \n"));
		data2.getChildren().add(new Text("Marca \n"));
		data3.getChildren().add(new Text("Descrição \n"));
		data4.getChildren().add(new Text("Preço \n"));
		
		HBox root = new HBox(10);
		root.setPadding(new Insets(10));
		root.getChildren().addAll(data1, data2, data3, data4);
		Scene scene = new Scene(root, 300, 150);
		stage.setTitle("Loja de materiais elétricos");
		stage.setScene(scene);
		stage.show();
	
		Connection con;
		Statement st;
		ResultSet result;
		try {
			con = DriverManager.getConnection(URL, USERNAME, PASSWORD);
			st = con.createStatement();
			result = st.executeQuery("select * from products");
			while (result.next()) {
				String serial = result.getString(1);
				String marca = result.getString(2);
				String descricao = result.getString(3);
				String preco = result.getString(4);
				data1.getChildren().add(new Text(serial));
				data2.getChildren().add(new Text(marca));
				data3.getChildren().add(new Text(descricao));
				data4.getChildren().add(new Text(preco));
			}
		} catch (SQLException ex) {
			System.out.print("Erro no SQL: " + ex.getMessage());
		}
	}
	
	public static void main(String args[]) {
		launch(args);		
	}
}