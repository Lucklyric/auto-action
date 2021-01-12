from .action_resolver import common_resolver


class ActionManager(object):
    all_resolvers = [
        common_resolver.SimpleShellResolver(),
        common_resolver.PythonResolver(),
        common_resolver.PythonModuleResolver(),
    ]

    @staticmethod
    def getResolver(action_type):
        for resolver in ActionManager.all_resolvers:
            if (resolver.fit(action_type)):
                return resolver
        raise Exception("action type |{}| not supported".format(action_type))

    @staticmethod
    def run(actions_configs):
        for action_config in actions_configs:
            ActionManager.getResolver(action_config['type']).execute(action_config)



