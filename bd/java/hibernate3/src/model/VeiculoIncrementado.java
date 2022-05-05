package model;

import java.math.BigDecimal;
import java.util.HashSet;
import java.util.Set;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import javax.persistence.Table;

@Entity
@Table(name="hylson_veiculo_incrementado")
public class VeiculoIncrementado {

	private Long codigo;
	private String fabricante;
	private String modelo;
	private Integer anoFabricacao;
	private Integer anoModelo;
	private BigDecimal valor;

	// HashSet em vez de ArrayList
	// para não permitir repetição de acessório
	private Set<Acessorio> acessorios = new HashSet<Acessorio>();
	
	@Id
	@GeneratedValue
	public Long getCodigo() {
		return codigo;
	}
	public void setCodigo(Long codigo) {
		this.codigo = codigo;
	}
	@Column(length=60, nullable=false)
	public String getFabricante() {
		return fabricante;
	}
	public void setFabricante(String fabricante) {
		this.fabricante = fabricante;
	}
	@Column(length=60, nullable=false)
	public String getModelo() {
		return modelo;
	}
	public void setModelo(String modelo) {
		this.modelo = modelo;
	}
	@Column(name = "ano_fabricacao", nullable=false)
	public Integer getAnoFabricacao() {
		return anoFabricacao;
	}
	public void setAnoFabricacao(Integer anoFabricacao) {
		this.anoFabricacao = anoFabricacao;
	}
	@Column(name = "ano_modelo", nullable=false)
	public Integer getAnoModelo() {
		return anoModelo;
	}
	public void setAnoModelo(Integer anoModelo) {
		this.anoModelo = anoModelo;
	}
	@Column(precision = 10, scale = 2, nullable=true)
	public BigDecimal getValor() {
		return valor;
	}
	public void setValor(BigDecimal valor) {
		this.valor = valor;
	}
		
	@ManyToMany
/*	@JoinTable(name = "acessorios_do_veiculo",
	  joinColumns=@JoinColumn(name="cod_veiculo"),
	  inverseJoinColumns=@JoinColumn(name="cod_acessorio"))*/
	public Set<Acessorio> getAcessorios() {
		return acessorios;
	}
	public void setAcessorios(Set<Acessorio> acessorios) {
		this.acessorios = acessorios;
	}	
}