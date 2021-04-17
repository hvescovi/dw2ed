package reflexao;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;

public class CriandoInstancia {

	public static void main(String args[]) {
		
		// classe local
		class Pessoa {
			String nome;
			String telefone;
			
			@Override
			public String toString() {
				return nome + ", " + telefone;
			}
		}
		
		// instanciando normalmente
		Pessoa joao = new Pessoa();
		joao.nome = "Joao da Silva";
		joao.telefone = "12341234";
		System.out.println(joao);
		
		// instanciando via reflexão
		
		// obtém referência da classe
		Class<?> cla = Pessoa.class;
		try {			
			// obtém o primeiro (e único) construtor
			Constructor c = cla.getDeclaredConstructors()[0];
			
			try {
				// cria a instância!
				Pessoa maria = (Pessoa) c.newInstance();
				maria.nome = "Maria Oliveira";
				maria.telefone = "91929394";
				System.out.println(maria);
			} catch (InstantiationException | IllegalAccessException 
					| IllegalArgumentException 
					| InvocationTargetException e) {
				e.printStackTrace();
			}							
		} catch (SecurityException e) {
			e.printStackTrace();
		}
	}	
}