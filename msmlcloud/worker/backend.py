__author__ = 'weigla'


class CloudApp(App):
    #TODO Overwrite for state information
    @property
    def executor(self):
        return ProgressLinearExecutor


class ProgressLinearExecutor(LinearExecutor):
    #TODO Overwrite for state information
    pass

