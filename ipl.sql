-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 20, 2020 at 04:47 PM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `ipl`
--

-- --------------------------------------------------------

--
-- Table structure for table `club`
--

CREATE TABLE IF NOT EXISTS `club` (
  `clid` int(11) NOT NULL AUTO_INCREMENT,
  `club` varchar(50) NOT NULL,
  `owner` varchar(100) NOT NULL,
  `venue` varchar(100) NOT NULL,
  `coach` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`clid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `club`
--

INSERT INTO `club` (`clid`, `club`, `owner`, `venue`, `coach`, `email`, `password`, `status`) VALUES
(1, 'Rajasthan Royals', 'Royal Multisport Pvt. Ltd', 'Sawai Mansingh Stadium', 'Andrew McDonald', 'rajsthanroyals@gmail.com', '123', 'Approve'),
(3, 'Royal Challengers Bangalore', 'Royal Challengers Sports Private Ltd', 'M. Chinnaswamy Stadium', 'Simon Katich', 'royal@gmail.com', '123456', 'Approve');

-- --------------------------------------------------------

--
-- Table structure for table `complaints`
--

CREATE TABLE IF NOT EXISTS `complaints` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `clid` int(11) NOT NULL,
  `complaints` varchar(100) NOT NULL,
  `cdate` varchar(50) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `complaints`
--


-- --------------------------------------------------------

--
-- Table structure for table `cust_reg`
--

CREATE TABLE IF NOT EXISTS `cust_reg` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `cust_reg`
--

INSERT INTO `cust_reg` (`cid`, `cname`, `address`, `gender`, `email`, `mobile`, `password`) VALUES
(1, 'Jithin', 'LCC', 'Male', 'jithin@gmail.com', '9638527410', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `clid` int(11) NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `fdate` varchar(50) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `feedback`
--


-- --------------------------------------------------------

--
-- Table structure for table `fixtures`
--

CREATE TABLE IF NOT EXISTS `fixtures` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `teamone` varchar(50) NOT NULL,
  `teamtwo` varchar(50) NOT NULL,
  `venue` varchar(100) NOT NULL,
  `mdate` varchar(50) NOT NULL,
  `mtime` varchar(50) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `fixtures`
--

INSERT INTO `fixtures` (`fid`, `teamone`, `teamtwo`, `venue`, `mdate`, `mtime`) VALUES
(1, 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Thazhathupally Forona', '2020-04-23', '4 pm');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `uname` varchar(50) NOT NULL,
  `pass` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`uname`, `pass`, `utype`) VALUES
('rajsthanroyals@gmail.com', '123', 'Club'),
('royal@gmail.com', '123456', 'Club'),
('admin@gmail.com', 'admin', 'Admin'),
('jithin@gmail.com', '123456', 'Customer');

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE IF NOT EXISTS `news` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `clid` int(11) NOT NULL,
  `news` varchar(100) NOT NULL,
  `details` varchar(4000) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`nid`, `clid`, `news`, `details`, `image`) VALUES
(1, 3, 'April 20 - RCB dismantle defending champions RR', 'The beginning of the 2009 season brought with it renewed hope. RCB had invested heavily in matchwinners in the auction.', 'static/media/RCBvRR%202009.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `player`
--

CREATE TABLE IF NOT EXISTS `player` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `player` varchar(50) NOT NULL,
  `team` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `matches` int(11) NOT NULL,
  `totalruns` int(11) NOT NULL,
  `totalwickets` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `player`
--

INSERT INTO `player` (`pid`, `player`, `team`, `type`, `category`, `matches`, `totalruns`, `totalwickets`, `image`) VALUES
(1, 'Virat Kohli', '3', 'Batsman', 'Indian', 177, 5412, 4, 'static/media/ae12a1ac618ea08d3b.jpg');
