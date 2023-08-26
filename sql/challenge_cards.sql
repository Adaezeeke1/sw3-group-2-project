DROP DATABASE IF EXISTS challenge_cards;
CREATE DATABASE challenge_cards;
USE challenge_cards;

CREATE TABLE Attributes (
    attribute_id INT PRIMARY KEY,
    name VARCHAR(255)
);


CREATE TABLE Cards (
    card_id INT PRIMARY KEY,
    name VARCHAR(255),
    image VARCHAR(255)
);


CREATE TABLE Card_Attribute_Score (
    card_id INT,
    attribute_id INT,
    score INT,
    FOREIGN KEY (card_id) REFERENCES Cards(card_id),
    FOREIGN KEY (attribute_id) REFERENCES Attributes(attribute_id)
);

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

INSERT INTO Cards (card_id, name, image)
VALUES
    (1, 'Melodies in paint', 'creativity.png'),
    (2, 'Take centre stage', 'stage.jpg'),
    (3, 'Pioneers of knowledge', 'innovation.png'),
    (4, 'Change minds, change lives', 'influence.jpg'),
    (5, 'Quest for justice', 'leadership.png'),
    (6, 'Pursuit of athletic excellence', 'sport.jpeg'),
    (7, 'Multitalented mind','multitalented.jpg');

INSERT INTO Card_Attribute_Score (card_id, attribute_id, score)
VALUES
    (1, 1, 8),
    (1, 2, 7),
    (1, 3, 9),
    (1, 4, 6),
    (2, 1, 7),
    (2, 2, 8),
    (2, 14, 7),
	(2, 15, 8),
    (3, 4, 6),
    (3, 12, 8),
    (3, 13, 7),
	(3, 11, 6),
    (4, 5, 8),
    (4, 10, 8),
    (4, 8, 6),
	(4, 9, 7),
    (5, 5, 9),
    (5, 7, 6),
    (5, 6, 8),
    (5, 9, 6),
    (6, 16, 9),
    (6, 6, 8),
    (6, 8, 5),
	(6, 10, 6),
    (7, 17, 5),
    (7, 7, 5),
    (7, 11, 5),
    (7, 13, 5);