import cosmosis


class PowerModule(cosmosis.ClassModule):
    # This parent class expects that the __init__ method is overridden,
    # matching the setup function in our first module.  
    def __init__(self, options):
        # In this class the options parameter has been trimmed to just be the options
        # specific to this module, so no funny 'cosmosis.options_section' is needed
        # when getting parameters
        self.exponent = options.get_double("exponent")
    
    # The execute method is exactly the same as the previous version
    def execute(self, block):
        coef  = block['power_module_coef', 'power_module_param']
        block['poly', 'y'] = (block['poly', 'y']*coef) ** self.exponent

# The parent class has a method called as_module which converts this to a module
