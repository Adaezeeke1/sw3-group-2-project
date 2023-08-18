drop database if exists top_trumps;
create database top_trumps;
use top_trumps;

create table female_icons (
name varchar(50),
attributes varchar(50),
attribute_score int
);



CREATE TABLE Attributes (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE Cards (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE Card_Attribute_Score (
    card_id INT,
    attribute_id INT,
    score INT,
    FOREIGN KEY (card_id) REFERENCES Cards(id),
    FOREIGN KEY (attribute_id) REFERENCES Attributes(id)
);

INSERT INTO Attributes (id, name) 
VALUES 
(1, 'Singing Voice'),
(2, 'Creativity'),
(4, 'Composing'),
(5, 'Intelligence'),
(6, 'Political Influence'),
(7, 'Determination'),
(8, 'Rebellious'),
(10, 'Resilience'),
(11, 'Confidence'),
(12, 'Activism'),
(13, 'Empowerment'),
(14, 'Social Influence'),
(15, 'Leadership'),
(16, 'Inspiration'),
(17, 'Mathematics'),
(18, 'Science'),
(19, 'Chemistry'),
(20, 'Physics'),
(22, 'Research'),
(23, 'Solar Energy'),
(24, 'Innovation'),
(25, 'Engineering');


INSERT INTO Cards (id, name, category_id) 
VALUES 
(1, 'Beyonce', 1),
(2, 'Sinead O''Connor', 1),
(3, 'Ruth Bader Ginsburg', 2),
(4, 'Hypatia', 2),
(5, 'Rosa Parks', 2),
(6, 'Florence Given', 3),
(7, 'Emily Pankhurst', 3),
(8, 'Malala Yousafzai', 3),
(9, 'Ada Lovelace', 4),
(10, 'Marie Curie', 4),
(11, 'Mamie Phipps Clark', 4),
(12, 'Maria Telkes', 4),
(13, 'Beatrice Shilling', 4),
(14, 'Michelle Obama', 5);

INSERT INTO Card_Attribute_Score (card_id, attribute_id, score) 
VALUES 
(1, 1, 10),
(1, 2, 7),
(1, 3, 0),
(1, 4, 5),
(2, 1, 9),
(2, 2, 8),
(2, 3, 0),
(2, 4, 8),
(3, 5, 9),
(3, 6, 9),
(3, 7, 6),
(3, 8, 9);