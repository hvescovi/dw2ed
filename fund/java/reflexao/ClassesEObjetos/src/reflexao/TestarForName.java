package reflexao;

import java.lang.reflect.Constructor;
import java.lang.reflect.Type;

public class TestarForName {

	public static void main(String args[]) {
		try {
			Class<?> hm = Class.forName("java.util.HashMap");
			System.out.println("Nome da classe: " + hm.getName());
			for (Constructor c : hm.getConstructors()) {
				System.out.print("Construtor com " + 
			        c.getParameterCount() + " parâmetros");
				if (c.getParameterCount() > 0) {
					System.out.print(": ");
					for (Type t : c.getGenericParameterTypes()) {
						System.out.print(" (" + t.getTypeName() + ")");
					}
				}
				System.out.println(" ");				
			}
		} catch (ClassNotFoundException ex) {
			System.out.println("Classe não encontrada: "+ex.getMessage());
		}
	}
}
