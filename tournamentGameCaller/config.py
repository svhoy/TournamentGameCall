# Standard Library
from configparser import SafeConfigParser
import logging


class Configuration:
    """Manage and get Configurations from config/config.cfg for the Package"""

    config = SafeConfigParser()
    config.read("urkunden/config.cfg")

    def get_database_config(self) -> dict:
        """Get Database Configurations

        Returns:
            dict: Database Configurations Driver, Path and Password
        """
        database_config = {}
        database_config["Driver"] = self.config["DATABASE"]["Driver"]
        database_config["Path"] = self.config["DATABASE"]["Path"]
        database_config["Password"] = self.config["DATABASE"]["Password"]
        return database_config

    def get_discipline_name(self, discipline_shortcut: str) -> str:
        """Get the full discipline name by shortcut

        Args:
            discipline_shortcut (str): Input the shortcut for a discipline

        Returns:
            str: full discipline name
        """
        return self.config["DISCIPLINES"][discipline_shortcut]
