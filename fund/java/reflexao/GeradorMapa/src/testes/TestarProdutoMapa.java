package testes;

import java.util.Map;

import aplicacao.GeradorMapa;
import modelo.Produto;

public class TestarProdutoMapa {

	public static void main(String args[]) {
	
        Produto p = new Produto();
		
		p.setNome("Caderno");
		p.setCategoria("Material escolar");
		p.setPreco(13.00);
		p.setDescricao("Caderno pauta dupla "
				+ "100 páginas tilibra");
		
		System.out.println(p); //invocação método toString
		
		Map<String, Object> props = GeradorMapa.gerarMapa(p);
		for (String prop : props.keySet()) {
			System.out.println(prop + " = " + props.get(prop));
		}
	}
	
}