/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

import java.math.BigDecimal;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.PrimaryKeyJoinColumn;
import javax.persistence.Table;

@Entity
@Table(name="hylson_cliente")
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
