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
    LinkName VARCHAR(25) NOT NULL,
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

INSERT INTO Users (FirstName, LastName, Email, Password, SessionToken) VALUES ("Daniel", "McPherson", "daniel.mcpherson@live.co.uk", "e8183822781ee45b69e3a5a1cc536b88fcf1396d4ca7fd77b91aa0b48b97d601", "aae9fca333958734ea00b53d07c56d32");
INSERT INTO Users (FirstName, LastName, Email, Password, SessionToken) VALUES ("Elliot", "Alderson", "elliot_alderson@proton.me", "f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2", "abc76ae5ac6a7f8e998f0eacfd7a23s4");