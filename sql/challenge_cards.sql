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
    image VARCHAR(225)
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

INSERT INTO Cards (card_id, name, image)
VALUES
    (1, 'Melodies in paint', 'artist.jpg'),
    (2, 'Take centre stage', 'actors.jpg'),
    (3, 'Pioneers of knowledge', 'academics.jpg'),
    (4, 'Change minds, change lives', 'activist.jpg'),
    (5, 'Science enthusiast', 'scientist.jpg'),
    (6, 'Quest for justice', 'politician.jpg'),
    (7, 'Pursuit of athletic excellence', 'sports.jpg');

INSERT INTO Card_Attribute_Score (card_id, attribute_id, score)
VALUES
    (1, 1, 8),
    (1, 2, 9),
    (1, 3, 10),
    (1, 4, 6),
    (2, 26, 7),
    (2, 28, 8),
    (2, 29, 9),
    (3, 5, 9),
    (3, 21, 10),
    (3, 22, 8),
    (4, 6, 8),
    (4, 12, 10),
    (4, 14, 9),
    (5, 18, 10),
    (5, 19, 8),
    (5, 20, 9),
    (6, 6, 9),
    (6, 13, 9),
    (6, 15, 10),
    (7, 7, 10),
    (7, 10, 9),
    (7, 14, 8);