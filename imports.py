import sys, json, requests, calendar, time
import random, string
import pandas as pd
import finplot.pdplot

import finplot as fplt
from pyqtgraph.dockarea import DockArea, Dock
from datetime import datetime
from web3 import Web3

from PyQt5 import *
#from PyQt5 import QtChart, QtCore
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from ui.Styles import *
from src.config_handler import *
from src.web3_functions import *
from src.math_functions import *
from src.Ui_functions import *
from src.limit_orders_algo import *

from ui.gui import Ui_Dialog
from ui.Styles import Ui_Fonts, Ui_Styles