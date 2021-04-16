package testes;

import java.util.Map;

import aplicacao.GeradorMapaComAnotacao;
import modelo.Telefone;

public class TestarTelefoneMapa {

	public static void main(String args[]) {
		
        Telefone t = new Telefone();
		
		t.setNumero("47 9912 1314");
		t.setOperadora("VIVO");
		t.setCodigoPais("55");
		
		// exibição via toString
		System.out.println("Exibição via toString:");
		System.out.println(t);
		
		// exibição via reflexão
		System.out.println("\nExibição com reflexão:");
		Map<String, Object> props = GeradorMapaComAnotacao.gerarMapaComAnotacao(t);
		for (String prop : props.keySet()) {
			System.out.println(prop + " = " + props.get(prop));
		}
		
		// exibição normal
		System.out.println("\nExibição com gets:");
		System.out.println("Número: " + t.getNumero());
		System.out.println("Operadora: " + t.getOperadora());
		System.out.println("Codigo do país: " + t.getCodigoPais());
		
	}
}