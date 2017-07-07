class ParamScanner:
    def get_groups(self, command_line_arguments):
        pass


class ArgParser:
    def __init__(self, schema):
        self.parameters = {}
        for parameter in schema:
            if type(parameter) is tuple:
                k, v = parameter
                self.parameters[k] = v
            else:
                self.parameters[parameter] = False

    def parse(self, command_line_arguments):
        for key, value in ParamScanner().get_groups(command_line_arguments):
            self.parameters[key] = value

    def get(self, key):
        return self.parameters[key]
