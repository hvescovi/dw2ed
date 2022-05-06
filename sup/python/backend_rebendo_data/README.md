Solução alternativa para tratamento de DATAS em JSON, ao receber dados no back-end.

* dividir a data em suas partes (ano, mes dia)
```partes = dados['dtnasc'].split("-")```

* substituir o item original do dicionário por um valor do python (conforme exemplo em modelo.py)

```dados['dtnasc'] = date(int(partes[0]), int(partes[1]), int(partes[2]))```
