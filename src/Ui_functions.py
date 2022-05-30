from imports import *


class UI_Functions():
        
    def deleteOrderButton(self, gui, id):
        LimitOrders_Settings().deleteOrder(str(id))
        gui.initOpenOrders()

        
 
    def changeCurrentToken(self, ui, Token_Address):
        ui.token_address.setText(str(Token_Address))       


    def createScrollAreaWidgetContents(self):
        scrollAreaWidgetContents = QWidget()
        scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        scrollAreaWidgetContents.setGeometry(QRect(0, 0, 358, 504))
        scrollAreaWidgetContents.setLayoutDirection(Qt.RightToLeft)
        return scrollAreaWidgetContents


    def createWalletTokenContainer(self, ui, Token_Address, Symbol, Name, Price ,Balance, Balance_USD):
        frame_token_Stats = QFrame()
        frame_token_Stats.setObjectName(u"frame_token_Stats")
        frame_token_Stats.setMinimumSize(QSize(0, 35))
        frame_token_Stats.setMaximumSize(QSize(16777215, 50))
        frame_token_Stats.setStyleSheet(u"QFrame {\n"
        "\n"
        "	border: 2px solid  rgba(27, 29, 35, 200);\n"
        "}\n"
        "\n"
        "QFrame:hover {\n"
        "	\n"
        "}")
        frame_token_Stats.setFrameShape(QFrame.StyledPanel)
        frame_token_Stats.setFrameShadow(QFrame.Raised)
        gridLayout = QGridLayout(frame_token_Stats)
        gridLayout.setSpacing(0)
        gridLayout.setObjectName(u"gridLayout")
        gridLayout.setContentsMargins(0, 0, 0, 0)
        pushButton_LabelTokenName = QPushButton(frame_token_Stats)
        pushButton_LabelTokenName.setObjectName(u"pushButton_LabelTokenName")
        pushButton_LabelTokenName.setMinimumSize(QSize(0, 10))
        pushButton_LabelTokenName.setMaximumSize(QSize(16777215, 22))
        pushButton_LabelTokenName.setStyleSheet(u"QPushButton {\n"
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

        gridLayout.addWidget(pushButton_LabelTokenName, 1, 2, 1, 1)

        label_tb_usd = QLabel(frame_token_Stats)
        label_tb_usd.setObjectName(u"label_tb_usd")
        label_tb_usd.setStyleSheet(u"color:#dca101;\n"
        "font-weight: bold;\n"
        "background:transparent;\n"
        "font-size: 9pt;\n"
        "border:None;\n"
        "border-left: 2px solid  rgba(27, 29, 35, 200);")
        label_tb_usd.setFrameShape(QFrame.NoFrame)
        label_tb_usd.setAlignment(Qt.AlignCenter)

        gridLayout.addWidget(label_tb_usd, 1, 1, 1, 1)

        label_token_balance = QLabel(frame_token_Stats)
        label_token_balance.setObjectName(u"label_token_balance")
        label_token_balance.setStyleSheet(u"color:#9ca9b3;\n"
        "font-weight: bold;\n"
        "background:transparent;\n"
        "border:None;\n"
        "border-left:2px solid  rgba(27, 29, 35, 200);\n"
        "font-size: 10pt;\n"
        "")
        label_token_balance.setFrameShape(QFrame.NoFrame)
        label_token_balance.setAlignment(Qt.AlignCenter)

        gridLayout.addWidget(label_token_balance, 0, 1, 1, 1)

        frame_Symbol_price = QFrame(frame_token_Stats)
        frame_Symbol_price.setObjectName(u"frame_Symbol_price")
        frame_Symbol_price.setStyleSheet(u"border:None;\n"
        "border-buttom:;")
        frame_Symbol_price.setFrameShape(QFrame.StyledPanel)
        frame_Symbol_price.setFrameShadow(QFrame.Raised)
        horizontalLayout_45 = QHBoxLayout(frame_Symbol_price)
        horizontalLayout_45.setSpacing(2)
        horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        label_token_usd_price = QLabel(frame_Symbol_price)
        label_token_usd_price.setObjectName(u"label_token_usd_price")
        label_token_usd_price.setStyleSheet(u"color:#dca101;\n"
        "font-weight: bold;\n"
        "background:transparent;\n"
        "font-size: 9pt;")
        label_token_usd_price.setAlignment(Qt.AlignCenter)

        horizontalLayout_45.addWidget(label_token_usd_price)

        label_token_symbol = QLabel(frame_Symbol_price)
        label_token_symbol.setObjectName(u"label_token_symbol")
        label_token_symbol.setStyleSheet(u"color:#9ca9b3;\n"
        "font-weight: bold;\n"
        "background:transparent;\n"
        "font-size: 10pt;")
        label_token_symbol.setAlignment(Qt.AlignCenter)
        horizontalLayout_45.addWidget(label_token_symbol)
        gridLayout.addWidget(frame_Symbol_price, 0, 2, 1, 1)
        label_token_symbol.setText(Symbol)
        label_token_usd_price.setText("$ " +Math_UI_Functions().FloatToCleanSting(Price))
        pushButton_LabelTokenName.setText(Name)
        pushButton_LabelTokenName.clicked.connect(lambda: self.changeCurrentToken(ui, Token_Address))
        label_token_balance.setText( Math_UI_Functions().FloatToCleanSting(Balance))
        label_tb_usd.setText("$ " + Math_UI_Functions().FloatToCleanSting(Balance_USD) )

        return frame_token_Stats


        
    def createOrderContainer(self, gui, Id, Symbol_Input, Symbol_Output,Side, Price, Amount):
        frame_Orders = QFrame()
        frame_Orders.setObjectName(u"frame_Orders")
        frame_Orders.setMinimumSize(QSize(0, 35))
        frame_Orders.setMaximumSize(QSize(16777215, 50))
        frame_Orders.setStyleSheet(u"QFrame {\n"
"	border: 2px solid  rgba(27, 29, 35, 200);\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	\n"
"}")
        frame_Orders.setFrameShape(QFrame.StyledPanel)
        frame_Orders.setFrameShadow(QFrame.Raised)
        verticalLayout = QVBoxLayout(frame_Orders)
        verticalLayout.setSpacing(0)
        verticalLayout.setObjectName(u"verticalLayout")
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        frame_Symbol_price = QFrame(frame_Orders)
        frame_Symbol_price.setObjectName(u"frame_Symbol_price")
        frame_Symbol_price.setStyleSheet(u"border:None;\n"
"")
        frame_Symbol_price.setFrameShape(QFrame.StyledPanel)
        frame_Symbol_price.setFrameShadow(QFrame.Raised)
        horizontalLayout_45 = QHBoxLayout(frame_Symbol_price)
        horizontalLayout_45.setSpacing(2)
        horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        label_token_usd_price = QLabel(frame_Symbol_price)
        label_token_usd_price.setObjectName(u"label_token_usd_price")
        label_token_usd_price.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;")
        label_token_usd_price.setAlignment(Qt.AlignCenter)

        horizontalLayout_45.addWidget(label_token_usd_price)

        label_at = QLabel(frame_Symbol_price)
        label_at.setObjectName(u"label_at")
        label_at.setMaximumSize(QSize(30, 16777215))
        label_at.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        label_at.setAlignment(Qt.AlignCenter)

        horizontalLayout_45.addWidget(label_at)

        label_Order_Symbol = QLabel(frame_Symbol_price)
        label_Order_Symbol.setObjectName(u"label_Order_Symbol")
        label_Order_Symbol.setLayoutDirection(Qt.RightToLeft)
        label_Order_Symbol.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"border:None;\n"
"")
        label_Order_Symbol.setFrameShape(QFrame.NoFrame)
        label_Order_Symbol.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        horizontalLayout_45.addWidget(label_Order_Symbol)

        label_Order_Amount = QLabel(frame_Symbol_price)
        label_Order_Amount.setObjectName(u"label_Order_Amount")
        label_Order_Amount.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"border:None;\n"
"")
        label_Order_Amount.setFrameShape(QFrame.NoFrame)
        label_Order_Amount.setAlignment(Qt.AlignCenter)

        horizontalLayout_45.addWidget(label_Order_Amount)

        label_Order_Side = QLabel(frame_Symbol_price)
        label_Order_Side.setObjectName(u"label_Order_Side")
        label_Order_Side.setStyleSheet(u"color:#9ca9b3;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 10pt;")
        label_Order_Side.setAlignment(Qt.AlignCenter)

        horizontalLayout_45.addWidget(label_Order_Side)


        verticalLayout.addWidget(frame_Symbol_price)

        frame = QFrame(frame_Orders)
        frame.setObjectName(u"frame")
        frame.setStyleSheet(u"border:None;")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        horizontalLayout = QHBoxLayout(frame)
        horizontalLayout.setSpacing(3)
        horizontalLayout.setObjectName(u"horizontalLayout")
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        pushButton_DeleteOrder = QPushButton(frame)
        pushButton_DeleteOrder.setObjectName(u"pushButton_DeleteOrder")
        pushButton_DeleteOrder.setMinimumSize(QSize(0, 10))
        pushButton_DeleteOrder.setMaximumSize(QSize(100, 22))
        pushButton_DeleteOrder.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 11px;\n"
"	color: rgb(196, 49, 69);\n"
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

        horizontalLayout.addWidget(pushButton_DeleteOrder)

        label_Order_From_TO = QLabel(frame)
        label_Order_From_TO.setObjectName(u"label_Order_From_TO")
        label_Order_From_TO.setStyleSheet(u"color:#dca101;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"font-size: 9pt;\n"
"border:None;\n"
"")
        label_Order_From_TO.setFrameShape(QFrame.NoFrame)
        label_Order_From_TO.setAlignment(Qt.AlignCenter)

        horizontalLayout.addWidget(label_Order_From_TO)


        verticalLayout.addWidget(frame)




        pushButton_DeleteOrder.setText(str("DELETE ORDER"))

        pushButton_DeleteOrder.clicked.connect(lambda: self.deleteOrderButton(gui, Id))
        label_token_usd_price.setText("$ " + str(Price))
        label_at.setText(u"at")
        label_Order_Amount.setText(str(Amount))
        label_Order_Symbol.setText(str(Symbol_Input))
        label_Order_From_TO.setText(str(Symbol_Input + " -> " + Symbol_Output))
        if Side == "BUY":
                label_Order_Side.setStyleSheet(Ui_Styles().BUY_label)
                
        if Side == "SELL":
                label_Order_Side.setStyleSheet(Ui_Styles().SELL_label)
                
        label_Order_Side.setText(str(Side))


        return frame_Orders