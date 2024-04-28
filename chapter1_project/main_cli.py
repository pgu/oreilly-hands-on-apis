"""Command line executable - Chapter 1"""
import models
from database import SessionLocal, engine

def main():
    with SessionLocal() as session:
        players = session.query(models.Player).all()
        for player in players:
            print(f'Player ID: {player.player_id}')
            print(f'Player ID: {player.first_name}')
            print(f'Player ID: {player.last_name}')
            for performance in player.performances:
                print(f'Performance ID: {performance.performance_id}')
                print(f'Week Number: {performance.week_number}')
                print(f'Fantasy Points: {performance.fantasy_points}')

# If running from the command line, main() is called
if __name__ == "__main__":
    main()