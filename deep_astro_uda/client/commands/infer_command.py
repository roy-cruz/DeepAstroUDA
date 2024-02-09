from cleo.commands.command import Command

class InferCommand(Command):
    name = "infer"
    
    def handle(self):
        self.line('Running the client')
        self.call('client:infer')
