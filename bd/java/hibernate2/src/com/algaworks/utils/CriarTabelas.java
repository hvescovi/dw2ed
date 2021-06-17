package com.algaworks.utils;

import javax.persistence.Persistence;

public class CriarTabelas {

	public static void main(String[] args) {
		Persistence.createEntityManagerFactory("AlgaWorksPU");
	}

}
