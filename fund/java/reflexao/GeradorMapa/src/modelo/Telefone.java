package modelo;

import aplicacao.GeradorMapaComAnotacao.Ignorar;
import aplicacao.GeradorMapaComAnotacao.NomePropriedade;

public class Telefone {

	private String numero;
	public String codigoPais;
	private String operadora;
	
	public String getNumero() { return numero; }
	public void setNumero(String n) { numero = n; }
	
	// anotação para permitir acesso ao campo de outra forma
	// similar a um "alias"
	@NomePropriedade("codigoInternacional")
	public String getCodigoPais() {	return codigoPais; }
	
	public void setCodigoPais(String codp) { codigoPais = codp; }
	
	// anotacao para ignorar este método 
	@Ignorar
	public String getOperadora() { return operadora; }
	
	public void setOperadora(String op) { operadora = op; }
	
	@Override
	public String toString() {
		return "Telefone [numero=" + numero + ", codigoPais=" 
	    + codigoPais + ", operadora=" + operadora + "]";
	}
	
	
}