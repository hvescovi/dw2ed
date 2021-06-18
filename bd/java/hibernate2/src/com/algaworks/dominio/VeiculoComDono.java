package com.algaworks.dominio;

import java.math.BigDecimal;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

@Entity
@Table(name="veiculo_com_dono")
public class VeiculoComDono {

	private Long codigo;
	private String fabricante;
	private String modelo;
	private Integer anoFabricacao;
	private Integer anoModelo;
	private BigDecimal valor;
	
	private Proprietario proprietario;
	
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
	@ManyToOne
	@JoinColumn(name = "cod_proprietario")
	public Proprietario getProprietario() {
		return proprietario;
	}
	public void setProprietario(Proprietario proprietario) {
		this.proprietario = proprietario;
	}	
}