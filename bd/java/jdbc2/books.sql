-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Tempo de geração: 09-Jun-2021 às 20:08
-- Versão do servidor: 5.7.33
-- versão do PHP: 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `books`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `AuthorISBN`
--

CREATE TABLE `AuthorISBN` (
  `AuthorID` int(11) NOT NULL,
  `ISBN` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `AuthorISBN`
--

INSERT INTO `AuthorISBN` (`AuthorID`, `ISBN`) VALUES
(1, '0132151006'),
(2, '0132151006'),
(3, '0132151006'),
(1, '0132575655'),
(2, '0132575655'),
(1, '013299044X'),
(2, '013299044X'),
(1, '0132990601'),
(2, '0132990601'),
(3, '0132990601'),
(1, '0133807800'),
(2, '0133807800');

-- --------------------------------------------------------

--
-- Estrutura da tabela `Authors`
--

CREATE TABLE `Authors` (
  `AuthorID` int(11) NOT NULL,
  `FirstName` varchar(254) NOT NULL,
  `LastName` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `Authors`
--

INSERT INTO `Authors` (`AuthorID`, `FirstName`, `LastName`) VALUES
(1, 'Paul', 'Deitel'),
(2, 'Harvey', 'Deitel'),
(3, 'Abbey', 'Deitel'),
(4, 'Dan', 'Quirk'),
(5, 'Michael', 'Morgano');

-- --------------------------------------------------------

--
-- Estrutura da tabela `Titles`
--

CREATE TABLE `Titles` (
  `ISBN` varchar(254) NOT NULL,
  `Title` varchar(254) NOT NULL,
  `EditionNumber` int(254) NOT NULL,
  `Copyright` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `Titles`
--

INSERT INTO `Titles` (`ISBN`, `Title`, `EditionNumber`, `Copyright`) VALUES
('0132151006', 'Internet & World Wide Web How to Program', 5, '2012'),
('0132575655', 'Java How to Program, Late Objects Version', 10, '2015'),
('013299044X', 'C How to Program', 7, '2013'),
('0132990601', 'Simply Visual Basic 2010', 4, '2013'),
('0133807800', 'Java How to Program', 10, '2015');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `AuthorISBN`
--
ALTER TABLE `AuthorISBN`
  ADD PRIMARY KEY (`AuthorID`,`ISBN`),
  ADD KEY `ISBN` (`ISBN`);

--
-- Índices para tabela `Authors`
--
ALTER TABLE `Authors`
  ADD PRIMARY KEY (`AuthorID`);

--
-- Índices para tabela `Titles`
--
ALTER TABLE `Titles`
  ADD PRIMARY KEY (`ISBN`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `Authors`
--
ALTER TABLE `Authors`
  MODIFY `AuthorID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `AuthorISBN`
--
ALTER TABLE `AuthorISBN`
  ADD CONSTRAINT `AuthorISBN_ibfk_1` FOREIGN KEY (`AuthorID`) REFERENCES `Authors` (`AuthorID`),
  ADD CONSTRAINT `AuthorISBN_ibfk_2` FOREIGN KEY (`ISBN`) REFERENCES `Titles` (`ISBN`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
