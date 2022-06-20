/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

/**
 *
 * @author EduardoVM
 */
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Table;
/**
 *
 * @author EduardoVM
 */
@Entity
@Table(name = "pgm4_hylson_pessoa") 
public class Pessoa {
@Id
@GeneratedValue(strategy = GenerationType.SEQUENCE, generator="pgm4_hylson_pessoa_seq")
@SequenceGenerator(name = "pgm4_hylson_pessoa_seq", initialValue = 1)
    Long id;
    String nome;
    String email;
    Float peso;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Float getPeso() {
        return peso;
    }

    public void setPeso(Float peso) {
        this.peso = peso;
    }

    public Pessoa(String nome, String email, Float peso) {
        this.nome = nome;
        this.email = email;
        this.peso = peso;
    }
}

