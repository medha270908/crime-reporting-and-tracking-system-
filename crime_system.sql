-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 12, 2026 at 05:37 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crime_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `crimes`
--

CREATE TABLE `crimes` (
  `track_id` varchar(10) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `crime_type` varchar(30) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `urgency` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `crimes`
--

INSERT INTO `crimes` (`track_id`, `name`, `gender`, `email`, `phone`, `crime_type`, `description`, `date`, `location`, `urgency`) VALUES
('CR5531', 'rani', 'Female', 'rani123@gmail.com', '123456789', 'Cyber Crime', 'fake calling\n', '3/19/26', NULL, NULL),
('CR3910', 'medha', 'Female', 'medha123@gmail.com', '123456789', 'Fraud', 'fraud done\n', '3/29/26', NULL, NULL),
('CR1391', 'Rakshit', 'Male', 'upadhyayrakshit123@gmail.com', '7094567890', 'Assault', 'i was assaulted\n', '4/11/26', 'mumbai', 'Medium'),
('CR5339', 'Medha', 'Female', 'upadhyaymedha2008@gmail.com', '7021830272', 'Robbery', 'i have got robbed\n', '4/9/26', 'mumbai', 'Medium'),
('CR4406', 'ruru', 'Female', 'ruru12@gmail.com', '890567234', 'Cyber Crime', 'fake calls\n', '4/10/26', 'mumbai', 'Low');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  `role` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `role`) VALUES
('admin', '1234', 'Admin'),
('Medha12!@', 'Medha12!@', 'Customer');

-- --------------------------------------------------------

--
-- Table structure for table `reports`
--

CREATE TABLE `reports` (
  `id` int(11) NOT NULL,
  `issue` varchar(255) DEFAULT NULL,
  `area` varchar(100) DEFAULT NULL,
  `severity` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reports`
--

INSERT INTO `reports` (`id`, `issue`, `area`, `severity`) VALUES
(1, 'online calls', 'Bandra', 'High'),
(2, 'harming people', 'Dadar', 'Medium'),
(3, 'attack', 'Andheri', 'Low');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `reports`
--
ALTER TABLE `reports`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `reports`
--
ALTER TABLE `reports`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
