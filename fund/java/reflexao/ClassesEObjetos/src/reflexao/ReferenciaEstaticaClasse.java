package reflexao;

public class ReferenciaEstaticaClasse {

	// código do livro Componentes reutilizáveis em java 
	// com reflexão e anotações, de Eduardo Guerra
	
	public static void main(String args[]) {
		Class<String> classe = String.class;
		System.out.println(classe.getName());
		imprimeNomeClasse(Integer.class);
		Class inst = Boolean.class;
		System.out.println(inst.getName());
	}
	
	public static void imprimeNomeClasse(Class<?> classe) {
		System.out.println("Chamando o método com " 
	    + classe.getName());
	}
}