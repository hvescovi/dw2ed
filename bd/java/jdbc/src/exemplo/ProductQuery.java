package exemplo;

// mysql connector downloaded from:
// https://mvnrepository.com/artifact/mysql/mysql-connector-java/8.0.25

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

// javafx downloaded from 
// https://gluonhq.com/products/javafx/

// all libraries were imported to from the
// unzipped folder at Downloads

// added parameters to the run configurations:
// https://stackoverflow.com/questions/52144931/how-to-add-javafx-runtime-to-eclipse-in-java-1

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;
import javafx.stage.Stage;

// database started like that:
// docker run --name=test-mysql -e MYSQL_ROOT_PASSWORD=testando -e MYSQL_ROOT_HOST=% mysql/mysql-server:5.7

// accessing and populating:

/*
$ docker exec -it test-mysql bash

# mysql -u root -p 

mysql> create database ElectricalStore;
mysql> use ElectricalStore;
mysql> create table products (serialNumber char(25), make char(10), description char(25), price decimal(10, 2));
mysql> insert into products values ("1076543", "Acme", "Aspirador de po", 180.11);
mysql> insert into products values ("3756354", "Nadir", "Maquina de lavar", 178.97);
mysql> select * from products;
mysql> help;
mysql> status;
mysql> exit
*/

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