DROP DATABASE IF EXISTS player_cards;
CREATE DATABASE player_cards;
USE player_cards;

CREATE TABLE Categories (
    category_id INT PRIMARY KEY,
    name VARCHAR(255)
);

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
    image VARCHAR(255)
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
    (7, 'Sports'),
    (8,'Multidisciplinary');



INSERT INTO Attributes (attribute_id, name)
VALUES
    (1, 'Singing Voice'),
    (2, 'Creativity'),
    (3, 'Painting'),
    (4, 'Abstract Intelligence'),
    (5, 'Political Influence'),
    (6, 'Determination'),
    (7, 'Rebellious'),
    (8, 'Activism'),
    (9, 'Empowerment'),
    (10, 'Social Influence'),
    (11, 'Science'),
    (12, 'Research'),
    (13, 'Innovation'),
    (14, 'Acting'),
    (15, 'Charisma'),
    (16, 'Athleticism'),
    (17, 'Writing');

INSERT INTO Cards (card_id, name, category_id,image)
VALUES
	(1, 'Beyonce', 1, 'beyonce.png'),
    (2, 'Sinead O''Connor', 1, 'sinead.jpg'),
    (3, 'Virginia Wolf ', 1, 'virginia.jpg'),
    (4, 'Taylor Swift', 1, 'taylor.jpg'),
	(5, 'Penelope Cruz', 2, 'penelopecruz.jpg'),
    (6, 'Susan Sarandon', 2, 'sarandon.jpg'),
    (7, 'Whoopi Goldberg', 2, 'whoopi.jpg'),
    (8, 'Meryl Streep', 2, 'streep.jpg'),
    (9, 'Ruth Bader Ginsburg', 3, 'ruth.jpg'),
    (10, 'Florence Nightingale', 8, 'florence.jpg'),
    (11, 'Rosa Parks', 3, 'rosa.jpg'),
    (12, 'Hedy Lamarr', 8, 'hedy.jpg'),
    (13, 'Emmeline Pankhurst', 4, 'pankhurst.jpg'),
    (14, 'Malala Yousafzai', 4, 'malala.jpg'),
    (15, 'Ada Lovelace', 5, 'ada.jpg'),
    (16, 'Marie Curie', 5, 'mariecurie.jpg'),
    (17, 'Harriet Tubman', 4, 'tubman.jpg'),
    (18, 'Maria Telkes', 5, 'mariatelkes.jpg'),
    (19, 'Beatrice Shilling', 5, 'beatrice.jpg'),
	(20, 'Michelle Obama', 6, 'michelle.jpg'),
	(21, 'Serena Williams', 7, 'serenawilliams.jpeg'),
    (22, 'Fu Yuanhui', 7, 'fuyuanhui.jpg'),
    (23,'Beatrix Potter',8,'potter.jpg'),
    (24, 'Frida Kahlo', 8, 'frida.png');

INSERT INTO Card_Attribute_Score (card_id, attribute_id, score)
VALUES
    (1, 1, 9),
    (1, 2, 8),
    (1, 15, 7),
    (1, 8, 6),
	(2, 1, 8),
    (2, 2, 8),
    (2, 10, 6),
    (2, 7, 9),
    (3, 2, 9),
    (3, 10, 6),
    (3, 7, 7),
    (3, 17, 10),
    (4, 1, 9),
    (4, 2, 9),
    (4, 6, 8),
    (4, 9, 7),
    (5, 14, 8),
    (5, 15, 7),
    (5, 6, 7),
    (5, 9, 6),
    (6, 14, 9),
    (6, 15, 7),
    (6, 6, 8),
    (6, 2, 7),
    (7, 14, 7),
    (7, 15, 10),
    (7, 2, 8),
    (7, 10, 7),
    (8, 14, 10),
    (8, 15, 8),
    (8, 2, 7),
    (8, 9, 6),
    (9, 4, 8),
    (9, 5, 10),
    (9, 6, 7),
    (9, 7, 7),
    (10, 17, 8),
    (10, 5, 10),
    (10, 13, 8),
    (10, 11, 9),
    (11, 5, 9),
    (11, 7, 8),
    (11, 10, 9),
    (11, 6, 10),
    (12, 11, 7),
    (12, 14, 9),
    (12, 13, 8),
    (12, 12, 8),
    (13, 5, 9),
    (13, 8, 10),
    (13, 10, 8),
    (13, 7, 9),
    (14, 8, 10),
    (14, 9, 8),
    (14, 10, 9),
    (14, 15, 7),
    (15, 11, 10),
    (15, 12, 8),
    (15, 13, 8),
    (15, 4, 7),
    (16, 11, 10),
    (16, 12, 8),
    (16, 13, 7),
    (16, 4, 9),
    (17, 7, 7),
    (17, 9, 9),
    (17, 10, 8),
    (17, 8, 10),
    (18, 4, 9),
    (18, 11, 10),
    (18, 13, 8),
    (18, 12, 8),
	(19, 4, 8),
    (19, 11, 9),
    (19, 13, 10),
    (19, 12, 7),
    (20, 5, 10),
    (20, 8, 8),
    (20, 15, 7),
    (20, 4, 9),
    (21, 6, 9),
    (21, 8, 7),
    (21, 16, 10),
    (21, 9, 8),
    (22, 16, 9),
    (22, 9, 8),
    (22, 7, 9),
    (22, 6, 7),
    (23, 11, 9),
    (23, 2, 8),
    (23, 17, 10),
    (23, 5, 8),
    (24, 2, 9),
    (24, 3, 10),
    (24, 5, 7),
    (24, 8, 8);
