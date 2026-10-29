import numpy as np
import cosmosis

class Likelihood(cosmosis.GaussianLikelihood):
    # The likelihood will be saved with this name,
    # here target_like
    like_name = "target"

    # The parent class will look for these x and y values
    # in the block, and interpolate the data x and y values to them.
    # If interpolation is not suitable for your likelihood, you can
    # instead override the extract_theory_points method.
    x_section = "poly"
    x_name = "x"
    y_section = "poly"
    y_name = "y"
    
    def __init__(self, options):
        # The parent initializer calls the methods below
        # after setting self.options to this options object
        super().__init__(options)
        print("Created a new likelihood called", self.like_name)

    # This is called from setup to load or simulate the
    # data for the likelihood
    
    def build_data(self):
        # Let's make up some fake data to fit our model to
        x = np.array([0.2, 0.31, 0.44, 0.77, 0.9])
        y = (1.4 * x**2 - 3.1 * x - 0.8) ** 2
        return x, y
    

    # This is also called at the start to load the covariance
    # matrix.  You could also overrride build_inverse_covariance
    # if you have that already.
    def build_covariance(self):
        # We can read parameters from the config like this:
        noise_level = self.options['noise_level']
        sigma = np.array([0.05, 0.06, 0.04, 0.03, 0.1]) * noise_level
        return np.diag(sigma**2)
