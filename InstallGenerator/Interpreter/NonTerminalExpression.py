from InstallGenerator.Interpreter.AbstractExpression import AbstractExpression
from InstallGenerator.Interpreter.Context import Context

class NonTerminalExpression(AbstractExpression):
    def __init__(self, expressions):
        self.expressions = expressions

    def interpret(self, context: Context):
        for expression in self.expressions:
            if not expression.interpret(context):
                return False
        return True