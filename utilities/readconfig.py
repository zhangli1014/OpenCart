import configparser

config = configparser.RawConfigParser()
config.read('./Configrations/config.ini')

class readConfig:
    @staticmethod
    def getconfig(section,key):
        url = config.get(section,key)
        return url

if __name__=='__main__':
    print(readConfig().getconfig('opencart info','baseURL'))