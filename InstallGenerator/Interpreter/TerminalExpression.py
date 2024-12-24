from InstallGenerator.Interpreter.AbstractExpression import AbstractExpression
from InstallGenerator.Interpreter.Context import Context

class TerminalExpression(AbstractExpression):
    def __init__(self, valid_key):
        self.valid_key = valid_key

    def interpret(self, context: Context):
        return context.user_input_key == self.valid_key