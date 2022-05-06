/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Inheritance;
import javax.persistence.InheritanceType;
import javax.persistence.Table;

@Entity
@Table(name="hylson_pessoa")
//1 tabela para cada classe (abstrata e concretas)
@Inheritance(strategy=InheritanceType.JOINED)
// SINGLE_TABLE: tabela única para todas as classes
//   nesse caso, há um campo discriminatório (tipo = "C", tipo = "F")
// TABLE_PER_CLASS: uma tabela para cada classe concreta
//   repetição dos atributos da superclasse nas subclasses
public abstract class Pessoa {
	
	private Long id;
	private String nome;
	private String tipoSanguineo;
	
	@Id
	@GeneratedValue
	public Long getId() {
		return id;
	}
	public void setId(Long id) {
		this.id = id;
	}
	@Column(nullable=false)
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	@Column(length=10)
	public String getTipoSanguineo() {
		return tipoSanguineo;
	}
	public void setTipoSanguineo(String tipoSanguineo) {
		this.tipoSanguineo = tipoSanguineo;
	}
}