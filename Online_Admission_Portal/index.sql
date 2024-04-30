
CREATE TABLE IF NOT EXISTS attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_number VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE student (
    roll_number int primary key,
    name VARCHAR(100)
);
INSERT INTO student (roll_number, name) VALUES
('1', 'Muhammad Haziqul Khair'),
('2', 'Hiba Imran'),
('3', 'Mehwish Naz'),
('4', 'Zulquar Nain'),
('5', 'Abdullah'),
('6', 'Muhammad Usman'),
('7', 'Abdul Sattar Samoo'),
('8', 'Muzzamil'),
('9', 'Muheeb Ur Rehman'),
('10', 'Mursalin Ahmed'),
('11', 'Mohammad Haseeb'),
('12', 'Imran'),
('13', 'Anees Ur Rehman'),
('15', 'Rahul Kumar'),
('16', 'Arsalan'),
('17', 'Amar Sham'),
('18', 'Altaf Younis'),
('20', 'Yousra'),
('21', 'Ammad Aziz'),
('22', 'Urooj Fatima'),
('24', 'Sarang Hussain'),
('25', 'Sarfaraz Ali'),
('26', 'Abdul Hameed'),
('28', 'Muhammad Raza Abbas'),
('29', 'Abdul Wasiu'),
('30', 'Noman Irfan'),
('31', 'Ameer Ali'),
('33', 'Anzar Ahmed'),
('34', 'Jahangir'),
('35', 'Basit Ali'),
('36', 'Darshan'),
('37', 'Aakash Awais'),
('38', 'Abdul Haseeb'),
('39', 'Sajad Hussain'),
('41', 'Rayan'),
('43', 'Nawail Khan'),
('44', 'Muhammad Ahmed'),
('45', 'Bushra Laraib'),
('46', 'Umair');
select * from attendance;