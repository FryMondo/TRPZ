from InstallGenerator.Interpreter.Context import Context

class AbstractExpression:
    def interpret(self, context: Context):
        raise NotImplementedError("Subclasses must implement 'interpret' method")