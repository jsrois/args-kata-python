import re


class ParamScanner:
    def get_groups(self, command_line_arguments):
        pattern = re.compile(r"(?:(?P<key>-[a-zA-Z])\s+(?P<value>[^\s\-]+)*)")
        groups = [(key, value or True) for key, value in pattern.findall(command_line_arguments)]
        return groups


class ArgParser:
    def __init__(self, schema):
        self.parameters = {}
        for parameter in schema:
            self.add_parameter_to_schema(parameter)

    def add_parameter_to_schema(self, parameter):
        if type(parameter) is tuple:
            k, v = parameter
            self.parameters[k] = v
        else:
            self.parameters[parameter] = False

    def parse(self, command_line_arguments):
        for key, value in ParamScanner().get_groups(command_line_arguments):
            self.parameters[key] = type(self.parameters[key])(value)

    def get(self, key):
        return self.parameters[key]
