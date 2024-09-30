class AbstractRunnerModel():
    def __init__(self, runner):
        self.speed = runner.speed
        self.direction = runner.direction
        self.isMoving = runner.isMoving
        self.model = runner.model
        self.name = runner.name

    def run(self, runner):
        pass

    def stop(self, runner):
        pass
