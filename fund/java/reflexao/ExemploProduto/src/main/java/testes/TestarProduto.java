package testes;

import modelo.Produto;

public class TestarProduto {

	public static void main(String[] args) {
		Produto p = new Produto();
		
		p.setNome("Caderno");
		p.setCategoria("Material escolar");
		p.setPreco(13.00);
		p.setDescricao("Caderno pauta dupla "
				+ "100 páginas tilibra");
		
		System.out.println(p);
	}

}