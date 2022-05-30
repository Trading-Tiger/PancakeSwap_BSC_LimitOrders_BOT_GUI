from imports import *

class Ui_Styles():
	BUY_label = u"""color:green;
font-weight: bold;
background:transparent;
font-size: 12pt;"""

	SELL_label = u"""color:rgb(196, 49, 69);
font-weight: bold;
background:transparent;
font-size: 12pt;"""

	ChartStyle = u"""
    background-color:black;
    """

	btn_CandelTime = u"""
QPushButton {
	font: bold;
	font-size: 11px;
	color: rgb(220, 161, 1);
	border-radius: 0%;

	background-color: rgb(33, 37, 43);
	border: 3px solid rgb(33, 37, 43);

	background-position: center;
	background-repeat: no-reperat;
}
QPushButton:hover {
	background-color: rgb(39, 44, 54);
}
QPushButton:pressed {	
	background-color: rgb(85, 170, 255);
}
    """

	btn_CandelTime_Select = u"""
QPushButton {
	font: bold;
	font-size: 11px;
	color: rgb(220, 161, 1);
	border-radius: 0%;

	background-color: rgb(39, 44, 54);
	border: 2px solid #dca101;

	background-position: center;
	background-repeat: no-reperat;
}
QPushButton:hover {
	background-color: rgb(39, 44, 54);
}
QPushButton:pressed {	
	background-color: rgb(85, 170, 255);
}
    """
    	

class Ui_Colors():
    BLACK = QColor("black")
    TIGS_ORANGE = QColor("#DCA101")

class Ui_Fonts():
    serifFont = QFont("Times", 10, QFont.Bold)
    sansFont = QFont("Helvetica [Cronyx]", 12)