package reflexao;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class InformacaoClasse {

	public static void main(String[] args) {
		
		String buscar = "java.util.TreeMap";
		try {
			Class<?> c = Class.forName(buscar);
			imprimirHierarquia(c, 1);
		} catch (ClassNotFoundException e) {
			System.out.println("Classe não encontrada: "+e.getMessage());
		}
	}
	
	private static void imprimirHierarquia(Class<?> c, int nivel) {
		List<Class<?>> lista = getSuperclasseEInterfaces(c);
		String recuo = "";
		for (int i=0; i<nivel; i++) { recuo += "   "; }
		for (Class<?> clazz : lista) {
			System.out.print(recuo+"|-> "+clazz.getName());
			if (!clazz.isInterface()) { // se não é interface...
				System.out.print(" (superclass)"); //... é a classe mãe
			}
			System.out.println(" ");
			if (clazz != Object.class) {
				imprimirHierarquia(clazz, nivel+1);
			}
		}
	}
	
	private static List<Class<?>> getSuperclasseEInterfaces(Class<?> c) {
		List<Class<?>> lista = new ArrayList<>();
		if (c.getSuperclass() != null) {
			lista.add(c.getSuperclass());
		}
		lista.addAll(Arrays.asList(c.getInterfaces()));
		return lista;
	}

}
