CREATE TABLE Users (
    UserID INT NOT NULL AUTO_INCREMENT,
    FirstName VARCHAR(15) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Email VARCHAR(250) NOT NULL UNIQUE,
    Password VARCHAR(64) NOT NULL,
    SessionToken VARCHAR(255) UNIQUE,
    PRIMARY KEY(UserID)
);

CREATE TABLE LinkFolders (
    FolderID INT NOT NULL AUTO_INCREMENT,
    FolderName VARCHAR(30) NOT NULL,
    UserID INT NOT NULL,
    PRIMARY KEY(FolderID),
    FOREIGN KEY(UserID) REFERENCES Users(UserID)
);

CREATE TABLE Links (
    LinkCode VARCHAR(255) NOT NULL UNIQUE,
    LinkName VARCHAR(50) NOT NULL,
    RedirectsTo TEXT NOT NULL,
    NumberOfVisits INT NOT NULL DEFAULT 0,
    IsEnabled INT NOT NULL DEFAULT 1,
    IsExpired INT NOT NULL DEFAULT 0,
    StartDate DATETIME,
    ExpiryDate DATETIME,
    DateCreated DATETIME NOT NULL,
    FolderID INT NOT NULL,
    PRIMARY KEY(LinkCode),
    FOREIGN KEY(FolderID) REFERENCES LinkFolders(FolderID)
);

CREATE TABLE QRCodes (
    QRCodeID INT NOT NULL AUTO_INCREMENT,
    LinkCode VARCHAR(255) NOT NULL,
    PRIMARY KEY(QRCodeID),
    FOREIGN KEY(LinkCode) REFERENCES Links(LinkCode)
);

-- Adds data into the Users table
INSERT INTO Users (FirstName, LastName, Email, Password, SessionToken) VALUES ("Daniel", "McPherson", "daniel.mcpherson@live.co.uk", "e8183822781ee45b69e3a5a1cc536b88fcf1396d4ca7fd77b91aa0b48b97d601", "aae9fca333958734ea00b53d07c56d32");
INSERT INTO Users (FirstName, LastName, Email, Password, SessionToken) VALUES ("Elliot", "Alderson", "elliot_alderson@proton.me", "f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2", "abc76ae5ac6a7f8e998f0eacfd7a23s4");
INSERT INTO Users (FirstName, LastName, Email, Password, SessionToken) VALUES ("Mr", "robot", "mr_robot@proton.me", "63c45d0e6b14344bda429b5caecb6994905fd19d8fbadc7539e4ef0e3c3a4342", "7826d6fb8csa09s5a67d8f7a54s6s8c9");

-- Adds data into the LinkFolders table
INSERT INTO LinkFolders (FolderName, UserID) VALUES ("Programming Events", 1);
INSERT INTO LinkFolders (FolderName, UserID) VALUES ("Blog Posts", 1);

INSERT INTO LinkFolders (FolderName, UserID) VALUES ("Winter Sale 2023", 2);

INSERT INTO LinkFolders (FolderName, UserID) VALUES ("Referral Programs", 3);
INSERT INTO LinkFolders (FolderName, UserID) VALUES ("Twitter Ads", 3);

-- Inserts data into the Links table
INSERT INTO Links (LinkCode, LinkName, RedirectsTo, NumberOfVisits, IsEnabled, IsExpired, StartDate, ExpiryDate, DateCreated, FolderID)
VALUES ('abc123', 'Python Workshop', 'https://example.com/python-workshop', 120, 1, 0, '2023-03-15', '2023-03-17', '2023-01-15 00:00:00', 1), ('def456', 'Introduction to Machine Learning', 'https://example.com/ml-intro', 80, 1, 0, '2023-04-01', '2023-04-05', '2023-02-10 00:00:00', 1), ('ghi789', 'Writing Clean Code', 'https://example.com/clean-code', 200, 1, 0, '2023-03-20', NULL, '2023-01-20 00:00:00', 2), ('jkl012', 'Data Privacy Best Practices', 'https://example.com/data-privacy', 150, 1, 0, '2023-02-28', NULL, '2023-01-28 00:00:00', 2), ('mno345', 'Winter Sale Homepage', 'https://example.com/winter-sale', 300, 1, 0, '2023-11-25', '2023-12-02', '2023-10-15 00:00:00', 3), ('pqr678', 'Winter Sale Product A', 'https://example.com/product-a', 50, 1, 0, '2023-11-25', '2023-12-02', '2023-11-01 00:00:00', 3), ('stu901', 'Web Development Tips', 'https://example.com/web-dev-tips', 180, 1, 0, '2023-03-10', NULL, '2023-01-10 00:00:00', 2), ('vwx234', 'Effective Database Design', 'https://example.com/db-design', 120, 1, 0, '2023-02-15', NULL, '2023-01-15 00:00:00', 2), ('yza567', 'Java Conference', 'https://example.com/java-conference', 250, 1, 0, '2023-04-20', '2023-04-22', '2023-02-20 00:00:00', 1), ('bcd890', 'Cybersecurity Blog', 'https://example.com/cybersecurity-blog', 120, 1, 0, '2023-03-05', NULL, '2023-01-05 00:00:00', 2);
