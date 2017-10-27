##flask app for pourbaix diagrams generation##

##first to do a very basic tutorial##
import numpy as np
from pourbaix_plot import solvated,Pourbaix

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"
def pourbaix_generation():
    
    refs = solvated('Zn')   
    refs1 = solvated('Cu')
    # print(refs)
    # print(refs1)
    # create a list contains all alloys or solids
    refs += [('Zn', 0.0), ('ZnO', -3.323), ('ZnO2(aq)', -2.921), ('Cu',0.0)] 
    #add solid and aqueous neutral species
    refs += refs1 ##can we get reference energies from somewhere else?
    #print(refs)
    pb = Pourbaix(refs, Zn=1, Cu = 1, O =1) ##if it can be adjusted as elem0= 1, elem1 = 1, O = 1??
    U = np.linspace(-2, 2, 200)
    pH = np.linspace(-2, 16, 300)
    d, names, text = pb.diagram(U, pH, plot=True)
    #print(names)                                    ##ASE considers single metal system which 
                                                    #may be oversimplified in binary systems
    #print(type(pb.diagram(U, pH, plot=True)))
    return d, name, text;

if __name__== "__pourbaix_generation__":
    app.run()
    
    
