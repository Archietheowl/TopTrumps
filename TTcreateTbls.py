from sqliteConnect import *

cursor.execute(
	""" 
CREATE TABLE "gobletoffire" (
	"CardID"	INTEGER NOT NULL UNIQUE,
	"CardName"	TEXT,
	"Info"		TEXT,
	"Courage"	INT,
	"Cunning"	INT,
	"Magic"		INT,
	"Temper"	INT,
	"Wisdom"	INT,
	PRIMARY KEY("CardID" AUTOINCREMENT)
)"""
)

# ...............................
cursor.execute("""
CREATE TABLE "roalddahl1" (
	"CardID"	INTEGER NOT NULL UNIQUE,
	"CardName"	TEXT,
	"Info"		TEXT,
	"Brains"	INT,
	"Cunning"	INT,
	"Greed"		INT,
	"Kindness"	INT,
	"Mischief"	INT,
	PRIMARY KEY("CardID" AUTOINCREMENT)
)"""
)
# ...........................
cursor.execute("""
CREATE TABLE "sportscars" (
	"CardID"	INTEGER NOT NULL UNIQUE,
	"CardName"				TEXT,
	"Info"					TEXT,
	"Cool Factor"			INT,
	"Engine Size"			DEC,
	"Innovation"			INT,
	"Top Speed(mph)"		INT,
	"Year Launched"			INT,
	"Years In Production"	INT,
	PRIMARY KEY("CardID" AUTOINCREMENT)
)"""
)