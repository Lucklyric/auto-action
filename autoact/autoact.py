import argparse
from .utils import load_yaml
from .core import ActionManager

def main():
    parser= argparse.ArgumentParser(description='autoAction(autoact) toolkit')
    subparsers = parser.add_subparsers(help='sub-command help')
    parser_apply = subparsers.add_parser('apply', help='Apply an action flow by applying a configuration in YAML format')
    parser_apply.add_argument('--filename', '-f', help='filepath of the YAML file')
    args = parser.parse_args()

    actions_configs = load_yaml(args.filename)

    actions = actions_configs['actions']
    
    ActionManager.run(actions)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        raise e
