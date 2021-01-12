from abc import abstractmethod
import subprocess

class BaseResolver(object):
    
    @abstractmethod
    def fit(self, action_type):
        raise NotImplementedError

    @abstractmethod
    def execute(self, action_config):
        raise NotImplementedError

class SimpleShellResolver(BaseResolver):
    resolver_type = 'shell'

    def fit(self, action_type):
        return action_type == SimpleShellResolver.resolver_type

    def parse_action_config(self, action_config):
        shell_cmd_list = []
        shell_cmd_list.extend(self.parse_target(action_config['target']))
        if ('positional_arguments' in action_config):
            shell_cmd_list.extend(self.parse_positional_args(action_config['positional_arguments']))
        if ('optional_arguments' in action_config):
            shell_cmd_list.extend(self.parse_optional_args(action_config['optional_arguments']))
        return shell_cmd_list

    def parse_positional_args(self, positional_args):
        return ["{}".format(arg) for arg in positional_args]

    def parse_optional_args(self, optional_args):
        arg_list = []
        for (optional_args_key) in optional_args:
            arg_list.append("--{}".format(optional_args_key))
            arg_list.append("{}".format(optional_args[optional_args_key]))
        return arg_list

    def parse_target(self, target):
        return [target]

    def execute(self, action_config):
        shell_cmd_list = self.parse_action_config(action_config)
        subprocess.run(shell_cmd_list)


class PythonResolver(SimpleShellResolver):
    resolver_type = 'python'

    def fit(self, action_type):
        return action_type == PythonResolver.resolver_type

    def parse_target(self, target):
        return ['python', target]

class PythonModuleResolver(SimpleShellResolver):
    resolver_type = 'python_module'

    def fit(self, action_type):
        return action_type == PythonModuleResolver.resolver_type

    def parse_target(self, target):
        return ['python', '-m', target]
