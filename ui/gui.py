from imports import *

import ui.icons_rc
import ui.files_rc



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1150, 901)
        Dialog.setMinimumSize(QSize(1150, 900))
        Dialog.setMaximumSize(QSize(1920, 1440))
        Dialog.setStyleSheet(u"background-color:#151719;")
        self.verticalLayout_10 = QVBoxLayout(Dialog)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.main_frame = QFrame(Dialog)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.main_frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_grip = QFrame(self.main_frame)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_14.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_version)


        self.horizontalLayout_13.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_size_grip)


        self.gridLayout_2.addWidget(self.frame_grip, 2, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.verticalLayout_4 = QVBoxLayout(self.stackedWidgetPage1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.stackedWidgetPage1)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_23.setSpacing(2)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_17)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(580, 90))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_9)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgba(27, 29, 35, 200);\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777214, 75))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(350, 70))
        self.frame.setMaximumSize(QSize(16777215, 140))
        self.frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.token_address = QLineEdit(self.frame)
        self.token_address.setObjectName(u"token_address")
        self.token_address.setMinimumSize(QSize(325, 30))
        self.token_address.setMaximumSize(QSize(350, 16777215))
        self.token_address.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#dca101;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.token_address.setMaxLength(43)
        self.token_address.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.token_address, 1, 0, 1, 2)

        self.frame_24 = QFrame(self.frame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_24)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.pushButton_AddtoList = QPushButton(self.frame_24)
        self.pushButton_AddtoList.setObjectName(u"pushButton_AddtoList")
        self.pushButton_AddtoList.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 0%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_11.addWidget(self.pushButton_AddtoList)


        self.gridLayout_3.addWidget(self.frame_24, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 70))
        self.frame_2.setMaximumSize(QSize(16777215, 140))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(5, 0, 5, 0)
        self.Button_Market = QPushButton(self.frame_26)
        self.Button_Market.setObjectName(u"Button_Market")
        self.Button_Market.setMinimumSize(QSize(1, 0))
        self.Button_Market.setLayoutDirection(Qt.LeftToRight)
        self.Button_Market.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 4px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Market.setCheckable(False)

        self.horizontalLayout_20.addWidget(self.Button_Market)

        self.Button_Limit = QPushButton(self.frame_26)
        self.Button_Limit.setObjectName(u"Button_Limit")
        self.Button_Limit.setMinimumSize(QSize(1, 0))
        self.Button_Limit.setLayoutDirection(Qt.LeftToRight)
        self.Button_Limit.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 4px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Limit.setCheckable(False)

        self.horizontalLayout_20.addWidget(self.Button_Limit)


        self.horizontalLayout_21.addWidget(self.frame_26)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_18 = QFrame(self.frame_4)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(500, 45))
        self.frame_18.setMaximumSize(QSize(16777215, 55))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_18)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(0, 0))
        self.frame_37.setMaximumSize(QSize(80, 16777215))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_37)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_69 = QFrame(self.frame_37)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(80, 21))
        self.frame_69.setMaximumSize(QSize(16777215, 21))
        self.frame_69.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_69)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 16))
        self.label_4.setMaximumSize(QSize(16777215, 16))
        self.label_4.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 8pt;")
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_4)


        self.verticalLayout_5.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.frame_37)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(80, 21))
        self.frame_70.setMaximumSize(QSize(16777215, 21))
        self.frame_70.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_70)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 18))
        self.label_11.setMaximumSize(QSize(16777215, 21))
        self.label_11.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 8pt;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.label_11)


        self.verticalLayout_5.addWidget(self.frame_70)


        self.horizontalLayout_9.addWidget(self.frame_37)

        self.frame_71 = QFrame(self.frame_18)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(240, 0))
        self.frame_71.setMaximumSize(QSize(200, 16777215))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_71)
        self.verticalLayout_18.setSpacing(2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_71)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(240, 21))
        self.frame_13.setMaximumSize(QSize(250, 21))
        self.frame_13.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius:0%;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_15.setSpacing(2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Chart_1m = QPushButton(self.frame_13)
        self.pushButton_Chart_1m.setObjectName(u"pushButton_Chart_1m")
        self.pushButton_Chart_1m.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 8%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton_Chart_1m)

        self.pushButton_Chart_5m = QPushButton(self.frame_13)
        self.pushButton_Chart_5m.setObjectName(u"pushButton_Chart_5m")
        self.pushButton_Chart_5m.setMinimumSize(QSize(5, 5))
        self.pushButton_Chart_5m.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 8%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton_Chart_5m)

        self.pushButton_Chart_10m = QPushButton(self.frame_13)
        self.pushButton_Chart_10m.setObjectName(u"pushButton_Chart_10m")
        self.pushButton_Chart_10m.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 8%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton_Chart_10m)

        self.pushButton_Chart_30m = QPushButton(self.frame_13)
        self.pushButton_Chart_30m.setObjectName(u"pushButton_Chart_30m")
        self.pushButton_Chart_30m.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 8%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton_Chart_30m)

        self.pushButton_Chart_1h = QPushButton(self.frame_13)
        self.pushButton_Chart_1h.setObjectName(u"pushButton_Chart_1h")
        self.pushButton_Chart_1h.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 0%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton_Chart_1h)

        self.pushButton_Chart_1d = QPushButton(self.frame_13)
        self.pushButton_Chart_1d.setObjectName(u"pushButton_Chart_1d")
        self.pushButton_Chart_1d.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 0%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton_Chart_1d)


        self.verticalLayout_18.addWidget(self.frame_13)

        self.frame_72 = QFrame(self.frame_71)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(240, 21))
        self.frame_72.setMaximumSize(QSize(250, 21))
        self.frame_72.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius:0%;")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ChartTime_1h = QPushButton(self.frame_72)
        self.pushButton_ChartTime_1h.setObjectName(u"pushButton_ChartTime_1h")
        self.pushButton_ChartTime_1h.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 8%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_42.addWidget(self.pushButton_ChartTime_1h)

        self.pushButton_ChartTime_1d = QPushButton(self.frame_72)
        self.pushButton_ChartTime_1d.setObjectName(u"pushButton_ChartTime_1d")
        self.pushButton_ChartTime_1d.setMinimumSize(QSize(5, 5))
        self.pushButton_ChartTime_1d.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 8%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_42.addWidget(self.pushButton_ChartTime_1d)

        self.pushButton_ChartTime_1w = QPushButton(self.frame_72)
        self.pushButton_ChartTime_1w.setObjectName(u"pushButton_ChartTime_1w")
        self.pushButton_ChartTime_1w.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 8%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_42.addWidget(self.pushButton_ChartTime_1w)

        self.pushButton_ChartTime_1m = QPushButton(self.frame_72)
        self.pushButton_ChartTime_1m.setObjectName(u"pushButton_ChartTime_1m")
        self.pushButton_ChartTime_1m.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 8%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_42.addWidget(self.pushButton_ChartTime_1m)

        self.pushButton_ChartTime_1y = QPushButton(self.frame_72)
        self.pushButton_ChartTime_1y.setObjectName(u"pushButton_ChartTime_1y")
        self.pushButton_ChartTime_1y.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 0%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_42.addWidget(self.pushButton_ChartTime_1y)


        self.verticalLayout_18.addWidget(self.frame_72)


        self.horizontalLayout_9.addWidget(self.frame_71)

        self.frame_73 = QFrame(self.frame_18)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(0, 45))
        self.frame_73.setMaximumSize(QSize(16777215, 45))
        self.frame_73.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_73)
        self.verticalLayout_43.setSpacing(2)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_73)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 20))
        self.label_27.setLayoutDirection(Qt.LeftToRight)
        self.label_27.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_27)

        self.frame_74 = QFrame(self.frame_73)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_43.setSpacing(2)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.ButtonChartHelper_Volume = QPushButton(self.frame_74)
        self.ButtonChartHelper_Volume.setObjectName(u"ButtonChartHelper_Volume")
        self.ButtonChartHelper_Volume.setMinimumSize(QSize(1, 0))
        self.ButtonChartHelper_Volume.setLayoutDirection(Qt.LeftToRight)
        self.ButtonChartHelper_Volume.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 5%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.ButtonChartHelper_Volume.setCheckable(False)

        self.horizontalLayout_43.addWidget(self.ButtonChartHelper_Volume)

        self.ButtonchartHelper_MA20 = QPushButton(self.frame_74)
        self.ButtonchartHelper_MA20.setObjectName(u"ButtonchartHelper_MA20")
        self.ButtonchartHelper_MA20.setMinimumSize(QSize(1, 0))
        self.ButtonchartHelper_MA20.setLayoutDirection(Qt.LeftToRight)
        self.ButtonchartHelper_MA20.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 5%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.ButtonchartHelper_MA20.setCheckable(False)

        self.horizontalLayout_43.addWidget(self.ButtonchartHelper_MA20)


        self.verticalLayout_43.addWidget(self.frame_74)


        self.horizontalLayout_9.addWidget(self.frame_73)


        self.verticalLayout.addWidget(self.frame_18)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setMaximumSize(QSize(16777215, 21))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_11)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 21))
        self.frame_6.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(41, 19))
        self.label_3.setMaximumSize(QSize(50, 19))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.TokenName = QLabel(self.frame_6)
        self.TokenName.setObjectName(u"TokenName")
        self.TokenName.setMinimumSize(QSize(0, 19))
        self.TokenName.setMaximumSize(QSize(16777215, 19))
        self.TokenName.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")

        self.horizontalLayout_7.addWidget(self.TokenName)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.frame_10 = QFrame(self.frame_11)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(191, 21))
        self.frame_10.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(41, 19))
        self.label_7.setMaximumSize(QSize(50, 16777215))
        self.label_7.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.TokenPrice = QLabel(self.frame_10)
        self.TokenPrice.setObjectName(u"TokenPrice")
        self.TokenPrice.setMinimumSize(QSize(0, 19))
        self.TokenPrice.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")

        self.horizontalLayout_3.addWidget(self.TokenPrice)

        self.TokenPriceChange = QLabel(self.frame_10)
        self.TokenPriceChange.setObjectName(u"TokenPriceChange")
        self.TokenPriceChange.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")

        self.horizontalLayout_3.addWidget(self.TokenPriceChange)


        self.horizontalLayout_8.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame_11)

        self.stackedWidget_16 = QStackedWidget(self.frame_4)
        self.stackedWidget_16.setObjectName(u"stackedWidget_16")
        self.stackedWidget_16.setMinimumSize(QSize(0, 0))
        self.stackedWidget_16.setMaximumSize(QSize(16777215, 450))
        self.stackedWidget_16.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_16.setFrameShadow(QFrame.Raised)
        self.Chart_Loaded = QWidget()
        self.Chart_Loaded.setObjectName(u"Chart_Loaded")
        self.verticalLayout_26 = QVBoxLayout(self.Chart_Loaded)
        self.verticalLayout_26.setSpacing(2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.chart_container = QWidget(self.Chart_Loaded)
        self.chart_container.setObjectName(u"chart_container")
        self.chart_container.setMinimumSize(QSize(200, 300))
        self.chart_container.setMaximumSize(QSize(16777215, 650))

        self.verticalLayout_26.addWidget(self.chart_container)

        self.stackedWidget_16.addWidget(self.Chart_Loaded)
        self.chart_isLoading = QWidget()
        self.chart_isLoading.setObjectName(u"chart_isLoading")
        self.horizontalLayout_12 = QHBoxLayout(self.chart_isLoading)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.chart_loading = QLabel(self.chart_isLoading)
        self.chart_loading.setObjectName(u"chart_loading")
        self.chart_loading.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.chart_loading)

        self.stackedWidget_16.addWidget(self.chart_isLoading)
        self.Error_Page = QWidget()
        self.Error_Page.setObjectName(u"Error_Page")
        self.Error_Page.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout_45 = QVBoxLayout(self.Error_Page)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_94 = QFrame(self.Error_Page)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setStyleSheet(u"background-color:;")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_94)
        self.verticalLayout_28.setSpacing(3)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_96 = QFrame(self.frame_94)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMaximumSize(QSize(16777215, 40))
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_96)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_96)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"font-size: 14px;\n"
"color: rgb(196, 49, 69) ;\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.label_8)


        self.verticalLayout_28.addWidget(self.frame_96)

        self.frame_97 = QFrame(self.frame_94)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_97)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_Settings_error_2 = QFrame(self.frame_97)
        self.frame_Settings_error_2.setObjectName(u"frame_Settings_error_2")
        self.frame_Settings_error_2.setStyleSheet(u"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(196, 49, 69) ;\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;")
        self.frame_Settings_error_2.setFrameShape(QFrame.StyledPanel)
        self.frame_Settings_error_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_Settings_error_2)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_ErrorMessage = QLabel(self.frame_Settings_error_2)
        self.label_ErrorMessage.setObjectName(u"label_ErrorMessage")
        self.label_ErrorMessage.setMaximumSize(QSize(16777215, 16777215))
        self.label_ErrorMessage.setStyleSheet(u"color:#9ca9b3;")
        self.label_ErrorMessage.setTextFormat(Qt.PlainText)
        self.label_ErrorMessage.setAlignment(Qt.AlignCenter)
        self.label_ErrorMessage.setWordWrap(True)
        self.label_ErrorMessage.setIndent(0)

        self.horizontalLayout_58.addWidget(self.label_ErrorMessage)


        self.verticalLayout_44.addWidget(self.frame_Settings_error_2)


        self.verticalLayout_28.addWidget(self.frame_97)

        self.frame_98 = QFrame(self.frame_94)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMaximumSize(QSize(16777215, 40))
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_59.setSpacing(4)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.pushButton_error_OK = QPushButton(self.frame_98)
        self.pushButton_error_OK.setObjectName(u"pushButton_error_OK")
        self.pushButton_error_OK.setMinimumSize(QSize(0, 30))
        self.pushButton_error_OK.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: green;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_59.addWidget(self.pushButton_error_OK)


        self.verticalLayout_28.addWidget(self.frame_98)


        self.verticalLayout_45.addWidget(self.frame_94)

        self.stackedWidget_16.addWidget(self.Error_Page)
        self.Submit_Page = QWidget()
        self.Submit_Page.setObjectName(u"Submit_Page")
        self.verticalLayout_33 = QVBoxLayout(self.Submit_Page)
        self.verticalLayout_33.setSpacing(2)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_86 = QFrame(self.Submit_Page)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_86)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_marketType = QLabel(self.frame_86)
        self.label_marketType.setObjectName(u"label_marketType")
        self.label_marketType.setMaximumSize(QSize(16777215, 30))
        self.label_marketType.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 14pt;")
        self.label_marketType.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_marketType)

        self.frame_87 = QFrame(self.frame_86)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMaximumSize(QSize(16777215, 40))
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_51.setSpacing(6)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.Confirm_OrderType = QLabel(self.frame_87)
        self.Confirm_OrderType.setObjectName(u"Confirm_OrderType")
        self.Confirm_OrderType.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Confirm_OrderType.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.Confirm_OrderType)

        self.Confirm_Amount_In = QLabel(self.frame_87)
        self.Confirm_Amount_In.setObjectName(u"Confirm_Amount_In")
        self.Confirm_Amount_In.setLayoutDirection(Qt.RightToLeft)
        self.Confirm_Amount_In.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Confirm_Amount_In.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_51.addWidget(self.Confirm_Amount_In)

        self.Confirm_Symbol_In = QLabel(self.frame_87)
        self.Confirm_Symbol_In.setObjectName(u"Confirm_Symbol_In")
        self.Confirm_Symbol_In.setMaximumSize(QSize(40, 16777215))
        self.Confirm_Symbol_In.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")

        self.horizontalLayout_51.addWidget(self.Confirm_Symbol_In)

        self.label_5 = QLabel(self.frame_87)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 16777215))
        self.label_5.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")

        self.horizontalLayout_51.addWidget(self.label_5)

        self.Confirm_Amount_Out = QLabel(self.frame_87)
        self.Confirm_Amount_Out.setObjectName(u"Confirm_Amount_Out")
        self.Confirm_Amount_Out.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Confirm_Amount_Out.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_51.addWidget(self.Confirm_Amount_Out)

        self.Confirm_Symbol_Out = QLabel(self.frame_87)
        self.Confirm_Symbol_Out.setObjectName(u"Confirm_Symbol_Out")
        self.Confirm_Symbol_Out.setMaximumSize(QSize(40, 16777215))
        self.Confirm_Symbol_Out.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")

        self.horizontalLayout_51.addWidget(self.Confirm_Symbol_Out)


        self.verticalLayout_16.addWidget(self.frame_87)

        self.frame_88 = QFrame(self.frame_86)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMaximumSize(QSize(16777215, 40))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_52.setSpacing(4)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_88)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.label_6)

        self.Confirm_TX_FEE_ETH = QLabel(self.frame_88)
        self.Confirm_TX_FEE_ETH.setObjectName(u"Confirm_TX_FEE_ETH")
        self.Confirm_TX_FEE_ETH.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")

        self.horizontalLayout_52.addWidget(self.Confirm_TX_FEE_ETH)


        self.verticalLayout_16.addWidget(self.frame_88)

        self.frame_89 = QFrame(self.frame_86)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_89)

        self.frame_90 = QFrame(self.frame_86)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMaximumSize(QSize(16777215, 40))
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_53.setSpacing(4)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Cancel_Confirm = QPushButton(self.frame_90)
        self.pushButton_Cancel_Confirm.setObjectName(u"pushButton_Cancel_Confirm")
        self.pushButton_Cancel_Confirm.setMinimumSize(QSize(0, 30))
        self.pushButton_Cancel_Confirm.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(196, 49, 69) ;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_53.addWidget(self.pushButton_Cancel_Confirm)

        self.pushButton_Submit_Confirm = QPushButton(self.frame_90)
        self.pushButton_Submit_Confirm.setObjectName(u"pushButton_Submit_Confirm")
        self.pushButton_Submit_Confirm.setMinimumSize(QSize(0, 30))
        self.pushButton_Submit_Confirm.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: green;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_53.addWidget(self.pushButton_Submit_Confirm)


        self.verticalLayout_16.addWidget(self.frame_90)


        self.verticalLayout_33.addWidget(self.frame_86)

        self.stackedWidget_16.addWidget(self.Submit_Page)
        self.Approve_Page = QWidget()
        self.Approve_Page.setObjectName(u"Approve_Page")
        self.verticalLayout_47 = QVBoxLayout(self.Approve_Page)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_103 = QFrame(self.Approve_Page)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_103)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_104 = QFrame(self.frame_103)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMaximumSize(QSize(16777215, 40))
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_64.setSpacing(4)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_104)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 14pt;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.label)


        self.verticalLayout_46.addWidget(self.frame_104)

        self.frame_105 = QFrame(self.frame_103)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMaximumSize(QSize(16777215, 40))
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_65.setSpacing(4)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_105)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.label_9)

        self.Approve_Symbol = QLabel(self.frame_105)
        self.Approve_Symbol.setObjectName(u"Approve_Symbol")
        self.Approve_Symbol.setMaximumSize(QSize(80, 16777215))
        self.Approve_Symbol.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")

        self.horizontalLayout_65.addWidget(self.Approve_Symbol)

        self.label_14 = QLabel(self.frame_105)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.label_14)

        self.label_tb_usd_2 = QLabel(self.frame_105)
        self.label_tb_usd_2.setObjectName(u"label_tb_usd_2")
        self.label_tb_usd_2.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"border:None;")
        self.label_tb_usd_2.setFrameShape(QFrame.NoFrame)
        self.label_tb_usd_2.setScaledContents(True)
        self.label_tb_usd_2.setAlignment(Qt.AlignCenter)
        self.label_tb_usd_2.setWordWrap(True)

        self.horizontalLayout_65.addWidget(self.label_tb_usd_2)


        self.verticalLayout_46.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.frame_103)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMaximumSize(QSize(16777215, 40))
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_66.setSpacing(4)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_106)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.label_20)

        self.Approve_TX_FEE_ETH = QLabel(self.frame_106)
        self.Approve_TX_FEE_ETH.setObjectName(u"Approve_TX_FEE_ETH")
        self.Approve_TX_FEE_ETH.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")

        self.horizontalLayout_66.addWidget(self.Approve_TX_FEE_ETH)


        self.verticalLayout_46.addWidget(self.frame_106)

        self.frame_107 = QFrame(self.frame_103)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)

        self.verticalLayout_46.addWidget(self.frame_107)

        self.frame_108 = QFrame(self.frame_103)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMaximumSize(QSize(16777215, 40))
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_67.setSpacing(4)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Reject_Approve = QPushButton(self.frame_108)
        self.pushButton_Reject_Approve.setObjectName(u"pushButton_Reject_Approve")
        self.pushButton_Reject_Approve.setMinimumSize(QSize(0, 30))
        self.pushButton_Reject_Approve.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(196, 49, 69) ;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_67.addWidget(self.pushButton_Reject_Approve)

        self.pushButton_Submit_Approve = QPushButton(self.frame_108)
        self.pushButton_Submit_Approve.setObjectName(u"pushButton_Submit_Approve")
        self.pushButton_Submit_Approve.setMinimumSize(QSize(0, 30))
        self.pushButton_Submit_Approve.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: green;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_67.addWidget(self.pushButton_Submit_Approve)


        self.verticalLayout_46.addWidget(self.frame_108)


        self.verticalLayout_47.addWidget(self.frame_103)

        self.stackedWidget_16.addWidget(self.Approve_Page)
        self.page_TX_Status = QWidget()
        self.page_TX_Status.setObjectName(u"page_TX_Status")
        self.verticalLayout_49 = QVBoxLayout(self.page_TX_Status)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_110 = QFrame(self.page_TX_Status)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_110)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.frame_111 = QFrame(self.frame_110)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMaximumSize(QSize(16777215, 40))
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_69.setSpacing(4)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_111)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 14pt;")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.label_45)


        self.verticalLayout_48.addWidget(self.frame_111)

        self.frame_112 = QFrame(self.frame_110)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMaximumSize(QSize(16777215, 40))
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_70.setSpacing(4)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.Transaction_Succesfully = QLabel(self.frame_112)
        self.Transaction_Succesfully.setObjectName(u"Transaction_Succesfully")
        self.Transaction_Succesfully.setMaximumSize(QSize(16777215, 16777215))
        self.Transaction_Succesfully.setStyleSheet(u"	font: bold;\n"
"	font-size: 14px;\n"
"	color: green;\n"
"\n"
"font-weight: bold;\n"
"background:transparent;\n"
"")
        self.Transaction_Succesfully.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.Transaction_Succesfully)


        self.verticalLayout_48.addWidget(self.frame_112)

        self.frame_113 = QFrame(self.frame_110)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMaximumSize(QSize(16777215, 40))
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_71.setSpacing(4)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.Transaction_Fail = QLabel(self.frame_113)
        self.Transaction_Fail.setObjectName(u"Transaction_Fail")
        self.Transaction_Fail.setMaximumSize(QSize(16777215, 16777215))
        self.Transaction_Fail.setStyleSheet(u"	font: bold;\n"
"	font-size: 14px;\n"
"	color: rgb(196, 49, 69);\n"
"\n"
"font-weight: bold;\n"
"background:transparent;\n"
"")
        self.Transaction_Fail.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.Transaction_Fail)


        self.verticalLayout_48.addWidget(self.frame_113)

        self.frame_114 = QFrame(self.frame_110)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_114)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.Input_TX_HEX = QLineEdit(self.frame_114)
        self.Input_TX_HEX.setObjectName(u"Input_TX_HEX")
        self.Input_TX_HEX.setMinimumSize(QSize(325, 30))
        self.Input_TX_HEX.setMaximumSize(QSize(16777215, 16777215))
        self.Input_TX_HEX.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#dca101;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Input_TX_HEX.setMaxLength(999999999)
        self.Input_TX_HEX.setClearButtonEnabled(True)

        self.verticalLayout_50.addWidget(self.Input_TX_HEX)


        self.verticalLayout_48.addWidget(self.frame_114)

        self.frame_115 = QFrame(self.frame_110)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMaximumSize(QSize(16777215, 40))
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_72.setSpacing(4)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Status_OK = QPushButton(self.frame_115)
        self.pushButton_Status_OK.setObjectName(u"pushButton_Status_OK")
        self.pushButton_Status_OK.setMinimumSize(QSize(0, 30))
        self.pushButton_Status_OK.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: green;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_72.addWidget(self.pushButton_Status_OK)


        self.verticalLayout_48.addWidget(self.frame_115)


        self.verticalLayout_49.addWidget(self.frame_110)

        self.stackedWidget_16.addWidget(self.page_TX_Status)
        self.page_LimitOrder = QWidget()
        self.page_LimitOrder.setObjectName(u"page_LimitOrder")
        self.verticalLayout_52 = QVBoxLayout(self.page_LimitOrder)
        self.verticalLayout_52.setSpacing(2)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_116 = QFrame(self.page_LimitOrder)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_116)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.frame_116)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(16777215, 50))
        self.label_46.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 14pt;")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.label_46)

        self.frame_117 = QFrame(self.frame_116)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setMaximumSize(QSize(16777215, 40))
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_73.setSpacing(6)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.Order_OrderType = QLabel(self.frame_117)
        self.Order_OrderType.setObjectName(u"Order_OrderType")
        self.Order_OrderType.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Order_OrderType.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_73.addWidget(self.Order_OrderType)

        self.Order_Amount = QLabel(self.frame_117)
        self.Order_Amount.setObjectName(u"Order_Amount")
        self.Order_Amount.setLayoutDirection(Qt.RightToLeft)
        self.Order_Amount.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Order_Amount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_73.addWidget(self.Order_Amount)

        self.Order_Symbol_In = QLabel(self.frame_117)
        self.Order_Symbol_In.setObjectName(u"Order_Symbol_In")
        self.Order_Symbol_In.setMaximumSize(QSize(40, 16777215))
        self.Order_Symbol_In.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")

        self.horizontalLayout_73.addWidget(self.Order_Symbol_In)

        self.label_47 = QLabel(self.frame_117)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(50, 16777215))
        self.label_47.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")

        self.horizontalLayout_73.addWidget(self.label_47)

        self.Order_Price = QLabel(self.frame_117)
        self.Order_Price.setObjectName(u"Order_Price")
        self.Order_Price.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Order_Price.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_73.addWidget(self.Order_Price)


        self.verticalLayout_51.addWidget(self.frame_117)

        self.frame_118 = QFrame(self.frame_116)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMaximumSize(QSize(16777215, 40))
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_118)
        self.horizontalLayout_74.setSpacing(4)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.Confirm_Orderway = QLabel(self.frame_118)
        self.Confirm_Orderway.setObjectName(u"Confirm_Orderway")
        self.Confirm_Orderway.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 14pt;")
        self.Confirm_Orderway.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.Confirm_Orderway)


        self.verticalLayout_51.addWidget(self.frame_118)

        self.frame_119 = QFrame(self.frame_116)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)

        self.verticalLayout_51.addWidget(self.frame_119)

        self.frame_120 = QFrame(self.frame_116)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMaximumSize(QSize(16777215, 40))
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_75.setSpacing(4)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Cancel_Order = QPushButton(self.frame_120)
        self.pushButton_Cancel_Order.setObjectName(u"pushButton_Cancel_Order")
        self.pushButton_Cancel_Order.setMinimumSize(QSize(0, 30))
        self.pushButton_Cancel_Order.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(196, 49, 69) ;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_75.addWidget(self.pushButton_Cancel_Order)

        self.pushButton_Submit_Order = QPushButton(self.frame_120)
        self.pushButton_Submit_Order.setObjectName(u"pushButton_Submit_Order")
        self.pushButton_Submit_Order.setMinimumSize(QSize(0, 30))
        self.pushButton_Submit_Order.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: green;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_75.addWidget(self.pushButton_Submit_Order)


        self.verticalLayout_51.addWidget(self.frame_120)


        self.verticalLayout_52.addWidget(self.frame_116)

        self.stackedWidget_16.addWidget(self.page_LimitOrder)

        self.verticalLayout.addWidget(self.stackedWidget_16)

        self.stackedWidget_17 = QStackedWidget(self.frame_4)
        self.stackedWidget_17.setObjectName(u"stackedWidget_17")
        self.stackedWidget_17.setMinimumSize(QSize(0, 170))
        self.stackedWidget_17.setMaximumSize(QSize(16777215, 200))
        self.stackedWidget_17.setStyleSheet(u"")
        self.stackedWidget_17.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_17.setFrameShadow(QFrame.Raised)
        self.Trade_Market = QWidget()
        self.Trade_Market.setObjectName(u"Trade_Market")
        self.Trade_Market.setMinimumSize(QSize(0, 80))
        self.Trade_Market.setMaximumSize(QSize(16777215, 280))
        self.Trade_Market.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.verticalLayout_11 = QVBoxLayout(self.Trade_Market)
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.Trade_Market)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_31)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_31)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))
        self.label_13.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 16pt;")
        self.label_13.setFrameShape(QFrame.NoFrame)
        self.label_13.setFrameShadow(QFrame.Plain)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_13)

        self.frame_16 = QFrame(self.frame_31)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_18.setSpacing(2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_16)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border: 3px solid  rgba(27, 29, 35, 200);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_27)
        self.verticalLayout_37.setSpacing(2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_84 = QFrame(self.frame_27)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMaximumSize(QSize(16777215, 14))
        self.frame_84.setStyleSheet(u"border:None;")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_47.setSpacing(2)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frame_84)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(100, 0))
        self.label_41.setMaximumSize(QSize(16777215, 12))
        self.label_41.setStyleSheet(u"color:green;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_41.setFrameShape(QFrame.NoFrame)
        self.label_41.setFrameShadow(QFrame.Plain)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.label_41)

        self.label_15 = QLabel(self.frame_84)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 16777215))
        self.label_15.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_15.setFrameShape(QFrame.NoFrame)
        self.label_15.setFrameShadow(QFrame.Plain)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.label_15)

        self.label_token_BuyTax = QLabel(self.frame_84)
        self.label_token_BuyTax.setObjectName(u"label_token_BuyTax")
        self.label_token_BuyTax.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;")
        self.label_token_BuyTax.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.label_token_BuyTax)


        self.verticalLayout_37.addWidget(self.frame_84)

        self.TokenName_MB = QLabel(self.frame_27)
        self.TokenName_MB.setObjectName(u"TokenName_MB")
        self.TokenName_MB.setMinimumSize(QSize(0, 0))
        self.TokenName_MB.setMaximumSize(QSize(16777215, 15))
        self.TokenName_MB.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;\n"
"border:None;")
        self.TokenName_MB.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.TokenName_MB)

        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 0))
        self.frame_28.setMaximumSize(QSize(16777215, 30))
        self.frame_28.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border:None;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_28)
        self.verticalLayout_35.setSpacing(2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.frame_28)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(16777215, 25))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_31.setSpacing(2)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_34)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(40, 20))
        self.label_30.setLayoutDirection(Qt.LeftToRight)
        self.label_30.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_30)

        self.Button_Base_BNB_MB = QPushButton(self.frame_34)
        self.Button_Base_BNB_MB.setObjectName(u"Button_Base_BNB_MB")
        self.Button_Base_BNB_MB.setMinimumSize(QSize(1, 0))
        self.Button_Base_BNB_MB.setLayoutDirection(Qt.LeftToRight)
        self.Button_Base_BNB_MB.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Base_BNB_MB.setCheckable(False)

        self.horizontalLayout_31.addWidget(self.Button_Base_BNB_MB)

        self.Button_Base_BUSD_MB = QPushButton(self.frame_34)
        self.Button_Base_BUSD_MB.setObjectName(u"Button_Base_BUSD_MB")
        self.Button_Base_BUSD_MB.setMinimumSize(QSize(1, 0))
        self.Button_Base_BUSD_MB.setLayoutDirection(Qt.LeftToRight)
        self.Button_Base_BUSD_MB.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Base_BUSD_MB.setCheckable(False)

        self.horizontalLayout_31.addWidget(self.Button_Base_BUSD_MB)


        self.verticalLayout_35.addWidget(self.frame_34)


        self.verticalLayout_37.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 40))
        self.frame_29.setStyleSheet(u"border:None;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_29)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 20))
        self.label_29.setLayoutDirection(Qt.LeftToRight)
        self.label_29.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_29)

        self.Input_MB = QLineEdit(self.frame_29)
        self.Input_MB.setObjectName(u"Input_MB")
        self.Input_MB.setMinimumSize(QSize(0, 0))
        self.Input_MB.setMaximumSize(QSize(200, 16777215))
        self.Input_MB.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Input_MB.setMaxLength(1000)
        self.Input_MB.setAlignment(Qt.AlignCenter)
        self.Input_MB.setClearButtonEnabled(True)

        self.horizontalLayout_25.addWidget(self.Input_MB)

        self.Input_MB_tokenSymbol = QLabel(self.frame_29)
        self.Input_MB_tokenSymbol.setObjectName(u"Input_MB_tokenSymbol")
        self.Input_MB_tokenSymbol.setMinimumSize(QSize(40, 0))
        self.Input_MB_tokenSymbol.setMaximumSize(QSize(16777215, 16777215))
        self.Input_MB_tokenSymbol.setLayoutDirection(Qt.LeftToRight)
        self.Input_MB_tokenSymbol.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Input_MB_tokenSymbol.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.Input_MB_tokenSymbol)


        self.verticalLayout_37.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_27)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 40))
        self.frame_30.setStyleSheet(u"border:None;")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_32.setSpacing(6)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_30)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 20))
        self.label_31.setLayoutDirection(Qt.LeftToRight)
        self.label_31.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_31)

        self.Output_MB = QLineEdit(self.frame_30)
        self.Output_MB.setObjectName(u"Output_MB")
        self.Output_MB.setMinimumSize(QSize(0, 0))
        self.Output_MB.setMaximumSize(QSize(200, 16777215))
        self.Output_MB.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Output_MB.setMaxLength(1000)
        self.Output_MB.setAlignment(Qt.AlignCenter)
        self.Output_MB.setClearButtonEnabled(True)

        self.horizontalLayout_32.addWidget(self.Output_MB)

        self.Output_MB_tokenSymbol = QLabel(self.frame_30)
        self.Output_MB_tokenSymbol.setObjectName(u"Output_MB_tokenSymbol")
        self.Output_MB_tokenSymbol.setMinimumSize(QSize(40, 0))
        self.Output_MB_tokenSymbol.setMaximumSize(QSize(16777215, 16777215))
        self.Output_MB_tokenSymbol.setLayoutDirection(Qt.LeftToRight)
        self.Output_MB_tokenSymbol.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Output_MB_tokenSymbol.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.Output_MB_tokenSymbol)


        self.verticalLayout_37.addWidget(self.frame_30)

        self.frame_14 = QFrame(self.frame_27)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"border:None;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_19)

        self.ButtonExecute_MB = QPushButton(self.frame_14)
        self.ButtonExecute_MB.setObjectName(u"ButtonExecute_MB")
        self.ButtonExecute_MB.setMinimumSize(QSize(200, 25))
        self.ButtonExecute_MB.setMaximumSize(QSize(200, 16777215))
        self.ButtonExecute_MB.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 14px;\n"
"	color:green;\n"
"\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: green;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_16.addWidget(self.ButtonExecute_MB)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_15)


        self.verticalLayout_37.addWidget(self.frame_14)


        self.horizontalLayout_18.addWidget(self.frame_27)

        self.frame_33 = QFrame(self.frame_16)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frame_33)

        self.frame_56 = QFrame(self.frame_16)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setLayoutDirection(Qt.LeftToRight)
        self.frame_56.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border: 3px solid  rgba(27, 29, 35, 200);")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_56)
        self.verticalLayout_38.setSpacing(2)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_56)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 14))
        self.frame_8.setStyleSheet(u"border:None;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(100, 0))
        self.label_21.setMaximumSize(QSize(16777215, 12))
        self.label_21.setStyleSheet(u"color:rgb(196, 49, 69);\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_21.setFrameShape(QFrame.NoFrame)
        self.label_21.setFrameShadow(QFrame.Plain)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_21)

        self.label_34 = QLabel(self.frame_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 16777215))
        self.label_34.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_34.setFrameShape(QFrame.NoFrame)
        self.label_34.setFrameShadow(QFrame.Plain)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_34)

        self.label_token_SellTax = QLabel(self.frame_8)
        self.label_token_SellTax.setObjectName(u"label_token_SellTax")
        self.label_token_SellTax.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;")
        self.label_token_SellTax.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_token_SellTax)


        self.verticalLayout_38.addWidget(self.frame_8)

        self.TokenName_MS = QLabel(self.frame_56)
        self.TokenName_MS.setObjectName(u"TokenName_MS")
        self.TokenName_MS.setMinimumSize(QSize(0, 0))
        self.TokenName_MS.setMaximumSize(QSize(16777215, 15))
        self.TokenName_MS.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;\n"
"border:None;")
        self.TokenName_MS.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.TokenName_MS)

        self.frame_58 = QFrame(self.frame_56)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(0, 0))
        self.frame_58.setMaximumSize(QSize(16777215, 30))
        self.frame_58.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border:None;")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_58)
        self.verticalLayout_36.setSpacing(2)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMaximumSize(QSize(16777215, 25))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_33.setSpacing(6)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_59)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(20, 20))
        self.label_28.setLayoutDirection(Qt.LeftToRight)
        self.label_28.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_28)

        self.Button_Base_BNB_MS = QPushButton(self.frame_59)
        self.Button_Base_BNB_MS.setObjectName(u"Button_Base_BNB_MS")
        self.Button_Base_BNB_MS.setMinimumSize(QSize(1, 0))
        self.Button_Base_BNB_MS.setLayoutDirection(Qt.LeftToRight)
        self.Button_Base_BNB_MS.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Base_BNB_MS.setCheckable(False)

        self.horizontalLayout_33.addWidget(self.Button_Base_BNB_MS)

        self.Button_Base_BUSD_MS = QPushButton(self.frame_59)
        self.Button_Base_BUSD_MS.setObjectName(u"Button_Base_BUSD_MS")
        self.Button_Base_BUSD_MS.setMinimumSize(QSize(1, 0))
        self.Button_Base_BUSD_MS.setLayoutDirection(Qt.LeftToRight)
        self.Button_Base_BUSD_MS.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Base_BUSD_MS.setCheckable(False)

        self.horizontalLayout_33.addWidget(self.Button_Base_BUSD_MS)


        self.verticalLayout_36.addWidget(self.frame_59)


        self.verticalLayout_38.addWidget(self.frame_58)

        self.frame_60 = QFrame(self.frame_56)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMaximumSize(QSize(16777215, 40))
        self.frame_60.setStyleSheet(u"border:None;")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_34.setSpacing(6)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_60)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 20))
        self.label_32.setLayoutDirection(Qt.LeftToRight)
        self.label_32.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_32)

        self.Input_MS = QLineEdit(self.frame_60)
        self.Input_MS.setObjectName(u"Input_MS")
        self.Input_MS.setMinimumSize(QSize(0, 0))
        self.Input_MS.setMaximumSize(QSize(200, 16777215))
        self.Input_MS.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Input_MS.setMaxLength(1000)
        self.Input_MS.setAlignment(Qt.AlignCenter)
        self.Input_MS.setClearButtonEnabled(True)

        self.horizontalLayout_34.addWidget(self.Input_MS)

        self.Input_MS_tokenSymbol = QLabel(self.frame_60)
        self.Input_MS_tokenSymbol.setObjectName(u"Input_MS_tokenSymbol")
        self.Input_MS_tokenSymbol.setMinimumSize(QSize(40, 0))
        self.Input_MS_tokenSymbol.setMaximumSize(QSize(16777215, 16777215))
        self.Input_MS_tokenSymbol.setLayoutDirection(Qt.LeftToRight)
        self.Input_MS_tokenSymbol.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Input_MS_tokenSymbol.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.Input_MS_tokenSymbol)


        self.verticalLayout_38.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_56)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMaximumSize(QSize(16777215, 40))
        self.frame_61.setStyleSheet(u"border:None;")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_35.setSpacing(6)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_61)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 20))
        self.label_33.setLayoutDirection(Qt.LeftToRight)
        self.label_33.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_33)

        self.Output_MS = QLineEdit(self.frame_61)
        self.Output_MS.setObjectName(u"Output_MS")
        self.Output_MS.setMinimumSize(QSize(0, 0))
        self.Output_MS.setMaximumSize(QSize(200, 16777215))
        self.Output_MS.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Output_MS.setMaxLength(1000)
        self.Output_MS.setAlignment(Qt.AlignCenter)
        self.Output_MS.setClearButtonEnabled(True)

        self.horizontalLayout_35.addWidget(self.Output_MS)

        self.Output_MS_tokenSymbol = QLabel(self.frame_61)
        self.Output_MS_tokenSymbol.setObjectName(u"Output_MS_tokenSymbol")
        self.Output_MS_tokenSymbol.setMinimumSize(QSize(40, 0))
        self.Output_MS_tokenSymbol.setMaximumSize(QSize(16777215, 16777215))
        self.Output_MS_tokenSymbol.setLayoutDirection(Qt.LeftToRight)
        self.Output_MS_tokenSymbol.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Output_MS_tokenSymbol.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.Output_MS_tokenSymbol)


        self.verticalLayout_38.addWidget(self.frame_61)

        self.frame_5 = QFrame(self.frame_56)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setLayoutDirection(Qt.LeftToRight)
        self.frame_5.setStyleSheet(u"border:None;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_20)

        self.ButtonExecute_MS = QPushButton(self.frame_5)
        self.ButtonExecute_MS.setObjectName(u"ButtonExecute_MS")
        self.ButtonExecute_MS.setMinimumSize(QSize(200, 25))
        self.ButtonExecute_MS.setMaximumSize(QSize(200, 16777215))
        self.ButtonExecute_MS.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 14px;\n"
"	color: rgb(196, 49, 69) ;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(196, 49, 69);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.ButtonExecute_MS)

        self.frame_21 = QFrame(self.frame_5)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_21)


        self.verticalLayout_38.addWidget(self.frame_5)


        self.horizontalLayout_18.addWidget(self.frame_56)


        self.verticalLayout_6.addWidget(self.frame_16)


        self.verticalLayout_11.addWidget(self.frame_31)

        self.stackedWidget_17.addWidget(self.Trade_Market)
        self.Trade_Sniper = QWidget()
        self.Trade_Sniper.setObjectName(u"Trade_Sniper")
        self.Trade_Sniper.setMinimumSize(QSize(0, 150))
        self.Trade_Sniper.setAutoFillBackground(False)
        self.Trade_Sniper.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.verticalLayout_25 = QVBoxLayout(self.Trade_Sniper)
        self.verticalLayout_25.setSpacing(2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.Trade_Sniper)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_45)
        self.verticalLayout_22.setSpacing(2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_45)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 15))
        self.label_22.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_22.setFrameShape(QFrame.NoFrame)
        self.label_22.setFrameShadow(QFrame.Plain)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_22)

        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMaximumSize(QSize(16777215, 15))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_47)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_47)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color:rgb(44, 175, 125);\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_23.setFrameShape(QFrame.NoFrame)
        self.label_23.setFrameShadow(QFrame.Plain)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_23)


        self.horizontalLayout_29.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_46)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_48)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_48)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color:rgb(196, 49, 69);\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_24.setFrameShape(QFrame.NoFrame)
        self.label_24.setFrameShadow(QFrame.Plain)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_24)


        self.horizontalLayout_29.addWidget(self.frame_48)


        self.verticalLayout_22.addWidget(self.frame_46)

        self.frame_49 = QFrame(self.frame_45)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_30.setSpacing(2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_30.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_49)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_30.addWidget(self.frame_51)


        self.verticalLayout_22.addWidget(self.frame_49)


        self.verticalLayout_25.addWidget(self.frame_45)

        self.stackedWidget_17.addWidget(self.Trade_Sniper)
        self.Trade_Limit = QWidget()
        self.Trade_Limit.setObjectName(u"Trade_Limit")
        self.Trade_Limit.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.verticalLayout_19 = QVBoxLayout(self.Trade_Limit)
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.Trade_Limit)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_36)
        self.verticalLayout_14.setSpacing(2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_36)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 20))
        self.label_16.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 16pt;")
        self.label_16.setFrameShape(QFrame.NoFrame)
        self.label_16.setFrameShadow(QFrame.Plain)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_16)

        self.frame_32 = QFrame(self.frame_36)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_24.setSpacing(2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_32)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border: 3px solid  rgba(27, 29, 35, 200);")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_38)
        self.verticalLayout_39.setSpacing(2)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.frame_38)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMaximumSize(QSize(16777215, 14))
        self.frame_85.setStyleSheet(u"border:None;")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_50.setSpacing(2)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame_85)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(100, 0))
        self.label_44.setMaximumSize(QSize(16777215, 12))
        self.label_44.setStyleSheet(u"color:green;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_44.setFrameShape(QFrame.NoFrame)
        self.label_44.setFrameShadow(QFrame.Plain)
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_44)

        self.label_18 = QLabel(self.frame_85)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 16777215))
        self.label_18.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_18.setFrameShape(QFrame.NoFrame)
        self.label_18.setFrameShadow(QFrame.Plain)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_18)

        self.label_token_BuyTax_2 = QLabel(self.frame_85)
        self.label_token_BuyTax_2.setObjectName(u"label_token_BuyTax_2")
        self.label_token_BuyTax_2.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;")
        self.label_token_BuyTax_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_token_BuyTax_2)


        self.verticalLayout_39.addWidget(self.frame_85)

        self.TokenName_LB = QLabel(self.frame_38)
        self.TokenName_LB.setObjectName(u"TokenName_LB")
        self.TokenName_LB.setMinimumSize(QSize(0, 0))
        self.TokenName_LB.setMaximumSize(QSize(16777215, 15))
        self.TokenName_LB.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;\n"
"Border:None;")
        self.TokenName_LB.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.TokenName_LB)

        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 0))
        self.frame_40.setMaximumSize(QSize(16777215, 25))
        self.frame_40.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"Border:None;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_40)
        self.verticalLayout_40.setSpacing(2)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(16777215, 25))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_36.setSpacing(2)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_41)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(40, 20))
        self.label_35.setLayoutDirection(Qt.LeftToRight)
        self.label_35.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_35)

        self.Button_Base_BNB_LB = QPushButton(self.frame_41)
        self.Button_Base_BNB_LB.setObjectName(u"Button_Base_BNB_LB")
        self.Button_Base_BNB_LB.setMinimumSize(QSize(1, 0))
        self.Button_Base_BNB_LB.setLayoutDirection(Qt.LeftToRight)
        self.Button_Base_BNB_LB.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Base_BNB_LB.setCheckable(False)

        self.horizontalLayout_36.addWidget(self.Button_Base_BNB_LB)

        self.Button_Base_BUSD_LB = QPushButton(self.frame_41)
        self.Button_Base_BUSD_LB.setObjectName(u"Button_Base_BUSD_LB")
        self.Button_Base_BUSD_LB.setMinimumSize(QSize(1, 0))
        self.Button_Base_BUSD_LB.setLayoutDirection(Qt.LeftToRight)
        self.Button_Base_BUSD_LB.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Base_BUSD_LB.setCheckable(False)

        self.horizontalLayout_36.addWidget(self.Button_Base_BUSD_LB)


        self.verticalLayout_40.addWidget(self.frame_41)


        self.verticalLayout_39.addWidget(self.frame_40)

        self.frame_42 = QFrame(self.frame_38)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"Border:None;")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_28.setSpacing(6)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_42)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(16777215, 20))
        self.label_36.setLayoutDirection(Qt.LeftToRight)
        self.label_36.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_36)

        self.Input_LB = QLineEdit(self.frame_42)
        self.Input_LB.setObjectName(u"Input_LB")
        self.Input_LB.setMinimumSize(QSize(0, 0))
        self.Input_LB.setMaximumSize(QSize(200, 16777215))
        self.Input_LB.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;	\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Input_LB.setMaxLength(43)
        self.Input_LB.setAlignment(Qt.AlignCenter)
        self.Input_LB.setClearButtonEnabled(True)

        self.horizontalLayout_28.addWidget(self.Input_LB)

        self.Input_LB_tokenSymbol = QLabel(self.frame_42)
        self.Input_LB_tokenSymbol.setObjectName(u"Input_LB_tokenSymbol")
        self.Input_LB_tokenSymbol.setMinimumSize(QSize(40, 0))
        self.Input_LB_tokenSymbol.setMaximumSize(QSize(16777215, 16777215))
        self.Input_LB_tokenSymbol.setLayoutDirection(Qt.LeftToRight)
        self.Input_LB_tokenSymbol.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Input_LB_tokenSymbol.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.Input_LB_tokenSymbol)


        self.verticalLayout_39.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_38)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"Border:None;")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_37.setSpacing(6)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_43)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 20))
        self.label_37.setLayoutDirection(Qt.LeftToRight)
        self.label_37.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_37)

        self.Price_LB = QLineEdit(self.frame_43)
        self.Price_LB.setObjectName(u"Price_LB")
        self.Price_LB.setMinimumSize(QSize(0, 0))
        self.Price_LB.setMaximumSize(QSize(200, 16777215))
        self.Price_LB.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Price_LB.setMaxLength(43)
        self.Price_LB.setAlignment(Qt.AlignCenter)
        self.Price_LB.setClearButtonEnabled(True)

        self.horizontalLayout_37.addWidget(self.Price_LB)

        self.Output_LB_tokenSymbol = QLabel(self.frame_43)
        self.Output_LB_tokenSymbol.setObjectName(u"Output_LB_tokenSymbol")
        self.Output_LB_tokenSymbol.setMinimumSize(QSize(40, 0))
        self.Output_LB_tokenSymbol.setMaximumSize(QSize(16777215, 16777215))
        self.Output_LB_tokenSymbol.setLayoutDirection(Qt.LeftToRight)
        self.Output_LB_tokenSymbol.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Output_LB_tokenSymbol.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.Output_LB_tokenSymbol)


        self.verticalLayout_39.addWidget(self.frame_43)

        self.frame_75 = QFrame(self.frame_38)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setLayoutDirection(Qt.LeftToRight)
        self.frame_75.setStyleSheet(u"Border:None;")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_77 = QFrame(self.frame_75)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMaximumSize(QSize(16777215, 16777215))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_77)

        self.ButtonPlace_LB = QPushButton(self.frame_75)
        self.ButtonPlace_LB.setObjectName(u"ButtonPlace_LB")
        self.ButtonPlace_LB.setMinimumSize(QSize(200, 25))
        self.ButtonPlace_LB.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 14px;\n"
"	color: green;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color:green;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_19.addWidget(self.ButtonPlace_LB)

        self.frame_76 = QFrame(self.frame_75)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_76)


        self.verticalLayout_39.addWidget(self.frame_75)


        self.horizontalLayout_24.addWidget(self.frame_38)

        self.frame_62 = QFrame(self.frame_32)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_24.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_32)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border: 3px solid  rgba(27, 29, 35, 200);")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_63)
        self.verticalLayout_41.setSpacing(2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_64 = QFrame(self.frame_63)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMaximumSize(QSize(16777215, 14))
        self.frame_64.setStyleSheet(u"border:None;")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_49.setSpacing(2)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_64)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(100, 0))
        self.label_42.setMaximumSize(QSize(16777215, 12))
        self.label_42.setStyleSheet(u"color:rgb(196, 49, 69);\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_42.setFrameShape(QFrame.NoFrame)
        self.label_42.setFrameShadow(QFrame.Plain)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_42)

        self.label_43 = QLabel(self.frame_64)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 16777215))
        self.label_43.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_43.setFrameShape(QFrame.NoFrame)
        self.label_43.setFrameShadow(QFrame.Plain)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_43)

        self.label_token_SellTax_2 = QLabel(self.frame_64)
        self.label_token_SellTax_2.setObjectName(u"label_token_SellTax_2")
        self.label_token_SellTax_2.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;")
        self.label_token_SellTax_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_token_SellTax_2)


        self.verticalLayout_41.addWidget(self.frame_64)

        self.TokenName_LS = QLabel(self.frame_63)
        self.TokenName_LS.setObjectName(u"TokenName_LS")
        self.TokenName_LS.setMinimumSize(QSize(0, 0))
        self.TokenName_LS.setMaximumSize(QSize(16777215, 15))
        self.TokenName_LS.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;\n"
"Border:None;")
        self.TokenName_LS.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.TokenName_LS)

        self.frame_65 = QFrame(self.frame_63)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(0, 23))
        self.frame_65.setMaximumSize(QSize(16777215, 25))
        self.frame_65.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"Border:None;")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_65)
        self.verticalLayout_42.setSpacing(2)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(0, 20))
        self.frame_66.setMaximumSize(QSize(16777215, 25))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_38.setSpacing(2)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_66)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(20, 20))
        self.label_38.setLayoutDirection(Qt.LeftToRight)
        self.label_38.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_38)

        self.Button_Base_BNB_LS = QPushButton(self.frame_66)
        self.Button_Base_BNB_LS.setObjectName(u"Button_Base_BNB_LS")
        self.Button_Base_BNB_LS.setMinimumSize(QSize(1, 0))
        self.Button_Base_BNB_LS.setLayoutDirection(Qt.LeftToRight)
        self.Button_Base_BNB_LS.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Base_BNB_LS.setCheckable(False)

        self.horizontalLayout_38.addWidget(self.Button_Base_BNB_LS)

        self.Button_Base_BUSD_LS = QPushButton(self.frame_66)
        self.Button_Base_BUSD_LS.setObjectName(u"Button_Base_BUSD_LS")
        self.Button_Base_BUSD_LS.setMinimumSize(QSize(1, 0))
        self.Button_Base_BUSD_LS.setLayoutDirection(Qt.LeftToRight)
        self.Button_Base_BUSD_LS.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Base_BUSD_LS.setCheckable(False)

        self.horizontalLayout_38.addWidget(self.Button_Base_BUSD_LS)


        self.verticalLayout_42.addWidget(self.frame_66)


        self.verticalLayout_41.addWidget(self.frame_65)

        self.frame_67 = QFrame(self.frame_63)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setStyleSheet(u"Border:None;")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_39.setSpacing(6)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_67)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 20))
        self.label_39.setLayoutDirection(Qt.LeftToRight)
        self.label_39.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_39)

        self.Input_LS = QLineEdit(self.frame_67)
        self.Input_LS.setObjectName(u"Input_LS")
        self.Input_LS.setMinimumSize(QSize(0, 0))
        self.Input_LS.setMaximumSize(QSize(200, 16777215))
        self.Input_LS.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Input_LS.setMaxLength(43)
        self.Input_LS.setAlignment(Qt.AlignCenter)
        self.Input_LS.setClearButtonEnabled(True)

        self.horizontalLayout_39.addWidget(self.Input_LS)

        self.Input_LS_tokenSymbol = QLabel(self.frame_67)
        self.Input_LS_tokenSymbol.setObjectName(u"Input_LS_tokenSymbol")
        self.Input_LS_tokenSymbol.setMinimumSize(QSize(40, 0))
        self.Input_LS_tokenSymbol.setMaximumSize(QSize(16777215, 16777215))
        self.Input_LS_tokenSymbol.setLayoutDirection(Qt.LeftToRight)
        self.Input_LS_tokenSymbol.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Input_LS_tokenSymbol.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.Input_LS_tokenSymbol)


        self.verticalLayout_41.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.frame_63)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setStyleSheet(u"Border:None;")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_40.setSpacing(6)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_68)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 20))
        self.label_40.setLayoutDirection(Qt.LeftToRight)
        self.label_40.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_40)

        self.Price_LS = QLineEdit(self.frame_68)
        self.Price_LS.setObjectName(u"Price_LS")
        self.Price_LS.setMinimumSize(QSize(0, 0))
        self.Price_LS.setMaximumSize(QSize(200, 16777215))
        self.Price_LS.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Price_LS.setMaxLength(43)
        self.Price_LS.setAlignment(Qt.AlignCenter)
        self.Price_LS.setClearButtonEnabled(True)

        self.horizontalLayout_40.addWidget(self.Price_LS)

        self.Output_LS_tokenSymbol = QLabel(self.frame_68)
        self.Output_LS_tokenSymbol.setObjectName(u"Output_LS_tokenSymbol")
        self.Output_LS_tokenSymbol.setMinimumSize(QSize(40, 0))
        self.Output_LS_tokenSymbol.setMaximumSize(QSize(16777215, 16777215))
        self.Output_LS_tokenSymbol.setLayoutDirection(Qt.LeftToRight)
        self.Output_LS_tokenSymbol.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Output_LS_tokenSymbol.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.Output_LS_tokenSymbol)


        self.verticalLayout_41.addWidget(self.frame_68)

        self.frame_22 = QFrame(self.frame_63)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setLayoutDirection(Qt.LeftToRight)
        self.frame_22.setStyleSheet(u"Border:None;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_17.setSpacing(2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.frame_22)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(0, 0))
        self.frame_57.setMaximumSize(QSize(16777215, 16777215))
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_57)

        self.ButtonPlace_LS = QPushButton(self.frame_22)
        self.ButtonPlace_LS.setObjectName(u"ButtonPlace_LS")
        self.ButtonPlace_LS.setMinimumSize(QSize(200, 25))
        self.ButtonPlace_LS.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 14px;\n"
"	color: rgb(196, 49, 69) ;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(196, 49, 69);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_17.addWidget(self.ButtonPlace_LS)

        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_25)


        self.verticalLayout_41.addWidget(self.frame_22)


        self.horizontalLayout_24.addWidget(self.frame_63)


        self.verticalLayout_14.addWidget(self.frame_32)


        self.verticalLayout_19.addWidget(self.frame_36)

        self.stackedWidget_17.addWidget(self.Trade_Limit)

        self.verticalLayout.addWidget(self.stackedWidget_17)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout_23.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frame_17)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(250, 550))
        self.frame_7.setMaximumSize(QSize(380, 16777215))
        self.frame_7.setStyleSheet(u"background-color: rgba(27, 29, 35, 200);\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_7)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_23)
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.MENU = QFrame(self.frame_23)
        self.MENU.setObjectName(u"MENU")
        self.MENU.setMinimumSize(QSize(0, 72))
        self.MENU.setMaximumSize(QSize(16777215, 72))
        self.MENU.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"")
        self.MENU.setFrameShape(QFrame.StyledPanel)
        self.MENU.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.MENU)
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.MENU)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 20))
        self.label_17.setLayoutDirection(Qt.LeftToRight)
        self.label_17.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_17)

        self.frame_35 = QFrame(self.MENU)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 0))
        self.frame_35.setMaximumSize(QSize(16777215, 16777215))
        self.frame_35.setStyleSheet(u"")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_26.setSpacing(2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Wallet = QPushButton(self.frame_35)
        self.pushButton_Wallet.setObjectName(u"pushButton_Wallet")
        self.pushButton_Wallet.setMinimumSize(QSize(0, 30))
        self.pushButton_Wallet.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_26.addWidget(self.pushButton_Wallet)

        self.pushButton_Orders = QPushButton(self.frame_35)
        self.pushButton_Orders.setObjectName(u"pushButton_Orders")
        self.pushButton_Orders.setMinimumSize(QSize(0, 30))
        self.pushButton_Orders.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 0%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_26.addWidget(self.pushButton_Orders)

        self.pushButton_Settings = QPushButton(self.frame_35)
        self.pushButton_Settings.setObjectName(u"pushButton_Settings")
        self.pushButton_Settings.setMinimumSize(QSize(0, 30))
        self.pushButton_Settings.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 0%;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_26.addWidget(self.pushButton_Settings)


        self.verticalLayout_13.addWidget(self.frame_35)


        self.verticalLayout_15.addWidget(self.MENU)

        self.stackedWidget_2 = QStackedWidget(self.frame_23)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"")
        self.WalletOverview = QWidget()
        self.WalletOverview.setObjectName(u"WalletOverview")
        self.WalletOverview.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.WalletOverview)
        self.verticalLayout_17.setSpacing(2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.WalletOverview)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_39)
        self.verticalLayout_21.setSpacing(2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_39)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 20))
        self.label_19.setLayoutDirection(Qt.LeftToRight)
        self.label_19.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_19)

        self.Balance_all = QLabel(self.frame_39)
        self.Balance_all.setObjectName(u"Balance_all")
        self.Balance_all.setMaximumSize(QSize(16777215, 20))
        self.Balance_all.setLayoutDirection(Qt.LeftToRight)
        self.Balance_all.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.Balance_all.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.Balance_all)

        self.frame_44 = QFrame(self.frame_39)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_44)
        self.verticalLayout_27.setSpacing(2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(6, 6, 6, 6)
        self.scrollArea = QScrollArea(self.frame_44)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: 3px solid  rgba(27, 29, 35, 200);")
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 354, 673))
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_27.addWidget(self.scrollArea)


        self.verticalLayout_21.addWidget(self.frame_44)


        self.verticalLayout_17.addWidget(self.frame_39)

        self.stackedWidget_2.addWidget(self.WalletOverview)
        self.OrdersOverview = QWidget()
        self.OrdersOverview.setObjectName(u"OrdersOverview")
        self.verticalLayout_31 = QVBoxLayout(self.OrdersOverview)
        self.verticalLayout_31.setSpacing(2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.OrdersOverview)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_52)
        self.verticalLayout_29.setSpacing(2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_52)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 20))
        self.label_25.setLayoutDirection(Qt.LeftToRight)
        self.label_25.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_25)

        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_53)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea_orders = QScrollArea(self.frame_53)
        self.scrollArea_orders.setObjectName(u"scrollArea_orders")
        self.scrollArea_orders.setStyleSheet(u"border: 3px solid  rgba(27, 29, 35, 200);")
        self.scrollArea_orders.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_orders.setWidgetResizable(True)
        self.scrollArea_ordersWidgetContents = QWidget()
        self.scrollArea_ordersWidgetContents.setObjectName(u"scrollArea_ordersWidgetContents")
        self.scrollArea_ordersWidgetContents.setGeometry(QRect(0, 0, 348, 647))
        self.scrollArea_ordersWidgetContents.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout_8 = QVBoxLayout(self.scrollArea_ordersWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_orders.setWidget(self.scrollArea_ordersWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea_orders)

        self.frame_100 = QFrame(self.frame_53)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(0, 0))
        self.frame_100.setMaximumSize(QSize(16777215, 40))
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_61.setSpacing(2)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_101 = QFrame(self.frame_100)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMinimumSize(QSize(200, 0))
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_Slippage_7 = QLabel(self.frame_101)
        self.label_Slippage_7.setObjectName(u"label_Slippage_7")
        self.label_Slippage_7.setMaximumSize(QSize(65, 16777215))
        self.label_Slippage_7.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"border:None;")
        self.label_Slippage_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.label_Slippage_7)

        self.label_Status_LIMITORDERS = QLabel(self.frame_101)
        self.label_Status_LIMITORDERS.setObjectName(u"label_Status_LIMITORDERS")
        self.label_Status_LIMITORDERS.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_Status_LIMITORDERS.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.label_Status_LIMITORDERS)


        self.horizontalLayout_61.addWidget(self.frame_101)

        self.pushButton_STOP_LimitOrders = QPushButton(self.frame_100)
        self.pushButton_STOP_LimitOrders.setObjectName(u"pushButton_STOP_LimitOrders")
        self.pushButton_STOP_LimitOrders.setMinimumSize(QSize(0, 30))
        self.pushButton_STOP_LimitOrders.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 12px;\n"
"	color: rgb(196, 49, 69) ;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(196, 49, 69);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_61.addWidget(self.pushButton_STOP_LimitOrders)

        self.pushButton_START_LimitOrders = QPushButton(self.frame_100)
        self.pushButton_START_LimitOrders.setObjectName(u"pushButton_START_LimitOrders")
        self.pushButton_START_LimitOrders.setMinimumSize(QSize(0, 30))
        self.pushButton_START_LimitOrders.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 12px;\n"
"	color: green;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color:green;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_61.addWidget(self.pushButton_START_LimitOrders)


        self.verticalLayout_9.addWidget(self.frame_100)


        self.verticalLayout_29.addWidget(self.frame_53)


        self.verticalLayout_31.addWidget(self.frame_52)

        self.stackedWidget_2.addWidget(self.OrdersOverview)
        self.SettingsOverview = QWidget()
        self.SettingsOverview.setObjectName(u"SettingsOverview")
        self.verticalLayout_34 = QVBoxLayout(self.SettingsOverview)
        self.verticalLayout_34.setSpacing(2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.SettingsOverview)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_54)
        self.verticalLayout_32.setSpacing(2)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(4, 0, 4, 0)
        self.label_26 = QLabel(self.frame_54)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 20))
        self.label_26.setLayoutDirection(Qt.LeftToRight)
        self.label_26.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_26)

        self.frame_78 = QFrame(self.frame_54)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMaximumSize(QSize(16777215, 40))
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_Slippage = QLabel(self.frame_78)
        self.label_Slippage.setObjectName(u"label_Slippage")
        self.label_Slippage.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"border:None;")

        self.horizontalLayout_44.addWidget(self.label_Slippage)

        self.Input_Settings_Address = QLineEdit(self.frame_78)
        self.Input_Settings_Address.setObjectName(u"Input_Settings_Address")
        self.Input_Settings_Address.setMinimumSize(QSize(0, 30))
        self.Input_Settings_Address.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Input_Settings_Address.setMaxLength(1000)
        self.Input_Settings_Address.setAlignment(Qt.AlignCenter)
        self.Input_Settings_Address.setClearButtonEnabled(True)

        self.horizontalLayout_44.addWidget(self.Input_Settings_Address)


        self.verticalLayout_32.addWidget(self.frame_78)

        self.frame_79 = QFrame(self.frame_54)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMaximumSize(QSize(16777215, 60))
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_79)
        self.verticalLayout_30.setSpacing(2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_Slippage_5 = QLabel(self.frame_79)
        self.label_Slippage_5.setObjectName(u"label_Slippage_5")
        self.label_Slippage_5.setMaximumSize(QSize(16777215, 15))
        self.label_Slippage_5.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"border:None;\n"
"")
        self.label_Slippage_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_Slippage_5)

        self.Input_Settings_PrivateKey = QLineEdit(self.frame_79)
        self.Input_Settings_PrivateKey.setObjectName(u"Input_Settings_PrivateKey")
        self.Input_Settings_PrivateKey.setMinimumSize(QSize(0, 30))
        self.Input_Settings_PrivateKey.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Input_Settings_PrivateKey.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.Input_Settings_PrivateKey.setInputMethodHints(Qt.ImhHiddenText)
        self.Input_Settings_PrivateKey.setMaxLength(1000)
        self.Input_Settings_PrivateKey.setAlignment(Qt.AlignCenter)
        self.Input_Settings_PrivateKey.setClearButtonEnabled(False)

        self.verticalLayout_30.addWidget(self.Input_Settings_PrivateKey)


        self.verticalLayout_32.addWidget(self.frame_79)

        self.frame_82 = QFrame(self.frame_54)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMaximumSize(QSize(16777215, 40))
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_Slippage_6 = QLabel(self.frame_82)
        self.label_Slippage_6.setObjectName(u"label_Slippage_6")
        self.label_Slippage_6.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"border:None;")

        self.horizontalLayout_48.addWidget(self.label_Slippage_6)

        self.Input_Settings_provider = QLineEdit(self.frame_82)
        self.Input_Settings_provider.setObjectName(u"Input_Settings_provider")
        self.Input_Settings_provider.setMinimumSize(QSize(0, 30))
        self.Input_Settings_provider.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Input_Settings_provider.setMaxLength(1000)
        self.Input_Settings_provider.setAlignment(Qt.AlignCenter)
        self.Input_Settings_provider.setClearButtonEnabled(True)

        self.horizontalLayout_48.addWidget(self.Input_Settings_provider)


        self.verticalLayout_32.addWidget(self.frame_82)

        self.frame_80 = QFrame(self.frame_54)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(0, 40))
        self.frame_80.setMaximumSize(QSize(16777215, 40))
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_Slippage_2 = QLabel(self.frame_80)
        self.label_Slippage_2.setObjectName(u"label_Slippage_2")
        self.label_Slippage_2.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"border:None;")

        self.horizontalLayout_45.addWidget(self.label_Slippage_2)

        self.Input_Settings_Slippage = QLineEdit(self.frame_80)
        self.Input_Settings_Slippage.setObjectName(u"Input_Settings_Slippage")
        self.Input_Settings_Slippage.setMinimumSize(QSize(0, 30))
        self.Input_Settings_Slippage.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Input_Settings_Slippage.setMaxLength(1000)
        self.Input_Settings_Slippage.setAlignment(Qt.AlignCenter)
        self.Input_Settings_Slippage.setClearButtonEnabled(True)

        self.horizontalLayout_45.addWidget(self.Input_Settings_Slippage)


        self.verticalLayout_32.addWidget(self.frame_80)

        self.frame_102 = QFrame(self.frame_54)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(0, 40))
        self.frame_102.setMaximumSize(QSize(16777215, 40))
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_Slippage_8 = QLabel(self.frame_102)
        self.label_Slippage_8.setObjectName(u"label_Slippage_8")
        self.label_Slippage_8.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"border:None;")

        self.horizontalLayout_63.addWidget(self.label_Slippage_8)

        self.Input_Settings_GAS = QLineEdit(self.frame_102)
        self.Input_Settings_GAS.setObjectName(u"Input_Settings_GAS")
        self.Input_Settings_GAS.setMinimumSize(QSize(0, 30))
        self.Input_Settings_GAS.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Input_Settings_GAS.setMaxLength(1000)
        self.Input_Settings_GAS.setAlignment(Qt.AlignCenter)
        self.Input_Settings_GAS.setClearButtonEnabled(True)

        self.horizontalLayout_63.addWidget(self.Input_Settings_GAS)


        self.verticalLayout_32.addWidget(self.frame_102)

        self.frame_91 = QFrame(self.frame_54)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(0, 40))
        self.frame_91.setMaximumSize(QSize(16777215, 40))
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_Slippage_3 = QLabel(self.frame_91)
        self.label_Slippage_3.setObjectName(u"label_Slippage_3")
        self.label_Slippage_3.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"border:None;")

        self.horizontalLayout_54.addWidget(self.label_Slippage_3)

        self.Input_Settings_OQI = QLineEdit(self.frame_91)
        self.Input_Settings_OQI.setObjectName(u"Input_Settings_OQI")
        self.Input_Settings_OQI.setMinimumSize(QSize(0, 30))
        self.Input_Settings_OQI.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Input_Settings_OQI.setMaxLength(1000)
        self.Input_Settings_OQI.setAlignment(Qt.AlignCenter)
        self.Input_Settings_OQI.setClearButtonEnabled(True)

        self.horizontalLayout_54.addWidget(self.Input_Settings_OQI)


        self.verticalLayout_32.addWidget(self.frame_91)

        self.frame_92 = QFrame(self.frame_54)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(0, 40))
        self.frame_92.setMaximumSize(QSize(16777215, 40))
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_Slippage_4 = QLabel(self.frame_92)
        self.label_Slippage_4.setObjectName(u"label_Slippage_4")
        self.label_Slippage_4.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"border:None;")

        self.horizontalLayout_55.addWidget(self.label_Slippage_4)

        self.Input_Settings_SQI = QLineEdit(self.frame_92)
        self.Input_Settings_SQI.setObjectName(u"Input_Settings_SQI")
        self.Input_Settings_SQI.setMinimumSize(QSize(0, 30))
        self.Input_Settings_SQI.setStyleSheet(u"QLineEdit {\n"
"	font-size: 11px;\n"
"	color:#9ca9b3;\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.Input_Settings_SQI.setMaxLength(1000)
        self.Input_Settings_SQI.setAlignment(Qt.AlignCenter)
        self.Input_Settings_SQI.setClearButtonEnabled(True)

        self.horizontalLayout_55.addWidget(self.Input_Settings_SQI)


        self.verticalLayout_32.addWidget(self.frame_92)

        self.frame_55 = QFrame(self.frame_54)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_55)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_109 = QFrame(self.frame_55)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMinimumSize(QSize(0, 40))
        self.frame_109.setMaximumSize(QSize(16777215, 40))
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.checkBox_WaitTXStatus = QCheckBox(self.frame_109)
        self.checkBox_WaitTXStatus.setObjectName(u"checkBox_WaitTXStatus")
        self.checkBox_WaitTXStatus.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;")

        self.horizontalLayout_68.addWidget(self.checkBox_WaitTXStatus)


        self.verticalLayout_20.addWidget(self.frame_109)

        self.frame_99 = QFrame(self.frame_55)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(0, 40))
        self.frame_99.setMaximumSize(QSize(16777215, 40))
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.checkBox_AutoStart_Orders = QCheckBox(self.frame_99)
        self.checkBox_AutoStart_Orders.setObjectName(u"checkBox_AutoStart_Orders")
        self.checkBox_AutoStart_Orders.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;")

        self.horizontalLayout_60.addWidget(self.checkBox_AutoStart_Orders)

        self.checkBox_AutoStart_Sniper = QCheckBox(self.frame_99)
        self.checkBox_AutoStart_Sniper.setObjectName(u"checkBox_AutoStart_Sniper")
        self.checkBox_AutoStart_Sniper.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;")

        self.horizontalLayout_60.addWidget(self.checkBox_AutoStart_Sniper)


        self.verticalLayout_20.addWidget(self.frame_99)

        self.frame_93 = QFrame(self.frame_55)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_93)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_95 = QFrame(self.frame_93)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_95)

        self.frame_Settings_error = QFrame(self.frame_93)
        self.frame_Settings_error.setObjectName(u"frame_Settings_error")
        self.frame_Settings_error.setStyleSheet(u"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(196, 49, 69) ;\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;")
        self.frame_Settings_error.setFrameShape(QFrame.StyledPanel)
        self.frame_Settings_error.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_Settings_error)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 9, 0)
        self.label_Settings_error = QLabel(self.frame_Settings_error)
        self.label_Settings_error.setObjectName(u"label_Settings_error")
        self.label_Settings_error.setTextFormat(Qt.PlainText)
        self.label_Settings_error.setAlignment(Qt.AlignCenter)
        self.label_Settings_error.setWordWrap(True)

        self.horizontalLayout_56.addWidget(self.label_Settings_error)

        self.label_Settings_success = QLabel(self.frame_Settings_error)
        self.label_Settings_success.setObjectName(u"label_Settings_success")
        self.label_Settings_success.setMaximumSize(QSize(80, 16777215))
        self.label_Settings_success.setStyleSheet(u"color:green;")
        self.label_Settings_success.setTextFormat(Qt.PlainText)
        self.label_Settings_success.setAlignment(Qt.AlignCenter)
        self.label_Settings_success.setWordWrap(True)

        self.horizontalLayout_56.addWidget(self.label_Settings_success)


        self.verticalLayout_12.addWidget(self.frame_Settings_error)


        self.verticalLayout_20.addWidget(self.frame_93)


        self.verticalLayout_32.addWidget(self.frame_55)

        self.frame_81 = QFrame(self.frame_54)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(0, 0))
        self.frame_81.setMaximumSize(QSize(16777215, 40))
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_46.setSpacing(2)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_83 = QFrame(self.frame_81)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(200, 0))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_46.addWidget(self.frame_83)

        self.pushButton_Discard_Settings = QPushButton(self.frame_81)
        self.pushButton_Discard_Settings.setObjectName(u"pushButton_Discard_Settings")
        self.pushButton_Discard_Settings.setMinimumSize(QSize(0, 30))
        self.pushButton_Discard_Settings.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_46.addWidget(self.pushButton_Discard_Settings)

        self.pushButton_Save_Settings = QPushButton(self.frame_81)
        self.pushButton_Save_Settings.setObjectName(u"pushButton_Save_Settings")
        self.pushButton_Save_Settings.setMinimumSize(QSize(0, 30))
        self.pushButton_Save_Settings.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(220, 161, 1);\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 3px solid rgb(33, 37, 43);\n"
"\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_46.addWidget(self.pushButton_Save_Settings)


        self.verticalLayout_32.addWidget(self.frame_81)


        self.verticalLayout_34.addWidget(self.frame_54)

        self.stackedWidget_2.addWidget(self.SettingsOverview)

        self.verticalLayout_15.addWidget(self.stackedWidget_2)


        self.verticalLayout_2.addWidget(self.frame_23)


        self.horizontalLayout_23.addWidget(self.frame_7)


        self.horizontalLayout_22.addWidget(self.frame_17)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.stackedWidgetPage1)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.frame_top_btns = QFrame(self.main_frame)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200);")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setMaximumSize(QSize(400, 16777215))
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMinimumSize(QSize(32, 32))
        self.frame_icon_top_bar.setMaximumSize(QSize(34, 34))
        self.frame_icon_top_bar.setBaseSize(QSize(32, 32))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/Fontawsome/icons/fontawsome/TIGS-32x32.png) ;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_12 = QLabel(self.frame_label_top_btns)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background: transparent;")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"color:#dca101;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)

        self.label_12.raise_()
        self.label_title_bar_top.raise_()
        self.frame_icon_top_bar.raise_()

        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.gridLayout_2.addWidget(self.frame_top_btns, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.main_frame)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_16.setCurrentIndex(0)
        self.stackedWidget_17.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_credits.setText("")
        self.label_version.setText(QCoreApplication.translate("Dialog", u"v0.0.11a-beta", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Token Address:", None))
        self.token_address.setText("")
        self.token_address.setPlaceholderText(QCoreApplication.translate("Dialog", u"0x34faa80fec0233e045ed4737cc152a71e490e2e3", None))
        self.label_10.setText("")
        self.pushButton_AddtoList.setText(QCoreApplication.translate("Dialog", u"Add ", None))
        self.Button_Market.setText(QCoreApplication.translate("Dialog", u"Market", None))
        self.Button_Limit.setText(QCoreApplication.translate("Dialog", u"Limit", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"CandleTime:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"TimeFrame:", None))
        self.pushButton_Chart_1m.setText(QCoreApplication.translate("Dialog", u"1M", None))
        self.pushButton_Chart_5m.setText(QCoreApplication.translate("Dialog", u"5M", None))
        self.pushButton_Chart_10m.setText(QCoreApplication.translate("Dialog", u"10M", None))
        self.pushButton_Chart_30m.setText(QCoreApplication.translate("Dialog", u"30M", None))
        self.pushButton_Chart_1h.setText(QCoreApplication.translate("Dialog", u"1H", None))
        self.pushButton_Chart_1d.setText(QCoreApplication.translate("Dialog", u"1D", None))
        self.pushButton_ChartTime_1h.setText(QCoreApplication.translate("Dialog", u"1H", None))
        self.pushButton_ChartTime_1d.setText(QCoreApplication.translate("Dialog", u"1D", None))
        self.pushButton_ChartTime_1w.setText(QCoreApplication.translate("Dialog", u"1W", None))
        self.pushButton_ChartTime_1m.setText(QCoreApplication.translate("Dialog", u"1M", None))
        self.pushButton_ChartTime_1y.setText(QCoreApplication.translate("Dialog", u"1Y", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Chart Helpers", None))
        self.ButtonChartHelper_Volume.setText(QCoreApplication.translate("Dialog", u"Volume", None))
        self.ButtonchartHelper_MA20.setText(QCoreApplication.translate("Dialog", u"MA20", None))
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("Dialog", u" Name:", None))
        self.TokenName.setText(QCoreApplication.translate("Dialog", u"Loading...", None))
#if QT_CONFIG(whatsthis)
        self.label_7.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_7.setText(QCoreApplication.translate("Dialog", u" Price:", None))
        self.TokenPrice.setText(QCoreApplication.translate("Dialog", u"Loading...", None))
        self.TokenPriceChange.setText(QCoreApplication.translate("Dialog", u"Loading...", None))
        self.chart_loading.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Error:", None))
        self.label_ErrorMessage.setText(QCoreApplication.translate("Dialog", u"Successfully", None))
        self.pushButton_error_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.label_marketType.setText(QCoreApplication.translate("Dialog", u"MARKET Transaction", None))
        self.Confirm_OrderType.setText(QCoreApplication.translate("Dialog", u"BUY/SELL", None))
        self.Confirm_Amount_In.setText(QCoreApplication.translate("Dialog", u"AMOUNT_INPUT", None))
        self.Confirm_Symbol_In.setText(QCoreApplication.translate("Dialog", u"Sym", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"FOR min", None))
        self.Confirm_Amount_Out.setText(QCoreApplication.translate("Dialog", u"AMOUNT_INPUT", None))
        self.Confirm_Symbol_Out.setText(QCoreApplication.translate("Dialog", u"Sym", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Estimate Tx Fee:", None))
        self.Confirm_TX_FEE_ETH.setText(QCoreApplication.translate("Dialog", u"TX_FEEBNB", None))
        self.pushButton_Cancel_Confirm.setText(QCoreApplication.translate("Dialog", u"Reject", None))
        self.pushButton_Submit_Confirm.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"APPROVE", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Approve MAX", None))
        self.Approve_Symbol.setText(QCoreApplication.translate("Dialog", u"SYM", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"To spend on", None))
        self.label_tb_usd_2.setText(QCoreApplication.translate("Dialog", u"Trading-Tigers Swapper", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Estimate Tx Fee:", None))
        self.Approve_TX_FEE_ETH.setText(QCoreApplication.translate("Dialog", u"TX_FEEBNB", None))
        self.pushButton_Reject_Approve.setText(QCoreApplication.translate("Dialog", u"Reject", None))
        self.pushButton_Submit_Approve.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.label_45.setText(QCoreApplication.translate("Dialog", u"Transaction Status", None))
        self.Transaction_Succesfully.setText(QCoreApplication.translate("Dialog", u"Transaction Sucessfull!", None))
        self.Transaction_Fail.setText(QCoreApplication.translate("Dialog", u"Transaction Fail!", None))
        self.Input_TX_HEX.setText("")
        self.Input_TX_HEX.setPlaceholderText(QCoreApplication.translate("Dialog", u"0x34faa80fec0233e045ed4737cc152a71e490e2e3", None))
        self.pushButton_Status_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.label_46.setText(QCoreApplication.translate("Dialog", u"Set LimitOrder", None))
        self.Order_OrderType.setText(QCoreApplication.translate("Dialog", u"BUY/SELL", None))
        self.Order_Amount.setText(QCoreApplication.translate("Dialog", u"AMOUNT_INPUT", None))
        self.Order_Symbol_In.setText(QCoreApplication.translate("Dialog", u"Sym", None))
        self.label_47.setText(QCoreApplication.translate("Dialog", u"at", None))
        self.Order_Price.setText(QCoreApplication.translate("Dialog", u"Price", None))
        self.Confirm_Orderway.setText(QCoreApplication.translate("Dialog", u"BNB -> BUSD", None))
        self.pushButton_Cancel_Order.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButton_Submit_Order.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Market", None))
        self.label_41.setText(QCoreApplication.translate("Dialog", u"BUY", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Token Tax:", None))
        self.label_token_BuyTax.setText(QCoreApplication.translate("Dialog", u"%", None))
        self.TokenName_MB.setText(QCoreApplication.translate("Dialog", u"Loading...", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"WITH", None))
        self.Button_Base_BNB_MB.setText(QCoreApplication.translate("Dialog", u"BNB", None))
        self.Button_Base_BUSD_MB.setText(QCoreApplication.translate("Dialog", u"BUSD", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"PAY", None))
        self.Input_MB.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Input_MB.setPlaceholderText(QCoreApplication.translate("Dialog", u"0", None))
        self.Input_MB_tokenSymbol.setText(QCoreApplication.translate("Dialog", u"sym", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"GET", None))
        self.Output_MB.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Output_MB.setPlaceholderText(QCoreApplication.translate("Dialog", u"0", None))
        self.Output_MB_tokenSymbol.setText(QCoreApplication.translate("Dialog", u"sym", None))
        self.ButtonExecute_MB.setText(QCoreApplication.translate("Dialog", u"Execute Buy", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"SELL", None))
        self.label_34.setText(QCoreApplication.translate("Dialog", u"Token Tax:", None))
        self.label_token_SellTax.setText(QCoreApplication.translate("Dialog", u"%", None))
        self.TokenName_MS.setText(QCoreApplication.translate("Dialog", u"Loading...", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"TO", None))
        self.Button_Base_BNB_MS.setText(QCoreApplication.translate("Dialog", u"BNB", None))
        self.Button_Base_BUSD_MS.setText(QCoreApplication.translate("Dialog", u"BUSD", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"PAY", None))
        self.Input_MS.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Input_MS.setPlaceholderText(QCoreApplication.translate("Dialog", u"0", None))
        self.Input_MS_tokenSymbol.setText(QCoreApplication.translate("Dialog", u"sym", None))
        self.label_33.setText(QCoreApplication.translate("Dialog", u"GET", None))
        self.Output_MS.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Output_MS.setPlaceholderText(QCoreApplication.translate("Dialog", u"0", None))
        self.Output_MS_tokenSymbol.setText(QCoreApplication.translate("Dialog", u"sym", None))
        self.ButtonExecute_MS.setText(QCoreApplication.translate("Dialog", u"Execute Sell", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Sniper", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"BUY", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"SELL", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Limit Order", None))
        self.label_44.setText(QCoreApplication.translate("Dialog", u"BUY", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Token Tax:", None))
        self.label_token_BuyTax_2.setText(QCoreApplication.translate("Dialog", u"%", None))
        self.TokenName_LB.setText(QCoreApplication.translate("Dialog", u"Loading...", None))
        self.label_35.setText(QCoreApplication.translate("Dialog", u"WITH", None))
        self.Button_Base_BNB_LB.setText(QCoreApplication.translate("Dialog", u"BNB", None))
        self.Button_Base_BUSD_LB.setText(QCoreApplication.translate("Dialog", u"BUSD", None))
        self.label_36.setText(QCoreApplication.translate("Dialog", u"PAY", None))
        self.Input_LB.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Input_LB.setPlaceholderText(QCoreApplication.translate("Dialog", u"0", None))
        self.Input_LB_tokenSymbol.setText(QCoreApplication.translate("Dialog", u"sym", None))
        self.label_37.setText(QCoreApplication.translate("Dialog", u"at PRICE", None))
        self.Price_LB.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Price_LB.setPlaceholderText(QCoreApplication.translate("Dialog", u"0", None))
        self.Output_LB_tokenSymbol.setText(QCoreApplication.translate("Dialog", u"sym", None))
        self.ButtonPlace_LB.setText(QCoreApplication.translate("Dialog", u"Place Buy Order", None))
        self.label_42.setText(QCoreApplication.translate("Dialog", u"SELL", None))
        self.label_43.setText(QCoreApplication.translate("Dialog", u"Token Tax:", None))
        self.label_token_SellTax_2.setText(QCoreApplication.translate("Dialog", u"%", None))
        self.TokenName_LS.setText(QCoreApplication.translate("Dialog", u"Loading...", None))
        self.label_38.setText(QCoreApplication.translate("Dialog", u"TO", None))
        self.Button_Base_BNB_LS.setText(QCoreApplication.translate("Dialog", u"BNB", None))
        self.Button_Base_BUSD_LS.setText(QCoreApplication.translate("Dialog", u"BUSD", None))
        self.label_39.setText(QCoreApplication.translate("Dialog", u"PAY", None))
        self.Input_LS.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Input_LS.setPlaceholderText(QCoreApplication.translate("Dialog", u"0", None))
        self.Input_LS_tokenSymbol.setText(QCoreApplication.translate("Dialog", u"sym", None))
        self.label_40.setText(QCoreApplication.translate("Dialog", u"at PRICE", None))
        self.Price_LS.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Price_LS.setPlaceholderText(QCoreApplication.translate("Dialog", u"0", None))
        self.Output_LS_tokenSymbol.setText(QCoreApplication.translate("Dialog", u"sym", None))
        self.ButtonPlace_LS.setText(QCoreApplication.translate("Dialog", u"Place Sell Order", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"MENU", None))
        self.pushButton_Wallet.setText(QCoreApplication.translate("Dialog", u"Wallet", None))
        self.pushButton_Orders.setText(QCoreApplication.translate("Dialog", u"Orders", None))
        self.pushButton_Settings.setText(QCoreApplication.translate("Dialog", u"Settings", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Wallet Balance", None))
        self.Balance_all.setText(QCoreApplication.translate("Dialog", u"$ 0.0", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Open Orders", None))
#if QT_CONFIG(tooltip)
        self.label_Slippage_7.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_Slippage_7.setText(QCoreApplication.translate("Dialog", u"Status:", None))
        self.label_Status_LIMITORDERS.setText(QCoreApplication.translate("Dialog", u"Online/Offline", None))
        self.pushButton_STOP_LimitOrders.setText(QCoreApplication.translate("Dialog", u"STOP", None))
        self.pushButton_START_LimitOrders.setText(QCoreApplication.translate("Dialog", u"START", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Settings", None))
        self.label_Slippage.setText(QCoreApplication.translate("Dialog", u"Address", None))
        self.Input_Settings_Address.setText(QCoreApplication.translate("Dialog", u"address", None))
        self.Input_Settings_Address.setPlaceholderText(QCoreApplication.translate("Dialog", u"Wallet Address", None))
        self.label_Slippage_5.setText(QCoreApplication.translate("Dialog", u"Private Key", None))
        self.Input_Settings_PrivateKey.setText("")
        self.Input_Settings_PrivateKey.setPlaceholderText(QCoreApplication.translate("Dialog", u"blank if you want to use read only", None))
        self.label_Slippage_6.setText(QCoreApplication.translate("Dialog", u"PROVIDER", None))
        self.Input_Settings_provider.setText("")
        self.Input_Settings_provider.setPlaceholderText(QCoreApplication.translate("Dialog", u"https://... wss://...", None))
        self.label_Slippage_2.setText(QCoreApplication.translate("Dialog", u"Max Slippage", None))
        self.Input_Settings_Slippage.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.Input_Settings_Slippage.setPlaceholderText(QCoreApplication.translate("Dialog", u"0.01", None))
        self.label_Slippage_8.setText(QCoreApplication.translate("Dialog", u"GAS (GWEI) ", None))
        self.Input_Settings_GAS.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.Input_Settings_GAS.setPlaceholderText(QCoreApplication.translate("Dialog", u"0.01", None))
#if QT_CONFIG(tooltip)
        self.label_Slippage_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_Slippage_3.setText(QCoreApplication.translate("Dialog", u"Order review interval", None))
        self.Input_Settings_OQI.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.Input_Settings_OQI.setPlaceholderText(QCoreApplication.translate("Dialog", u"0.01", None))
#if QT_CONFIG(tooltip)
        self.label_Slippage_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_Slippage_4.setText(QCoreApplication.translate("Dialog", u"Sniper Check interval", None))
        self.Input_Settings_SQI.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.Input_Settings_SQI.setPlaceholderText(QCoreApplication.translate("Dialog", u"0.01", None))
        self.checkBox_WaitTXStatus.setText(QCoreApplication.translate("Dialog", u"Wait for transaction status", None))
        self.checkBox_AutoStart_Orders.setText(QCoreApplication.translate("Dialog", u"AutoStart Limit Orders", None))
        self.checkBox_AutoStart_Sniper.setText(QCoreApplication.translate("Dialog", u"AutoStart Sniper Orders", None))
        self.label_Settings_error.setText("")
        self.label_Settings_success.setText(QCoreApplication.translate("Dialog", u"Successfully", None))
        self.pushButton_Discard_Settings.setText(QCoreApplication.translate("Dialog", u"Discard", None))
        self.pushButton_Save_Settings.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.label_12.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("Dialog", u"Tading-Tigers.com Toolkit & Bot", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("Dialog", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("Dialog", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
    # retranslateUi

