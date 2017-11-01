#!/usr/bin/env python

##flask app for pourbaix diagrams generation##
import StringIO

import numpy as np
import matplotlib.pyplot as plt
from pourbaix_plot import solvated, Pourbaix
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from flask import Flask, jsonify, make_response #render_template
app = Flask(__name__)

@app.route("/")
def index():
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
    pb.diagram(U, pH, plot=True)
    
    fig1 = plt.gcf()
#     canvas = FigureCanvas(fig1)
#     output = StringIO.StringIO()
#     canvas.print_png(output)
#     response = make_response(output.getvalue())
#     response.mimetype = 'image/png'
#     return response
    import mpld3
    fig1_json = mpld3.save_json(fig1,"fig1_json")
   
    return jsonify(fig1_json)
#     return render_template('template.html')


if __name__== "__main__":
    app.run()
