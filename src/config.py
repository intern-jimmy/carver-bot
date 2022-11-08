import configparser


class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        self.config = config

    def get(self, section, option):
        return self.config[section][option]

    def set(self, section, option, value):
        self.config.set(section, option, value)

    def addSection(self, section):
        if (not self.config.has_section(section)):
            self.config.add_section(section)

    def getSections(self):
        return self.config.sections()

    def getOptions(self, section):
        return self.config.options(section)

    def removeSection(self, section):
        self.config.remove_section(section)

    def removeOption(self, section, option):
        self.config.remove_option(section, option)

    def display(self):
        value = {section: dict(self.config[section]) for section in self.config.sections()}
        return value