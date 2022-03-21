package reflexao;

import java.lang.reflect.Method;

public class ExecutandoMetodo {

	public static void main(String args[]) {
		
		// classe local
		class Pessoa {
			String nome;
			String telefone;
			
			public void enviarMensagemWhats(String msg) {
				System.out.println(nome+
				  " enviou via whats ("+telefone+"): "+ msg);
			}
			@Override
			public String toString() {
				return nome + ", " + telefone;
			}
		}
		
		Pessoa joao = new Pessoa();
		joao.nome = "Joao da Silva";
		joao.telefone = "12341234";
		System.out.println(joao);
		joao.enviarMensagemWhats("bom dia");
				
		Method m;
		try {
			m = acharMetodoPeloNome(Pessoa.class, "enviarMensagemWhats");
			m.invoke(joao, "tudo bem com vocês?");
		} catch (Exception e) {
			e.printStackTrace();
		}				
	}	
	
	public static Method acharMetodoPeloNome(Class<?> c, String nome) throws Exception {
		for (Method m : c.getMethods()) {
			if (m.getName().equals(nome)) {
				return m;
			}
		}
		throw new Exception("Método " + nome + " não encontrado");
	}
}