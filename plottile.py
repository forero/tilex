import os, sys

import numpy as np
from astropy.table import Table
from astropy.io import fits


import bokeh.plotting as bk
from bokeh.models import ColumnDataSource, CDSView, IndexFilter
from bokeh.models import CustomJS, LabelSet, Label, Span, Legend
from bokeh.models.widgets import (
    Slider, Button, Div, CheckboxButtonGroup, RadioButtonGroup)
from bokeh.layouts import widgetbox
import bokeh.events


# Load data
fibassign = fits.getdata("/Users/forero/DESI/svdc2019c/fiberassign/tile-070000.fits", "FIBERASSIGN")


# Prepare data for bokeh
assigned_data = dict(ra=fibassign['TARGET_RA'],
                     dec=fibassign['TARGET_DEC'], 
                     x=fibassign['DESIGN_X'], 
                     y=fibassign['DESIGN_Y'])


#set up plotting canvas
plot_width=500
plot_height=500
title='assigned'
tools = 'pan,box_zoom,wheel_zoom,reset,save'

fig = bk.figure(height=plot_height, width=plot_width, title=title,
        tools=tools, toolbar_location='above', y_range=(-450, 450))

bk.output_file("assigned_tile.html")

#plot the assigned fibers
c = fig.circle('x', 'y', source=assigned_data, size=4, color="navy", alpha=0.5)

bk.show(fig)




