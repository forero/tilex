import os, sys

import numpy as np
from astropy.table import Table

import bokeh.plotting as bk
from bokeh.models import ColumnDataSource, CDSView, IndexFilter
from bokeh.models import CustomJS, LabelSet, Label, Span, Legend
from bokeh.models.widgets import (
    Slider, Button, Div, CheckboxButtonGroup, RadioButtonGroup)
from bokeh.layouts import widgetbox
import bokeh.events


