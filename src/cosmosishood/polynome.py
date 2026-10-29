import cosmosis
import numpy as np


class PolyModule(cosmosis.ClassModule):
    # This parent class expects that the __init__ method is overridden,
    # matching the setup function in our first module.  
    
    def __init__(self, options):
        # In this class the options parameter has been trimmed to just be the options
        # specific to this module, so no funny 'cosmosis.options_section' is needed
        # when getting parameters
        self.degree =  options.get_int("degree")

        
    def execute(self, block):
        # The parameters it needs are the coefficients,
        # which we will name "p_0", "p_1", etc.
        coeffs = []
        print(f"DEBUG block.sections(): {block.keys()}")
        for i in range(self.degree+1):
            coef  = block['coefficients', f'param_{i}']
            coeffs.append(coef)
    
    
    
        # Now we can make the polynomial x and y values,
        x = np.linspace(0, 1, 1000)
        y = np.zeros_like(x)
        for i in range(self.degree+1):
            y += coeffs[i] * x**i
            
        # and store them in the block for later modules
        # to use
        block['poly', 'x'] = x
        block['poly', 'y'] = y
    
        # we return 0 to indicate that everything worked.
        return 0


