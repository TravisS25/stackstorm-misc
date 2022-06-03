from st2common.runners.base_action import Action

class LogAction(Action):
    def __init__(self, config):
        """Creates a new BaseAction given a StackStorm config object (kwargs works too)
        :param config: StackStorm configuration object for the pack
        :returns: a new BaseAction
        """
        super(LogAction, self).__init__(config)

    def run(self, **kwargs):
        with open(kwargs['file_path'], "w") as fp:
            fp.write(kwargs['log'])
