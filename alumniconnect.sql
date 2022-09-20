-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 20, 2022 at 07:58 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alumniconnect`
--

-- --------------------------------------------------------

--
-- Table structure for table `alumni_students`
--

CREATE TABLE `alumni_students` (
  `register_no` varchar(15) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email_ID` varchar(45) NOT NULL,
  `phone_no` varchar(12) NOT NULL,
  `college_name` varchar(100) DEFAULT NULL,
  `DOB` varchar(15) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `confirm_password` varchar(20) NOT NULL,
  `linkedin_profile` text DEFAULT NULL,
  `github_profile` text DEFAULT NULL,
  `other_links` text DEFAULT NULL,
  `profile_pic` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `alumni_students`
--

INSERT INTO `alumni_students` (`register_no`, `first_name`, `last_name`, `email_ID`, `phone_no`, `college_name`, `DOB`, `Gender`, `password`, `confirm_password`, `linkedin_profile`, `github_profile`, `other_links`, `profile_pic`) VALUES
('2132241030003', 'Ranveer', 'Singh', 'rs2013@srmist.edu.in', '9084897342', NULL, '15-06-1996', 'Male', 'abc@123', 'abc@123', NULL, NULL, NULL, NULL),
('2132241030005', 'Ajay', 'Rajput', 'ar2340@srmist.edu.in', '9354687412', NULL, '1998-01-02', 'Male', 'ajay123', 'ajay123', NULL, NULL, NULL, NULL),
('2132241030013', 'Alina', 'Gomez', 'ag1234@srmist.edu.in', '9354687412', NULL, '1981-06-14', 'Female', 'abc123', 'abc123', NULL, NULL, NULL, NULL),
('2132241030015', 'Rahul', 'Sani', 'rs2456@srmist.edu.in', '9354265412', NULL, '1996-06-20', 'Male', 'rahul123', 'rahul123', NULL, NULL, NULL, NULL),
('2132241030016', 'Anamika', 'Srivastava', 'as4024@srmist.edu.in', '9084567412', NULL, '1995-12-15', 'Female', 'anamika123', 'anamika123', NULL, NULL, NULL, NULL),
('2132241030017', 'Anushka', 'Tiwari', 'at4894@srmist.edu.in', '9084567445', NULL, '1999-02-04', 'Female', 'anushka123', 'anushka123', NULL, NULL, NULL, NULL),
('RA193524102001', 'Rahul', 'Sinha', 'rs1254@srmist.edu.in', '9354214512', NULL, '1994-08-25', 'Male', 'rahul123', 'rahul123', NULL, NULL, NULL, NULL),
('RA2132241030056', 'Salman', 'Shekh', 'ss4923@srmist.edu.in', '9084897541', NULL, '1991-10-05', 'Male', 'salman123', 'rahul123', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `current_students`
--

CREATE TABLE `current_students` (
  `register_no` varchar(15) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email_ID` varchar(45) NOT NULL,
  `phone_no` varchar(12) NOT NULL,
  `college_name` varchar(45) DEFAULT NULL,
  `DOB` varchar(15) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `password` varchar(15) NOT NULL,
  `confirm_password` int(15) NOT NULL,
  `linkedin_profile` text DEFAULT NULL,
  `github_profile` text DEFAULT NULL,
  `other_links` text DEFAULT NULL,
  `profile_pic` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alumni_students`
--
ALTER TABLE `alumni_students`
  ADD PRIMARY KEY (`register_no`),
  ADD UNIQUE KEY `register_no` (`register_no`),
  ADD UNIQUE KEY `email_ID` (`email_ID`);

--
-- Indexes for table `current_students`
--
ALTER TABLE `current_students`
  ADD PRIMARY KEY (`register_no`),
  ADD UNIQUE KEY `std_ID_UNIQUE` (`register_no`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
