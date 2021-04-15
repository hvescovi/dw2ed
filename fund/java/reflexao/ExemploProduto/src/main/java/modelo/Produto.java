package modelo;

public class Produto {
 
	private String nome;
    private String categoria;
    private Double preco;
    private String descricao;

	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getCategoria() {
		return categoria;
	}
	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}
	public Double getPreco() {
		return preco;
	}
	public void setPreco(Double preco) {
		this.preco = preco;
	}
	public String getDescricao() {
		return descricao;
	}
	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}
	
	@Override
	public String toString() {
		return "Produto [nome=" + nome + ", categoria=" + 
	        categoria + ", preco=" + preco + ", "
			+ "descricao=" + descricao
			+ "]";
	}
	
	public static void main(String args[]) {
		System.out.println("Hello");
	}

}