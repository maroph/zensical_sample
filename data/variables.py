# https://zensical.org/docs/setup/extensions/macros/
def define_env(env):
    # Variables are accessible as {{ variable }} in templates
    env.variables["author"] = "Manfred Rosenboom"
    env.variables["version"] = "1.0"

    # # Macros are called as {{ greet("World") }}
    # @env.macro
    # def greet(name):
    #     return f"Hello, {name}!"

    # # Filters are applied as {{ "hello" | shout }}
    # @env.filter
    # def shout(text):
    #     return text.upper()

