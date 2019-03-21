-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  jeu. 21 mars 2019 à 10:30
-- Version du serveur :  5.7.21
-- Version de PHP :  7.1.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `stats_nba`
--

-- --------------------------------------------------------

--
-- Structure de la table `equipe_nba`
--

DROP TABLE IF EXISTS `equipe_nba`;
CREATE TABLE IF NOT EXISTS `equipe_nba` (
  `idEquipe` int(11) NOT NULL,
  `Nom` varchar(64) NOT NULL,
  PRIMARY KEY (`idEquipe`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `joueur_nba`
--

DROP TABLE IF EXISTS `joueur_nba`;
CREATE TABLE IF NOT EXISTS `joueur_nba` (
  `idJoueur` int(11) NOT NULL,
  `Nom` varchar(64) NOT NULL,
  PRIMARY KEY (`idJoueur`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `match_nba`
--

DROP TABLE IF EXISTS `match_nba`;
CREATE TABLE IF NOT EXISTS `match_nba` (
  `idMatch` int(11) NOT NULL,
  `idEquipeDom` int(11) NOT NULL,
  `idEquipeExt` int(11) NOT NULL,
  `saison` varchar(16) NOT NULL,
  `date` date NOT NULL,
  `resultatFinal` int(11) NOT NULL,
  PRIMARY KEY (`idMatch`),
  KEY `idEquipeDom_fk` (`idEquipeDom`),
  KEY `idEquipeExt_fk` (`idEquipeExt`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `quart_temps_nba`
--

DROP TABLE IF EXISTS `quart_temps_nba`;
CREATE TABLE IF NOT EXISTS `quart_temps_nba` (
  `numQT` int(11) NOT NULL,
  `idMatch` int(11) NOT NULL,
  `idEquipe` int(11) NOT NULL,
  `idJoueur` int(11) NOT NULL,
  `positionDepart` varchar(8) NOT NULL,
  `tempsDeJeu` varchar(8) NOT NULL,
  `fgm` int(11) NOT NULL,
  `fga` int(11) NOT NULL,
  `fg_pct` int(11) NOT NULL,
  `fg3m` int(11) NOT NULL,
  `ftm` int(11) NOT NULL,
  `fta` int(11) NOT NULL,
  `ft_pct` int(11) NOT NULL,
  `oreb` int(11) NOT NULL,
  `dreb` int(11) NOT NULL,
  `ast` int(11) NOT NULL,
  `stl` int(11) NOT NULL,
  `blk` int(11) NOT NULL,
  `turnover` int(11) NOT NULL,
  `pf` int(11) NOT NULL,
  `pts` int(11) NOT NULL,
  `plus_minus` int(11) NOT NULL,
  `e_off_rating` int(11) NOT NULL,
  `off_rating` int(11) NOT NULL,
  `e_def_rating` int(11) NOT NULL,
  `def_rating` int(11) NOT NULL,
  `e_net_rating` int(11) NOT NULL,
  `net_rating` int(11) NOT NULL,
  PRIMARY KEY (`idMatch`,`idJoueur`,`numQT`) USING BTREE,
  KEY `idEquipeQT_fk` (`idEquipe`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `stats_equipe_match_nba`
--

DROP TABLE IF EXISTS `stats_equipe_match_nba`;
CREATE TABLE IF NOT EXISTS `stats_equipe_match_nba` (
  `idEquipe` int(11) NOT NULL,
  `idMatch` int(11) NOT NULL,
  `fgm` int(11) NOT NULL,
  `fga` int(11) NOT NULL,
  `fg_pct` int(11) NOT NULL,
  `fg3m` int(11) NOT NULL,
  `fg3a` int(11) NOT NULL,
  `fg3_pct` int(11) NOT NULL,
  `ftm` int(11) NOT NULL,
  `fta` int(11) NOT NULL,
  `ft_pct` int(11) NOT NULL,
  `oreb` int(11) NOT NULL,
  `dreb` int(11) NOT NULL,
  `reb` int(11) NOT NULL,
  `ast` int(11) NOT NULL,
  `stl` int(11) NOT NULL,
  `blk` int(11) NOT NULL,
  `turnover` int(11) NOT NULL,
  `pf` int(11) NOT NULL,
  `pts` int(11) NOT NULL,
  `plus_minus` int(11) NOT NULL,
  `min` int(11) NOT NULL,
  PRIMARY KEY (`idEquipe`,`idMatch`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `match_nba`
--
ALTER TABLE `match_nba`
  ADD CONSTRAINT `idEquipeDom_fk` FOREIGN KEY (`idEquipeDom`) REFERENCES `equipe_nba` (`idEquipe`),
  ADD CONSTRAINT `idEquipeExt_fk` FOREIGN KEY (`idEquipeExt`) REFERENCES `equipe_nba` (`idEquipe`);

--
-- Contraintes pour la table `quart_temps_nba`
--
ALTER TABLE `quart_temps_nba`
  ADD CONSTRAINT `idEquipeQT_fk` FOREIGN KEY (`idEquipe`) REFERENCES `equipe_nba` (`idEquipe`),
  ADD CONSTRAINT `idMatchQT_fk` FOREIGN KEY (`idMatch`) REFERENCES `match_nba` (`idMatch`);

--
-- Contraintes pour la table `stats_equipe_match_nba`
--
ALTER TABLE `stats_equipe_match_nba`
  ADD CONSTRAINT `idEquipeStats_fk` FOREIGN KEY (`idEquipe`) REFERENCES `equipe_nba` (`idEquipe`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
