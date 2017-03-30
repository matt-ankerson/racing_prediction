
IF OBJECT_ID('dbo.Competitor', 'U') IS NOT NULL
DROP TABLE dbo.Competitor
GO
IF OBJECT_ID('dbo.Bet', 'U') IS NOT NULL
DROP TABLE dbo.Bet
GO
IF OBJECT_ID('dbo.Race', 'U') IS NOT NULL
DROP TABLE dbo.Race
GO
IF OBJECT_ID('dbo.Event', 'U') IS NOT NULL
DROP TABLE dbo.Event
GO

-- =========================================
-- RaceEvent
-- =========================================

CREATE TABLE dbo.Event
(
    ID int NOT NULL, 
    Name varchar(MAX) NULL, 
    EventDate varchar(MAX) NULL, 
    PRIMARY KEY (ID)
)
GO

-- =========================================
-- Race
-- =========================================

CREATE TABLE dbo.Race
(
    ID int NOT NULL, 
    RaceNumber varchar(MAX) NULL, 
    Distance varchar(MAX) NULL, 
    Stake varchar(MAX) NULL, 
    TrackCondition varchar(MAX) NULL, 
    Weather varchar(MAX) NULL, 
    WinningMargins varchar(MAX) NULL, 
    WinnerOwners varchar(MAX) NULL, 
    WinnerTrainer varchar(MAX) NULL, 
    WinnerBreeding varchar(MAX) NULL, 
    Sub varchar(MAX) NULL, 
    WinnerTime varchar(MAX) NULL, 
    -- bets
    -- competitors
    EventID int NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (EventID) REFERENCES dbo.Event(ID)
)
GO

-- =========================================
-- Competitor
-- =========================================

CREATE TABLE dbo.Competitor
(
    ID int NOT NULL, 
    Number varchar(MAX) NULL, 
    Name varchar(MAX) NULL, 
    Jockey varchar(MAX) NULL, 
    Place varchar(MAX) NULL, 
    Win varchar(MAX) NULL, 
    LengthsBehindLeader varchar(MAX) NULL, 
    RaceID int NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (RaceID) REFERENCES Race(ID)
)
GO

-- =========================================
-- Bet 
-- =========================================

CREATE TABLE dbo.Bet
(
    ID int NOT NULL, 
    BetType varchar(MAX) NULL, 
    Runners varchar(MAX) NULL, 
    Dividend varchar(MAX) NULL, 
    RaceID int NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (RaceID) REFERENCES Race(ID)
)
GO
