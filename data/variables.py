# https://zensical.org/docs/setup/extensions/macros/
def define_env(env):
    # Variables are accessible as {{ variable }} in templates
    env.variables["author"] = "Manfred Rosenboom"
    env.variables["version"] = "1.0"

