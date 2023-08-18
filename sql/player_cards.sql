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
    (25, 'Engineering'),
    (26, 'Acting'),
    (27, 'Comedy'),
    (28, 'Charisma'),
    (29, 'Confidence');


INSERT INTO Cards (card_id, name, category_id,image) 
VALUES 
	(1, 'Beyonce', 1, 'beyonce.png'),
    (2, 'Sinead O''Connor', 1, 'sinead.jpg'),
    (3, 'Frida Kahlo', 1, 'frida.png'),
    (4, 'Taylor Swift', 1, 'taylor.jpg'),
	(5, 'Penelope Cruz', 2, 'penelopecruz.jpg'),
    (6, 'Susan Sarandon', 2, 'sarandon.jpg'),
    (7, 'Whoopi Goldberg', 2, 'whoopi.jpg'),
    (8, 'Meryl Streep', 2, 'streep.jpg'),
    (9, 'Ruth Bader Ginsburg', 3, 'ruth.jpg'),
    (10, 'Hypatia', 3, 'hypatia.jpg'),
    (11, 'Rosa Parks', 3, 'rosa.jpg'),
    (12, 'Florence Given', 4, 'florencegiven.jpg'),
    (13, 'Emily Pankhurst', 4, 'pankhurst.jpg'),
    (14, 'Malala Yousafzai', 4, 'malala.jpg'),
    (15, 'Ada Lovelace', 5, 'ada.jpg'),
    (16, 'Marie Curie', 5, 'mariecurie.jpg'),
    (17, 'Mamie Phipps Clark', 5, 'mamie.jpg'),
    (18, 'Maria Telkes', 5, 'mariatelkes.jpg'),
    (19, 'Beatrice Shilling', 5, 'beatrice.jpg'),
	(20, 'Michelle Obama', 6, 'michelle.jpg'),
	(21, 'Serena Williams', 7, 'serenawilliams.jpeg'),
    (22, 'Fu Yuanhui', 7, 'fuyuanhui.jpg');
    

    
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
    (3, 1, 2),
    (3, 2, 10),
    (3, 3, 10),
    (3, 4, 2),
    (4, 1, 8),
    (4, 2, 10),
    (4, 3, 2),
    (4, 4, 9),
    (5, 26, 8),
    (5, 27, 7),
    (5, 28, 9),
    (5, 29, 9),
    (6, 26, 8),
    (6, 27, 9),
    (6, 28, 8),
    (6, 29, 10),
    (7, 26, 8),
    (7, 27, 10),
    (7, 28, 8),
    (7, 29, 10),
    (8, 9, 10),
    (8, 10, 6),
    (8, 11, 9),
    (8, 12, 8),
    (9, 5, 9),
    (9, 6, 9),
    (9, 7, 6),
    (9, 8, 9),
    (10, 5, 10),
    (10, 6, 3),
    (10, 7, 9),
    (10, 8, 10),
    (11, 5, 8),
    (11, 7, 10),
    (11, 10, 9),
    (11, 8, 10),
    (12, 11, 10),
    (12, 12, 10),
    (12, 13, 9),
    (12, 14, 8),
    (13, 11, 9),
    (13, 12, 10),
    (13, 15, 10),
    (13, 16, 8),
    (14, 11, 6),
    (14, 12, 10),
    (14, 15, 10),
    (14, 16, 10),
    (15, 5, 10),
    (15, 17, 9),
    (15, 18, 8),
    (15, 19, 10),
    (15, 20, 10),
    (15, 21, 9),
    (15, 22, 10),
    (15, 23, 10),
    (15, 24, 8),
    (15, 25, 10),
    (16, 5, 9),
    (16, 17, 10),
    (16, 18, 10),
    (16, 19, 10),
    (16, 20, 9),
    (16, 21, 9),
    (16, 22, 8),
    (16, 23, 9),
    (16, 24, 10),
    (16, 25, 9),
    (17, 5, 9),
    (17, 17, 10),
    (17, 21, 10),
    (17, 22, 8),
    (17, 13, 10),
    (17, 14, 8),
    (18, 5, 9),
    (18, 17, 10),
    (18, 18, 8),
    (18, 19, 10),
    (18, 23, 8),
    (18, 24, 10),
     (19, 5, 9),
    (19, 17, 10),
    (19, 18, 9),
    (19, 19, 10),
    (19, 20, 9),
    (19, 21, 10),
    (19, 22, 8),
    (19, 23, 9),
    (19, 24, 9),
    (19, 25, 8),
    (20, 5, 10),
    (20, 6, 10),
    (20, 15, 10),
    (20, 16, 9),
    (21, 9, 9),
    (21, 10, 9),
    (21, 10, 8),
    (21, 12, 8),
    (22, 9, 8),
    (22, 10, 10),
    (22, 11, 8),
    (22, 12, 7);

  

    
    
    
    
    
    
  

