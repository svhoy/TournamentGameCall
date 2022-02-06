from configparser import SafeConfigParser


class Configuration:
    config = SafeConfigParser()
    config.read("config/config.cfg")

    def getDatabaseConfig(self) -> dict:
        database_config = {}
        database_config["Driver"] = self.config["DATABASE"]["Driver"]
        database_config["Path"] = self.config["DATABASE"]["Path"]
        database_config["Password"] = self.config["DATABASE"]["Password"]
        return database_config

    def get_discipline_name(self, discipline_shortcut: str) -> str:
        return self.config["DISCIPLINES"][discipline_shortcut]
