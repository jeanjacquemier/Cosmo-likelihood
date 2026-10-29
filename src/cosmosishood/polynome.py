import cosmosis
import numpy as np



    
def setup(config: cosmosis.datablock):
    # In this class the options parameter has been trimmed to just be the options
    # specific to this module, so no funny 'cosmosis.options_section' is needed
    # when getting parameters
    degree =  config.get_int("degree")
    return {"degree": degree}

    
def execute(sample: cosmosis.datablock, config: cosmosis.datablock):
    # The parameters it needs are the coefficients,
    # which we will name "p_0", "p_1", etc.
    degree = config['degree']

    coeffs = []
    print(f"DEBUG block.sections(): {sample.keys()}")
    for i in range(degree+1):
        coef  = sample['coefficients', f'param_{i}']
        coeffs.append(coef)



    # Now we can make the polynomial x and y values,
    x = np.linspace(0, 1, 1000)
    y = np.zeros_like(x)
    for i in range(degree+1):
        y += coeffs[i] * x**i
        
    # and store them in the block for later modules
    # to use
    sample['poly', 'x'] = x
    sample['poly', 'y'] = y

    # we return 0 to indicate that everything worked.
    return 0


