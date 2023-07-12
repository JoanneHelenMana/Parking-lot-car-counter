class Configuration:
    """
    Contains a static method that will allow a configuration file to be read, and it will return
    a dictionary containing the configuration items (key=value).
    """
    @staticmethod
    def from_file(file_name='Configuration/configuration.txt'):
        """Reads the configuration file using the {file_name} and stores the key=value pairs
        in a dictionary that is then returned.
        :param file_name: file containing the configuration
        :return: a dictionary
        """
        configuration = {}
        with open(file_name, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    # end of file
                    break

                line = line.strip()
                if line == '':
                    # skip empty lines
                    continue

                key, value = line.split('=', maxsplit=1)
                configuration[str(key.strip())] = str(value.strip())

        return configuration
