import re
from os.path import exists



class DataValidatorFactory(object):
    def factory(type):
        if type == "value-in-range": return ValueInRange()
        if type == "file-exists": return FileExists()
        if type == "correct-url": return CorrectURL()
        assert 0, "Error: Bad validator type: " + type

    factory = staticmethod(factory)


class DataValidator(object):
    def validate(self):
        # returns TRUE / FALSE
        pass
    def error_msg(self):
        return "Invalid input data"


class ValueInRange(DataValidator):
    def validate(self, data, rangeFrom, rangeTo):
        return data >= rangeFrom and data <= rangeTo


class FileExists(DataValidator):
    def validate(self, filepath):
        return exists(filepath)


class CorrectURL(DataValidator):
    def validate(self, url):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) != None


#added 1st line
#added 2nd line

#added 3rd line

#new entry from my_branch
