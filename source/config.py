from configparser import ConfigParser


<<<<<<< HEAD
def config(name='../database.ini', section='postgresql'):
=======
def config(name='database.ini', section='postgresql'):
>>>>>>> fe1792045b2a4db0295b0b1ec417cc3f5ec6555d
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(name)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, name))

    return db
