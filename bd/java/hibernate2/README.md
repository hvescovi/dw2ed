Códigos básicos de exemplos do livro:

THIAGO, Faria; JUNIOR, Normandes. JPA e Hibernate. 2015, AlgaWorks Softwares, Treinamentos e Serviços LTDA.

* Driver mysql adicionado do projeto hibernate

https://mvnrepository.com/artifact/mysql/mysql-connector-java/8.0.25

* Hibernate adicionado de diretório de downloads. São muitos arquivos, da pasta /lib/required, e não foram incluídos neste repositório. 

hibernate.org

Exemplos deste projeto:

* Mínimo: classes Veiculo e TestarVeiculos
* Desanexando e sincronizando objetos: TestarVeiculoDesanexado
* Composição/agregação (relação 1 x N): classes VeiculoComDono, Proprietario e TestarProprietario
* Relacionamento N x N: VeiculoIncrementado, Acessorio e TestarVeiculoIncrementado
* Herança: Pessoa, Funcionario, Cliente e TestarHeranca

Conceitos do livro: 

* Objetos embutidos: mais de um objeto/classe em uma única tabela (tabela desnormalizada, sistemas legados, relacionamento 1 x 1, , menos relacionamentos)

* Estratégia de carregamento de dados

> Lazy loading: carregamento de dados apenas quando forem utilizados (métodos get). Essa é a estratégia padrão.
@OneToMany(fetch = FetchType.LAZY)

> Eager loading: carregamento de dados já quando o objeto for buscado/localizado
@OneToMany(fetch = FetchType.EAGER)

* Operações em cascata

> Quando persistir um objeto, persistir também seus relacionamentos transientes (ainda não persistidos)
@OneToMany(cascade = CascadeType.PERSIST)

> CascadeType.ALL: todas as operações ocorrerão em cascata

> CascadeType.REMOVE: exclusão em cascata