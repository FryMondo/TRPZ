from InstallGenerator.Interpreter.Context import Context
from InstallGenerator.Interpreter.TerminalExpression import TerminalExpression
from InstallGenerator.Methods.LanguageSelect import get_language

class CheckLicense:
    def __init__(self, repository):
        self.context = Context(repository)

    def checkLicense(self):
        terminal_expression = TerminalExpression(self.context.licence_key_repository.get())
        while True:
            self.context.user_input_key = input(get_language().get_message("enter_license_key"))
            if terminal_expression.interpret(self.context):
                print(get_language().get_message("license_key_valid"))
                break
            else:
                print(get_language().get_message("license_key_invalid"))