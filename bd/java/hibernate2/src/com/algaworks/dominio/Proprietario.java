package com.algaworks.dominio;

import java.util.List;
//import com.algaworks.dominio.Veiculo;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

// pgs 75 e 77, seção 4.10

@Entity
@Table(name = "proprietario")
public class Proprietario {

	private Long codigo;
	private String nome;
	private String telefone;
	private String email;
	
	private List<VeiculoComDono> veiculos;
	
	@Id
	@GeneratedValue
	public Long getCodigo() {
		return codigo;
	}
	public void setCodigo(Long codigo) {
		this.codigo = codigo;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getTelefone() {
		return telefone;
	}
	public void setTelefone(String telefone) {
		this.telefone = telefone;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	@OneToMany(mappedBy = "proprietario")
	public List<VeiculoComDono> getVeiculos() {
		return veiculos;
	}
	public void setVeiculos(List<VeiculoComDono> veiculos) {
		this.veiculos = veiculos;
	}
	
	
}
