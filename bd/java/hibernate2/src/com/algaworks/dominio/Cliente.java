package com.algaworks.dominio;

import java.math.BigDecimal;

import javax.persistence.Column;
import javax.persistence.DiscriminatorValue;
import javax.persistence.Entity;
import javax.persistence.PrimaryKeyJoinColumn;

@Entity
@PrimaryKeyJoinColumn(name = "pessoa_id")
public class Cliente extends Pessoa {

	private BigDecimal limiteCredito;
	private BigDecimal rendaMensal;
	private boolean Bloqueado;
	
	@Column(name = "limite_credito", nullable=true)
	public BigDecimal getLimiteCredito() {
		return limiteCredito;
	}
	public void setLimiteCredito(BigDecimal limiteCredito) {
		this.limiteCredito = limiteCredito;
	}
	public BigDecimal getRendaMensal() {
		return rendaMensal;
	}
	public void setRendaMensal(BigDecimal rendaMensal) {
		this.rendaMensal = rendaMensal;
	}
	public boolean isBloqueado() {
		return Bloqueado;
	}
	public void setBloqueado(boolean bloqueado) {
		Bloqueado = bloqueado;
	}
	
}
