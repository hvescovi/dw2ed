package exemplo;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import java.util.ArrayList;
import org.hibernate.query.Query;
import org.hibernate.HibernateException;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import org.hibernate.cfg.Configuration;
import org.hibernate.service.ServiceRegistry;

public class ProductQuery2 extends Application {

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
	
		try {
		  Configuration cfg = new Configuration();
		  cfg.configure("hibernate.cfg.xml");
		
		  cfg.addResource("hibernate.hbm.xml");
		  
		  ServiceRegistry serviceRegistry = new 
				  StandardServiceRegistryBuilder().applySettings(
						  cfg.getProperties()).build();
		  SessionFactory sessionFactory = cfg.buildSessionFactory(serviceRegistry);
		  Session session = sessionFactory.openSession();
		  
		  Query query = session.createQuery("from Product");
		  ArrayList<Product> list = (ArrayList) query.list();
		  
		  for (Product pr : list) {
			String serial = pr.getStockNumber();
			String marca = pr.getManufacturer();
			String descricao = pr.getItem();
			double preco = pr.getUnitPrice();
			data1.getChildren().add(new Text(serial));
			data2.getChildren().add(new Text(marca));
			data3.getChildren().add(new Text(descricao));
			data4.getChildren().add(new Text("R$" + preco)); // conversão implícita
		  }
		  
		  session.close();
		  sessionFactory.close();
		  StandardServiceRegistryBuilder.destroy(serviceRegistry);
		  
		} 
		catch (HibernateException e) 
		{
		    System.out.println("Erro: " + e.getMessage());
		    e.printStackTrace();
		}	
		
	}
	
	public static void main(String args[]) {
		launch(args);
	}
		
}
