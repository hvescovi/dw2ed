-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 06-Maio-2022 às 18:16
-- Versão do servidor: 10.2.43-MariaDB-cll-lve
-- versão do PHP: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `hylsonco_poo2`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `hylson_acessorio`
--

CREATE TABLE `hylson_acessorio` (
  `codigo` bigint(20) NOT NULL,
  `descricao` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `hylson_acessorio`
--

INSERT INTO `hylson_acessorio` (`codigo`, `descricao`) VALUES
(9, 'alarme'),
(10, 'bancos de couro');

-- --------------------------------------------------------

--
-- Estrutura da tabela `hylson_cliente`
--

CREATE TABLE `hylson_cliente` (
  `bloqueado` bit(1) NOT NULL,
  `limite_credito` decimal(19,2) DEFAULT NULL,
  `rendaMensal` decimal(19,2) DEFAULT NULL,
  `pessoa_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `hylson_cliente`
--

INSERT INTO `hylson_cliente` (`bloqueado`, `limite_credito`, `rendaMensal`, `pessoa_id`) VALUES
(b'0', 10000.00, 5000.00, 4);

-- --------------------------------------------------------

--
-- Estrutura da tabela `hylson_funcionario`
--

CREATE TABLE `hylson_funcionario` (
  `cargo` varchar(255) DEFAULT NULL,
  `salario` decimal(19,2) DEFAULT NULL,
  `pessoa_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `hylson_funcionario`
--

INSERT INTO `hylson_funcionario` (`cargo`, `salario`, `pessoa_id`) VALUES
('Cientista de Dados', 7850.00, 5);

-- --------------------------------------------------------

--
-- Estrutura da tabela `hylson_pessoa`
--

CREATE TABLE `hylson_pessoa` (
  `id` bigint(20) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `tipoSanguineo` varchar(10) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `hylson_pessoa`
--

INSERT INTO `hylson_pessoa` (`id`, `nome`, `tipoSanguineo`) VALUES
(4, 'João da Silva', 'O+'),
(5, 'Maria Oliveira', 'AB-');

-- --------------------------------------------------------

--
-- Estrutura da tabela `hylson_proprietario`
--

CREATE TABLE `hylson_proprietario` (
  `codigo` bigint(20) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `telefone` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `hylson_proprietario`
--

INSERT INTO `hylson_proprietario` (`codigo`, `email`, `nome`, `telefone`) VALUES
(1, 'josilva@gmail.com', 'João da Silva', '34 1234-5678'),
(6, 'josilva@gmail.com', 'João da Silva', '34 1234-5678');

-- --------------------------------------------------------

--
-- Estrutura da tabela `hylson_veiculo`
--

CREATE TABLE `hylson_veiculo` (
  `codigo` bigint(20) NOT NULL,
  `ano_fabricacao` int(11) NOT NULL,
  `ano_modelo` int(11) NOT NULL,
  `fabricante` varchar(60) NOT NULL,
  `modelo` varchar(60) NOT NULL,
  `valor` decimal(10,2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `hylson_veiculo_com_dono`
--

CREATE TABLE `hylson_veiculo_com_dono` (
  `codigo` bigint(20) NOT NULL,
  `ano_fabricacao` int(11) NOT NULL,
  `ano_modelo` int(11) NOT NULL,
  `fabricante` varchar(60) NOT NULL,
  `modelo` varchar(60) NOT NULL,
  `valor` decimal(10,2) DEFAULT NULL,
  `cod_proprietario` bigint(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `hylson_veiculo_com_dono`
--

INSERT INTO `hylson_veiculo_com_dono` (`codigo`, `ano_fabricacao`, `ano_modelo`, `fabricante`, `modelo`, `valor`, `cod_proprietario`) VALUES
(2, 2012, 2013, 'Honda', 'Civic', 71300.00, 1),
(3, 2003, 2004, 'Ford', 'KA', 14000.00, 1),
(7, 2012, 2013, 'Honda', 'Civic', 71300.00, 6),
(8, 2003, 2004, 'Ford', 'KA', 14000.00, 6);

-- --------------------------------------------------------

--
-- Estrutura da tabela `hylson_veiculo_incrementado`
--

CREATE TABLE `hylson_veiculo_incrementado` (
  `codigo` bigint(20) NOT NULL,
  `ano_fabricacao` int(11) NOT NULL,
  `ano_modelo` int(11) NOT NULL,
  `fabricante` varchar(60) NOT NULL,
  `modelo` varchar(60) NOT NULL,
  `valor` decimal(10,2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `hylson_veiculo_incrementado`
--

INSERT INTO `hylson_veiculo_incrementado` (`codigo`, `ano_fabricacao`, `ano_modelo`, `fabricante`, `modelo`, `valor`) VALUES
(11, 2012, 2013, 'Honda', 'Civic', 71300.00);

-- --------------------------------------------------------

--
-- Estrutura da tabela `hylson_veiculo_incrementado_hylson_acessorio`
--

CREATE TABLE `hylson_veiculo_incrementado_hylson_acessorio` (
  `VeiculoIncrementado_codigo` bigint(20) NOT NULL,
  `acessorios_codigo` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `hylson_veiculo_incrementado_hylson_acessorio`
--

INSERT INTO `hylson_veiculo_incrementado_hylson_acessorio` (`VeiculoIncrementado_codigo`, `acessorios_codigo`) VALUES
(11, 9),
(11, 10);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `hylson_acessorio`
--
ALTER TABLE `hylson_acessorio`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices para tabela `hylson_cliente`
--
ALTER TABLE `hylson_cliente`
  ADD PRIMARY KEY (`pessoa_id`);

--
-- Índices para tabela `hylson_funcionario`
--
ALTER TABLE `hylson_funcionario`
  ADD PRIMARY KEY (`pessoa_id`);

--
-- Índices para tabela `hylson_pessoa`
--
ALTER TABLE `hylson_pessoa`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `hylson_proprietario`
--
ALTER TABLE `hylson_proprietario`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices para tabela `hylson_veiculo`
--
ALTER TABLE `hylson_veiculo`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices para tabela `hylson_veiculo_com_dono`
--
ALTER TABLE `hylson_veiculo_com_dono`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `FKd3q1hgopm5n7r4966s95yrwak` (`cod_proprietario`);

--
-- Índices para tabela `hylson_veiculo_incrementado`
--
ALTER TABLE `hylson_veiculo_incrementado`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices para tabela `hylson_veiculo_incrementado_hylson_acessorio`
--
ALTER TABLE `hylson_veiculo_incrementado_hylson_acessorio`
  ADD PRIMARY KEY (`VeiculoIncrementado_codigo`,`acessorios_codigo`),
  ADD KEY `FKjatxpolq0nwgoq9ksqpc8vvsv` (`acessorios_codigo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
