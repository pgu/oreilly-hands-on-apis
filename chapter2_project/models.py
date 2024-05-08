"""SQLAlchemy models - Chapter 2"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Player(Base):
    __tablename__ = "player"

    player_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    performances = relationship("Performance", back_populates="player")


class Performance(Base):
    __tablename__ = "performance"

    performance_id = Column(Integer, primary_key=True, index=True)
    week_number = Column(String, nullable=False)
    fantasy_points = Column(Float, nullable=False)

    player_id = Column(Integer, ForeignKey("player.player_id"))

    player = relationship("Player", back_populates="performances")


class League(Base):
    __tablename__ = "league"

    league_id = Column(Integer, primary_key=True, index=True)
    league_name = Column(String, nullable=False)
    scoring_type = Column(String, nullable=False)

    teams = relationship("Team", back_populates="league")


class Team(Base):
    __tablename__ = "team"

    team_id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, nullable=False)

    league_id = Column(Integer, ForeignKey("league.league_id"))

    league = relationship("League", back_populates="teams")

    players = relationship("Player", secondary="team_player", back_populates="teams")

class TeamPlayer(Base):
    __tablename__ = "team_player"

    team_id = Column(Integer, ForeignKey("team.team_id"), primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("player.player_id"), primary_key=True, index=True)

# Many-to-many relationship between Player and Team tables
Player.teams = relationship("Team", secondary="team_player", back_populates="players")

