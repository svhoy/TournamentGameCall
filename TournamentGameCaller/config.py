from configparser import SafeConfigParser


class Configuration():
    config = SafeConfigParser()
    config.read('config/config.cfg')

    def getDatabaseConfig(self) -> dict:
        print(self.config.sections())
        database_config = {}
        database_config['Driver'] = self.config['DATABASE']['Driver']
        database_config['Path'] = self.config['DATABASE']['Path']
        database_config['Password'] = self.config['DATABASE']['Password']
        return database_config
