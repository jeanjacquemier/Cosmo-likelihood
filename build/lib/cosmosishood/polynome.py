import cosmosis


class PolynomeModule(cosmosis.ClassModule):
    # This parent class expects that the __init__ method is overridden,
    # matching the setup function in our first module.  

    def setup(options):
        # The options object is a DataBlock.  We use the special pre-defined section name
        # cosmosis.option_section to indicate that we want the options relevant to this
        # module (discussed below)
        degree = options.get_int(cosmosis.option_section, "degree")
        print(f"We will fit polynomials of degree {degree}")
        # This can return any python object.  In C, C++, or Fortran it would return a pointer.
        return {"degree": degree}
        
    # The execute method is exactly the same as the previous version
    def execute(block, config):
        # "config" is just whatever we passed from setup, returned to us here
        degree = config['degree']

        # Let's imagine our first module is calculating a polynomial
        # function. Then the parameters it needs are the coefficients,
        # which we will name "p_0", "p_1", etc.
        coeffs = []
        for i in range(degree+1):
            coef  = block['coefficients', f'param_{i}']
            coeffs.append(coef)



        # Now we can make the polynomial x and y values,
        x = np.linspace(0, 1, 1000)
        y = np.zeros_like(x)
        for i in range(degree+1):
            y += coeffs[i] * x**i
            
        # and store them in the block for later modules
        # to use
        block['poly', 'x'] = x
        block['poly', 'y'] = y

        # we return 0 to indicate that everything worked.
        return 0


