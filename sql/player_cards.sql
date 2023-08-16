DROP DATABASE IF EXISTS player_cards;
CREATE DATABASE player_cards;
USE player_cards;

CREATE TABLE Categories (
    category_id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE Attributes (
    attribute_id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE Cards (
    card_id INT PRIMARY KEY,
    name VARCHAR(255),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id),
    image VARCHAR(225)
);

CREATE TABLE Card_Attribute_Score (
    card_id INT,
    attribute_id INT,
    score INT,
    FOREIGN KEY (card_id) REFERENCES Cards(card_id),
    FOREIGN KEY (attribute_id) REFERENCES Attributes(attribute_id)
);
    
INSERT INTO Categories (category_id, name) 
VALUES 
    (1, 'Artist'),
    (2, 'Actors'),
    (3, 'Academic'),
    (4, 'Activist'),
    (5, 'Scientist'),
    (6, 'Politician'),
    (7, 'Sports');

    

INSERT INTO Attributes (attribute_id, name) 
VALUES 
    (1, 'Singing Voice'),
    (2, 'Creativity'),
    (3, 'Painting'),
    (4, 'Composing'),
    (5, 'Abstract Intelligence'),
    (6, 'Political Influence'),
    (7, 'Determination'),
    (8, 'Rebellious'),
    (9, 'Courage'),
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
    (21, 'Psychology'),
    (22, 'Research'),
    (23, 'Solar Energy'),
    (24, 'Innovation'),
    (25, 'Engineering');


INSERT INTO Cards (card_id, name, category_id,image) 
VALUES 
    (1, 'Beyonce', 1, 'beyonce.png'),
    (2, 'Sinead O''Connor', 1, 'sinead.jpg'),
    (3, 'Ruth Bader Ginsburg', 2,'ruth.jpg'),
    (4, 'Hypatia', 2, 'hypatia.jpg'),
    (5, 'Rosa Parks', 2, 'rosa.jpg'),
    (6, 'Florence Given', 3, 'florencegiven.jpg'),
    (7, 'Emily Pankhurst', 3, 'pankhurst.jpg'),
    (8, 'Malala Yousafzai', 3, 'malala.jpg'),
    (9, 'Ada Lovelace', 4, 'ada.jpg'),
    (10, 'Marie Curie', 4, 'mariecurie.jpg'),
    (11, 'Mamie Phipps Clark', 4, 'mamie.jpg'),
    (12, 'Maria Telkes', 4, 'mariatelkes.jpg'),
    (13, 'Beatrice Shilling', 4, 'beatrice.jpg'),
    (14, 'Michelle Obama', 5, 'michelle.jpg'),
    (15, 'Penelope Cruz', 2, 'penelopecruz.jpg'),
    (16, 'Whoopi Goldberg', 2, 'whoopi.jpg'),
    (17, 'Meryl Streep', 2, 'streep.jpg'),
    (18, 'Susan Sarandon', 2, 'sarandon.jpg'),
    (19, 'Serena Williams', 7, 'serenawilliams.jpeg'),
    (20, 'Fu Yuanhui', 7, 'fuyuanhui.jpg');


-- Artist
INSERT INTO Card_Attribute_Score (card_id, attribute_id, score) 
VALUES 
    (3, 5, 9),
    (3, 6, 9),
    (4, 5, 10),
    (4, 6, 3),
    (4, 7, 9),
    (4, 8, 10);

-- Actors
INSERT INTO Card_Attribute_Score (card_id, attribute_id, score) 
VALUES 
    (15, 9, 8),
    (15, 10, 7),
    (15, 11, 9),
    (15, 12, 9),
    (16, 9, 8),
    (16, 10, 9),
    (16, 11, 8),
    (16, 12, 10),
    (17, 9, 10),
    (17, 10, 6),
    (17, 11, 9),
    (17, 12, 8),
    (18, 9, 9),
    (18, 10, 8),
    (18, 11, 7),
    (18, 12, 7);

-- Academic
INSERT INTO Card_Attribute_Score (card_id, attribute_id, score) 
VALUES 
    (3, 5, 9),
    (3, 6, 9),
    (5, 5, 8),
    (5, 6, 10),
    (5, 7, 9),
    (5, 8, 10);

-- Activist
INSERT INTO Card_Attribute_Score (card_id, attribute_id, score) 
VALUES 
    (6, 11, 10),
    (6, 12, 10),
    (6, 13, 9),
    (6, 14, 8),
    (7, 11, 9),
    (7, 12, 10),
    (7, 13, 10),
    (7, 14, 8),
    (8, 11, 6),
    (8, 12, 10),
    (8, 13, 10),
    (8, 14, 10);

-- Scientist
INSERT INTO Card_Attribute_Score (card_id, attribute_id, score) 
VALUES 
    (9, 5, 10),
    (9, 17, 9),
    (9, 18, 8),
    (9, 19, 10),
    (9, 20, 9),
    (9, 21, 10),
    (9, 22, 9),
    (9, 23, 10),
    (9, 24, 9),
    (9, 25, 10),
    (10, 5, 9),
    (10, 17, 10),
    (10, 18, 10),
    (10, 19, 10),
    (10, 20, 9),
    (10, 21, 9),
    (10, 22, 8),
    (10, 23, 9),
    (10, 24, 10),
    (10, 25, 9),
    (11, 5, 9),
    (11, 17, 10),
    (11, 18, 9),
    (11, 19, 8),
    (11, 20, 9),
    (11, 21, 8),
    (11, 22, 9),
    (11, 23, 10),
    (11, 24, 8),
    (11, 25, 9),
    (12, 5, 9),
    (12, 17, 10),
    (12, 18, 8),
    (12, 19, 8),
    (12, 20, 10),
    (12, 21, 8),
    (12, 22, 10),
    (12, 23, 9),
    (12, 24, 9),
    (12, 25, 8),
    (13, 5, 9),
    (13, 17, 10),
    (13, 18, 10),
    (13, 19, 10),
    (13, 20, 9),
    (13, 21, 9),
    (13, 22, 10),
    (13, 23, 10),
    (13, 24, 8),
   (13, 25, 9);

-- Politician
INSERT INTO Card_Attribute_Score (card_id, attribute_id, score) 
VALUES 
(14, 5, 10),
(14, 6, 10),
(14, 15, 10),
(14, 16, 9);

-- Sports
INSERT INTO Card_Attribute_Score (card_id, attribute_id, score) 
VALUES 
(19, 9, 9),
(19, 10, 9),
(19, 10, 9),
(19, 12, 8),
(20, 9, 8),
(20, 10, 10),
(20, 11, 8),
(20, 12, 7);


