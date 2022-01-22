import os

from TournamentGameCaller.db_connector import DB_Connector

dir_path = os.path.dirname(os.path.realpath(__file__))

DB_Connector(dir_path)
