##flask app for pourbaix diagrams generation##

##first to do a very basic tutorial##
import numpy as np
from pourbaix_plot import solvated,Pourbaix

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Pourbaix diagrams view app"

@app.route("/apps/pourbaix")
def pourbaix_generation():
    
    refs = solvated('Zn')   
    refs1 = solvated('Cu')
    refs += [('Zn', 0.0), ('ZnO', -3.323), ('ZnO2(aq)', -2.921), ('Cu',0.0)] 
    refs += refs1 

    pb = Pourbaix(refs, Zn=1, Cu = 1, O =1) 
    U = np.linspace(-2, 2, 200)
    pH = np.linspace(-2, 16, 300)
#   d, names, text = 
    d, names, text= pb.diagram(U, pH, plot=True)
    
#     import matplotlib.pyplot as plt
#     fig_1 = plt.gcf()
# #     import mpld3
# #     mpld3.save_json(fig_1,"/Users/mengzhao/Desktop/fig1_json")
   
    return d, names, text

if __name__== "__main__":
    app.run()
   
    
      
