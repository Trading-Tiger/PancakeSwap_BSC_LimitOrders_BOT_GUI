from imports import *



class WorkerSignals(QObject):
    result = pyqtSignal(bool, tuple)


class AWorker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(AWorker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            data = self.fn(*self.args, **self.kwargs)
            self.signals.result.emit(True, tuple(data))
        except:
            self.signals.result.emit(False, tuple(data))



class AExecutor(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(AExecutor, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)



class functions_Chart():
    def __init__(self):
        self.address = Web3.toChecksumAddress("0x34faa80fec0233e045ed4737cc152a71e490e2e3") #TIGS

    def reinit(self, address):
        self.address = Web3.toChecksumAddress(address)

    def currentUnixTime(self):
        date = datetime.utcnow()
        utc_time = calendar.timegm(date.utctimetuple())
        return utc_time

    def doRequest(self, candleTime, candleHistory):
        currentUnixTime = int(self.currentUnixTime())
        unix = candleHistory * 60 * 60
        realCandelTime = int(currentUnixTime - unix)
        reqJ = requests.get(f'https://api.trading-tigers.com/PancakeSwap/Chart/{self.address}/{candleTime}&from={currentUnixTime}&to={realCandelTime}').text
        return json.loads(reqJ)['data']


class MainWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        fplt.foreground = '#dca101'
        fplt.background = '#272c36'
        self.ui = Ui_Dialog()
        self.chart_functions = functions_Chart()
        self.GS = Global_Settings()
        self.US = User_Settings()
        self.OS = LimitOrders_Settings()
        self.limitorders = LimitOrders_Algo()
        self.web3 = Web3_UI_Functions()
        self.math = Math_UI_Functions()
        self.uif = UI_Functions()
        self.ui.setupUi(self)

        self.threadpool = QThreadPool.globalInstance()
        self.setWindowTitle('Trading Tigers Toolkit')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())
        #BUTTONS & CHANGED QTEXTEDIT
        self.ui.token_address.textChanged.connect(lambda: self.addressChange())
        self.ui.ButtonchartHelper_MA20.clicked.connect(lambda: self.changeIndicatorSettings("MA20"))
        self.ui.ButtonChartHelper_Volume.clicked.connect(lambda: self.changeIndicatorSettings("VOLUME"))
        self.ui.pushButton_error_OK.clicked.connect(lambda: self.ui.stackedWidget_16.setCurrentWidget(self.ui.Chart_Loaded))
        self.ui.pushButton_Status_OK.clicked.connect(lambda: self.ui.stackedWidget_16.setCurrentWidget(self.ui.Chart_Loaded))
        self.ui.pushButton_Status_OK.clicked.connect(lambda: self.ui.stackedWidget_16.setCurrentWidget(self.ui.Chart_Loaded))
        self.ui.pushButton_Cancel_Confirm.clicked.connect(lambda: self.ui.stackedWidget_16.setCurrentWidget(self.ui.Chart_Loaded))
        self.ui.pushButton_Cancel_Order.clicked.connect(lambda: self.ui.stackedWidget_16.setCurrentWidget(self.ui.Chart_Loaded))
        self.ui.pushButton_Reject_Approve.clicked.connect(lambda: self.ui.stackedWidget_16.setCurrentWidget(self.ui.Chart_Loaded))



        self.linkStartStopButtons()
        self.ui.pushButton_STOP_LimitOrders.clicked.connect(lambda: self.ButtonStopOrderALGO())
        self.ui.pushButton_START_LimitOrders.clicked.connect(lambda: self.ButtonStartOrderALGO())


        self.initButtonValidators()
        self.initButtonsChart()
        self.initButtonsBToken()
        self.initButtonsOrderType()
        self.initButtonsMenu()
        self.initChart()
        self.initTradeInputs()


        self.ui.frame_Settings_error.hide()

        self.ui.Input_Settings_PrivateKey.setEchoMode(QLineEdit.Password)

        update_Price = QtCore.QTimer(self, interval=10000, timeout=self.update_Price)
        update_Price.start()

        update_wallet_balance = QtCore.QTimer(self, interval=10000, timeout=self.update_wallet_balance)
        update_wallet_balance.start()

        AllowanceChecker = QtCore.QTimer(self, interval=5000, timeout=self.checkTokenAllowances)
        AllowanceChecker.start()

        update_OpenOrders = QtCore.QTimer(self, interval=10000, timeout=self.initOpenOrders)
        update_OpenOrders.start()

        self.LimitOrderAlgo = QtCore.QTimer(self, interval=int(self.US.OQI * 1000), timeout=self.RunLimitOrderAlgorithumus)

        if self.US.AUTOSTART_ORDERS:
            if self.GS.O_ONLINE:
                self.LimitOrderAlgo.start()


        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.main_frame.setGraphicsEffect(self.shadow)

        ##############
        self.selectBaseToken()
        self.selectIndicatorsButtons()
        self.selectCandleTime()
        self.selectCandleHistoryTime()
        self.selectOrderType()
        self.selectMenuButton()

        self.update_wallet_balance()
        self.ui.token_address.setText(str(Web3.toChecksumAddress("0x34faa80fec0233e045ed4737cc152a71e490e2e3")))



        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.frame_top_btns.mouseMoveEvent = moveWindow

        self.window().axs = [self.ax]
        self.show()

    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
   
    def addressChange(self):
        token_address = self.ui.token_address.text()
        if Web3.isAddress(token_address) == True:
            if self.web3.checkIsTokenContract(Web3.toChecksumAddress(token_address)):
                self.token_address = Web3.toChecksumAddress(token_address)
                self.ui.token_address.setText(self.token_address)
                self.loadTokenAddress()

    def RunLimitOrderAlgorithumus(self):
        self.limitorders.start()
            
    def linkStartStopButtons(self):
        self.ui.pushButton_STOP_LimitOrders.clicked.connect(lambda: self.ButtonStopOrderALGO())
        self.ui.pushButton_START_LimitOrders.clicked.connect(lambda: self.ButtonStartOrderALGO())
        self.initOrderAlgoButtons(True)


    def initOrderAlgoButtons(self, firstStart):
        if firstStart:
            if self.US.AUTOSTART_ORDERS:
                if self.GS.O_ONLINE:
                    self.ui.label_Status_LIMITORDERS.setText("ONLINE")
                    self.ui.label_Status_LIMITORDERS.setStyleSheet(Ui_Styles().BUY_label)
                else:
                    self.ui.label_Status_LIMITORDERS.setText("OFFLINE")
                    self.ui.label_Status_LIMITORDERS.setStyleSheet(Ui_Styles().SELL_label)
            else:
                self.ui.label_Status_LIMITORDERS.setText("OFFLINE")
                self.ui.label_Status_LIMITORDERS.setStyleSheet(Ui_Styles().SELL_label)
        else:
            if self.GS.O_ONLINE:
                self.ui.label_Status_LIMITORDERS.setText("ONLINE")
                self.ui.label_Status_LIMITORDERS.setStyleSheet(Ui_Styles().BUY_label)
            else:
                self.ui.label_Status_LIMITORDERS.setText("OFFLINE")
                self.ui.label_Status_LIMITORDERS.setStyleSheet(Ui_Styles().SELL_label)


    def ButtonStopOrderALGO(self):
        self.GS.changeGlobalSetting("ORDERS_ONLINE", False)
        self.initOrderAlgoButtons(False)
        self.LimitOrderAlgo.stop()

    def ButtonStartOrderALGO(self):
        self.GS.changeGlobalSetting("ORDERS_ONLINE", True)
        self.initOrderAlgoButtons(False)
        self.LimitOrderAlgo.start()


    def loadTokenAddress(self):
        self.chart_functions.reinit(self.token_address)
        self.loadAddButton()
        self.update_TokenInfos()
        self.update_Price()
        self.update_chart_dex()
        self.update_TokenTax()
        self.update_TokenAllowance()
        self.resetInputs()

    def update_TokenAllowance(self):
        self.threadpool.start(AExecutor(self.checkTokenAllowances))

    def checkTokenAllowances(self):
        try:
            if self.GS.B_TOKEN == "BUSD":
                ALLOWANCE = int(self.web3.checkAlloanceSwapper(self.web3.BUSD, self.US.ADDRESS)) / 10**18
                if float(ALLOWANCE) <= float(self.ui.Input_LB.text()) or float(ALLOWANCE) < float(self.ui.Input_MB.text()):
                    self.changeApproveButtonsBUY(True)
                else:
                    self.changeApproveButtonsBUY(False)
            else:
                self.changeApproveButtonsBUY(False)
            if self.token_address != self.web3.WBNB:
                ALLOWANCE = int(self.web3.checkAlloanceSwapper(self.token_address, self.US.ADDRESS)) / 10**self.jsonTokenData['tokenDecimals']
                if float(ALLOWANCE) <= float(self.ui.Input_LS.text()) or float(ALLOWANCE) < float(self.ui.Input_MS.text()):
                    self.changeApproveButtonsSELL(True)
                else:
                    self.changeApproveButtonsSELL(False)
            else:
                self.changeApproveButtonsSELL(False)

        except:
            pass

    
    def changeApproveButtonsBUY(self, bool):
        try:
            self.ui.ButtonExecute_MB.clicked.disconnect()
        except:
            pass
        try:
            self.ui.ButtonPlace_LB.clicked.disconnect()
        except:
            pass

        if bool:
            self.ui.ButtonExecute_MB.clicked.connect(lambda: self.ApproveToken(self.web3.BUSD))
            self.ui.ButtonExecute_MB.setText("APPROVE")
            self.ui.ButtonPlace_LB.clicked.connect(lambda: self.ApproveToken(self.web3.BUSD))
            self.ui.ButtonPlace_LB.setText("APPROVE")
        else:
            self.ui.ButtonExecute_MB.clicked.connect(lambda: self.ConfirmPageMarket("MARKET","BUY"))
            self.ui.ButtonExecute_MB.setText("EXECUTE BUY")
            self.ui.ButtonPlace_LB.clicked.connect(lambda: self.ConfirmPageMarket("LIMIT","BUY"))
            self.ui.ButtonPlace_LB.setText("PLACE ORDER")


    def changeApproveButtonsSELL(self, bool):
        try:
            self.ui.ButtonExecute_MS.clicked.disconnect()
        except:
            pass
        try:
            self.ui.ButtonPlace_LS.clicked.disconnect()
        except:
            pass

        if bool:
            self.ui.ButtonExecute_MS.clicked.connect(lambda: self.ApproveToken(self.token_address))
            self.ui.ButtonExecute_MS.setText("APPROVE")
            self.ui.ButtonPlace_LS.clicked.connect(lambda: self.ApproveToken(self.token_address))
            self.ui.ButtonPlace_LS.setText("APPROVE")
        else:
            self.ui.ButtonExecute_MS.clicked.connect(lambda: self.ConfirmPageMarket("MARKET", "SELL"))
            self.ui.ButtonExecute_MS.setText("EXECUTE SELL")
            self.ui.ButtonPlace_LS.clicked.connect(lambda: self.ConfirmPageMarket("LIMIT","SELL"))
            self.ui.ButtonPlace_LS.setText("PLACE ORDER")


    def ConfirmPageMarket(self, type, side):
        status = True
        if str(self.jsonTokenData["tokenSymbol"]) == str(self.GS.B_TOKEN):
            status = False
            self.ui.label_ErrorMessage.setText("FROM and TO TOKEN IS SAME, Wrapped TOKENS not Supported!")
            self.ui.stackedWidget_16.setCurrentWidget(self.ui.Error_Page)

        if status:
            if type == "MARKET":
                if float(self.ui.Input_MB.text()) != 0 or float(self.ui.Input_MS.text()) !=0:
                    if side == "SELL":

                        self.ui.Confirm_OrderType.setText(type + " " + side)
                        self.ui.Confirm_OrderType.setStyleSheet(Ui_Styles().SELL_label)
                        self.ui.Confirm_Symbol_In.setText(self.jsonTokenData["tokenSymbol"])
                        self.ui.Confirm_Symbol_Out.setText(self.GS.B_TOKEN)
                        self.ui.Confirm_Amount_In.setText(str(self.ui.Input_MS.text()))
                        self.ui.Confirm_Amount_Out.setText(str(self.ui.Output_MS.text()))
                        self.ui.stackedWidget_16.setCurrentWidget(self.ui.Submit_Page)

                        if self.GS.B_TOKEN == "BNB":
                            Status, Estimate_Fee, Signed_TX = self.web3.createSignedTransactionTokentoETH(
                                self.US.ADDRESS, self.token_address, float(self.ui.Input_MS.text()),self.jsonTokenData["tokenDecimals"], self.US.SLIPPAGE,  self.US.GAS,  self.US.PRIVKEY)
                        elif self.GS.B_TOKEN == "BUSD":
                            if self.token_address == self.web3.WBNB:
                                Status, Estimate_Fee, Signed_TX = self.web3.createSignedTransactionETHtoToken(
                                    self.US.ADDRESS, self.web3.BUSD, float(self.ui.Input_MS.text()), self.US.SLIPPAGE,  self.US.GAS,  self.US.PRIVKEY)
                        elif self.GS.B_TOKEN == "BUSD":
                            Status, Estimate_Fee, Signed_TX = self.web3.createSignedTransactionTokentoToken(
                                self.US.ADDRESS, self.token_address, self.web3.BUSD, float(self.ui.Input_MS.text()), self.jsonTokenData["tokenDecimals"], self.US.SLIPPAGE,  self.US.GAS,  self.US.PRIVKEY)
                        if Status == True:
                            self.ui.Confirm_TX_FEE_ETH.setText(str(self.math.FloatToCleanSting(Estimate_Fee)))
                            try:
                                self.ui.pushButton_Submit_Confirm.clicked.diconnect()
                            except:
                                pass
                            self.ui.pushButton_Submit_Confirm.clicked.connect(lambda: self.SubmitTransaction())
                            self.ui.stackedWidget_16.setCurrentWidget(self.ui.Submit_Page)
                            self.Signed_TX = Signed_TX
                        else:
                            self.ui.label_ErrorMessage.setText(str(Status))
                            status = False
                    elif side == "BUY":

                        self.ui.Confirm_OrderType.setText(type + " " + side)
                        self.ui.Confirm_OrderType.setStyleSheet(Ui_Styles().BUY_label)
                        self.ui.Confirm_Symbol_In.setText(self.GS.B_TOKEN)
                        self.ui.Confirm_Symbol_Out.setText(self.jsonTokenData["tokenSymbol"])
                        self.ui.Confirm_Amount_In.setText(str(self.ui.Input_MB.text()))
                        self.ui.Confirm_Amount_Out.setText(str(self.ui.Output_MB.text()))  

                        if self.GS.B_TOKEN == "BNB":
                            Status, Estimate_Fee, Signed_TX= self.web3.createSignedTransactionETHtoToken(
                                self.US.ADDRESS, self.token_address, float(self.ui.Input_MB.text()), self.US.SLIPPAGE,  self.US.GAS,  self.US.PRIVKEY)
                        elif self.GS.B_TOKEN == "BUSD":
                            Status, Estimate_Fee, Signed_TX= self.web3.createSignedTransactionTokentoToken(
                                self.US.ADDRESS, self.web3.BUSD, self.token_address, float(self.ui.Input_MB.text()), 18, self.US.SLIPPAGE,  self.US.GAS,  self.US.PRIVKEY)
                        if Status == True:
                            self.ui.Confirm_TX_FEE_ETH.setText(str(self.math.FloatToCleanSting(Estimate_Fee)))
                            try:
                                self.ui.pushButton_Submit_Confirm.clicked.diconnect()
                            except:
                                pass
                            self.ui.pushButton_Submit_Confirm.clicked.connect(lambda: self.SubmitTransaction())
                            self.ui.stackedWidget_16.setCurrentWidget(self.ui.Submit_Page)
                            self.Signed_TX = Signed_TX
                    
                        else:
                            self.ui.label_ErrorMessage.setText(str(Status))
                            status = False
                else:
                    self.ui.label_ErrorMessage.setText("Check your Input or Output Amount!")
                    status = False


            if type == "LIMIT":
                if float(self.ui.Input_LB.text()) != 0 or float(self.ui.Input_LS.text()) !=0:
                    if float(self.ui.Price_LB.text()) != 0 or float(self.ui.Price_LS.text()) !=0:
                        try:
                            self.ui.pushButton_Submit_Order.clicked.disconnect()
                        except:
                            pass
                        if side == "BUY":
                            self.LO = self.createOrderDict("BUY", self.GS.B_TOKEN,
                             float(self.ui.Input_LB.text()), self.jsonTokenData["tokenSymbol"],
                              float(self.ui.Price_LB.text()), self.token_address)
                              
                            status = True
                        elif side == "SELL":
                            self.LO = self.createOrderDict("SELL", self.jsonTokenData["tokenSymbol"],
                             float(self.ui.Input_LS.text()), self.GS.B_TOKEN,
                             float(self.ui.Price_LS.text()), self.token_address)
                            status = True

                        if status:
                            self.ui.Order_OrderType.setText(str(side))
                            if side == "BUY":
                                self.ui.Order_OrderType.setStyleSheet(Ui_Styles().BUY_label)
                            if side == "SELL":
                                self.ui.Order_OrderType.setStyleSheet(Ui_Styles().SELL_label)
                            self.ui.Order_Amount.setText(str(self.LO["INPUT_AMOUNT"]))
                            self.ui.Order_Symbol_In.setText(self.LO["INPUT_SYMBOL"])
                            self.ui.Order_Price.setText(str(self.LO["TARGET_PRICE"]) + " $")
                            self.ui.Confirm_Orderway.setText(str(self.LO["INPUT_SYMBOL"] +" -> " + self.LO["OUTPUT_SYMBOL"]))
                            self.ui.stackedWidget_16.setCurrentWidget(self.ui.page_LimitOrder)
                            self.ui.pushButton_Submit_Order.clicked.connect(lambda: self.saveOrder())


                    else:
                        self.ui.label_ErrorMessage.setText("Check your Target Price!")
                        status = False
                else:
                    self.ui.label_ErrorMessage.setText("Check your Input Amount!")
                    status = False

        if not status:
            self.ui.stackedWidget_16.setCurrentWidget(self.ui.Error_Page)

            
    def createOrderDict(self, side, INPUT_SYMBOL, INPUT_AMOUNT, OUTPUT_SYMBOL, TARGET_PRICE, TOKEN_ADDRESS):
        return {
        "ID": str(''.join(random.choice(string.ascii_letters) for x in range(5))).upper(),
        "SIDE": side,
        "INPUT_SYMBOL": INPUT_SYMBOL,
        "INPUT_AMOUNT": INPUT_AMOUNT,
        "OUTPUT_SYMBOL": OUTPUT_SYMBOL,
        "TARGET_PRICE": TARGET_PRICE,
        "TOKEN_ADDRESS": TOKEN_ADDRESS
        }

    def saveOrder(self):
        self.OS.addNewOrder(self.LO)
        self.ui.stackedWidget_16.setCurrentWidget(self.ui.Chart_Loaded)
        self.initOpenOrders()
        self.resetInputs()
        del self.LO


    def ApproveToken(self, Token_Address):
        try:
            self.ui.pushButton_Submit_Approve.clicked.disconnect()
        except:
            pass
        Status = True
        try:

            self.ui.Approve_Symbol.setText(self.jsonTokenData["tokenSymbol"])
            self.ui.Approve_Symbol.setText(self.jsonTokenData["tokenSymbol"])
            status, Estimate_Fee, Signed_TX = self.web3.createSignedTransactionApproveMAX(self.US.ADDRESS, Token_Address, self.US.GAS, self.US.PRIVKEY)
            self.ui.Approve_TX_FEE_ETH.setText(self.math.FloatToCleanSting(Estimate_Fee))
            if status == True:
                self.ui.stackedWidget_16.setCurrentWidget(self.ui.Approve_Page)
                self.ui.pushButton_Submit_Approve.clicked.connect(lambda: self.SubmitTransaction())
                self.Signed_TX = Signed_TX
            else:
                self.ui.label_ErrorMessage.setText(str(status))
                Status = False
        except Exception as e:
            Status = False
            self.ui.label_ErrorMessage.setText(str(e))
            print(e)

        if not Status:
            self.ui.stackedWidget_16.setCurrentWidget(self.ui.Error_Page)

    
    def waitTransaction(self):
        try:
            self.ui.Transaction_Succesfully.hide()
        except:
            pass
        try:
            self.ui.Transaction_Fail.hide()
        except:
            pass
        result = self.web3.awaitTransaction(self.tx)
        if result: # 1 == True :)
            self.ui.Transaction_Succesfully.show()
            self.ui.Input_TX_HEX.setText(str(self.tx.hex()))
            self.ui.stackedWidget_16.setCurrentWidget(self.ui.page_TX_Status)
        else:
            self.ui.Transaction_Fail.show()
            self.ui.Input_TX_HEX.setText(str(self.tx.hex()))
            self.ui.stackedWidget_16.setCurrentWidget(self.ui.page_TX_Status)
        del self.tx
        

    def SubmitTransaction(self):
        try:
            self.ui.stackedWidget_16.setCurrentWidget(self.ui.chart_isLoading) 
            if self.US.WAIT_TX_STATUS:
                self.tx = self.web3.SubmitTransaction(self.Signed_TX)
                self.waitTransaction()
            else:
                self.web3.SubmitTransaction(self.Signed_TX)
                self.ui.stackedWidget_16.setCurrentWidget(self.ui.Chart_Loaded)
            self.resetInputs()
            del self.Signed_TX
        except:
            self.ui.stackedWidget_16.setCurrentWidget(self.ui.Chart_Loaded)
            pass
        
        



    def loadAddButton(self):
        for token in self.US.TOKEN_LIST:
            AllreadyinList =  Web3.toChecksumAddress(self.token_address) == Web3.toChecksumAddress(token)
            if AllreadyinList:
                break
        try:
            self.ui.pushButton_AddtoList.clicked.disconnect()
        except:
            pass
        if AllreadyinList:
            self.ui.pushButton_AddtoList.hide()
        else:
            self.ui.pushButton_AddtoList.show()
            self.ui.pushButton_AddtoList.clicked.connect(self.addTokenAddressToList)

    def addTokenAddressToList(self):
        self.US.TOKEN_LIST.append(self.token_address)
        self.US.changeUserSetting("TOKEN_LIST",self.US.TOKEN_LIST)
        self.loadAddButton()
    
    def update_TokenTax(self):
        self.threadpool.start(AExecutor(self.refresh_tokenTax))

    def update_TokenInfos(self):
        self.threadpool.start(AExecutor(self.refresh_token_infos))

    def refresh_tokenTax(self):
        Successfull, buy_tax, sell_tax  = self.web3.checkTokenTax(self.token_address)
        if Successfull == True:
            self.ui.label_token_BuyTax_2.setText(str(buy_tax)+ " %")
            self.ui.label_token_BuyTax.setText(str(buy_tax)+ " %")
            self.ui.label_token_SellTax_2.setText(str(sell_tax)+ " %")
            self.ui.label_token_SellTax.setText(str(sell_tax)+ " %")
        else:
            self.ui.label_token_BuyTax_2.setText("?? %")
            self.ui.label_token_BuyTax.setText("?? %")
            self.ui.label_token_SellTax_2.setText("?? %")
            self.ui.label_token_SellTax.setText("?? %")


    def refresh_token_infos(self):
        try:
            data = self.web3.fetchWalletTokenInformations(self.US.ADDRESS, [self.token_address])

            if str(data[1][0]) == "WBNB":
                self.jsonTokenData = {'tokenName': "Binance Coin", 'tokenSymbol': "BNB", 'tokenDecimals': 18 }
            else:
                self.jsonTokenData = {'tokenName': data[0][0], 'tokenSymbol': data[1][0], 'tokenBalance': float(data[2][0] / 10**int(data[4][0])), 'tokenPrice': float(data[3][0] / 10**18), 'tokenBalance_USD': float(data[2][0] / 10**int(data[4][0]) * data[3][0] / 10**18), 'tokenDecimals': data[4][0] }

            namestr = str(self.jsonTokenData['tokenName']) + " ( " + str(self.jsonTokenData['tokenSymbol']) + " )" 
            self.ui.TokenName.setText(namestr)
            self.ui.TokenName_LB.setText(namestr)
            self.ui.TokenName_LS.setText(namestr)
            self.ui.TokenName_MS.setText(namestr)
            self.ui.TokenName_MB.setText(namestr)
            self.initTradeSymbols()
        except Exception as e:
            print(e)
            name = self.web3.fetchName(self.token_address)
            self.ui.TokenName.setText(name)
            self.ui.TokenName_LB.setText(name)
            self.ui.TokenName_LS.setText(name)
            self.ui.TokenName_MS.setText(name)
            self.ui.TokenName_MB.setText(name)




    def update_Price(self):
        try:
            self.current_price = self.math.FloatToCleanSting(self.web3.fetchCurrentPrice(self.token_address))
            self.ui.TokenPrice.setText(str(self.current_price)+ " $  ")
        except Exception as e:
            print(e)
            pass



    def refresh_datas(self, a, b):
        if a == True:
            first_Price = float(b[0][3][0])
            percent = round(self.math.get_change(float(self.current_price), float(first_Price)), 2)
            p = str(percent) + " %"
            if str(p[-0]) == "-":
                self.ui.TokenPriceChange.setStyleSheet(u"color:rgb(196, 49, 69);\nfont-weight: bold;\nbackground:transparent;\nfont-size: 10pt;")
                prefix= ""
            else:
                self.ui.TokenPriceChange.setStyleSheet(u"color:#006626;\nfont-weight: bold;\nbackground:transparent;\nfont-size: 10pt;")
                prefix= "+"
            self.ui.TokenPriceChange.setText( str(prefix + p))
            fplt.candlestick_ochl(b[0], ax = self.ax)
            if self.GS.MA20 == True:
                fplt.plot(b[1], legend = "MA-20", ax = self.ax, size=3)
            if self.GS.VOLUME == True:
                fplt.volume_ocv(b[2], ax=self.axo)
            fplt.refresh()
            self.ui.stackedWidget_16.setCurrentWidget(self.ui.Chart_Loaded)
            print("updated Chart")
        else:
            print("Request Fail!")




    def fetchTokenData(self):
        try:
            req = self.chart_functions.doRequest(self.GS.candleTimeMin, self.GS.candleHistory)
            df = pd.DataFrame(req)
            df = df.rename(columns={'t':'Time', 'o':'Open', 'c':'Close', 'h':'High', 'l':'Low', 'v':'Volume'})
            o = df['Open']#.apply(float(self.math.FloatToCleanSting))
            c = df['Close']#.apply(float(self.math.FloatToCleanSting))
            h = df['High']#.apply(float(self.math.FloatToCleanSting))
            l = df['Low']#.apply(float(self.math.FloatToCleanSting))
            v = df['Volume']#.apply(float(self.math.FloatToCleanSting))
            candles = df['Time'], o, c, h, l
            ma20 = df.Close.rolling(20).mean()
            volume = df["Time"], o, c, v
            data = candles, ma20, volume
            return data
        except Exception as e:
            return e


    def fetchWalletBalances(self):
        t = []
        for i in range(0, len(self.US.TOKEN_LIST), 40):
            t.append(self.US.TOKEN_LIST[i:i+40])
        data = [[],[],[],[],[]]
        for token in t:
            d = self.web3.fetchWalletTokenInformations(self.US.ADDRESS, token)
            data[0].extend(d[0])
            data[1].extend(d[1])
            data[2].extend(d[2])
            data[3].extend(d[3])
            data[4].extend(d[4])
        i = 0
        rou = []
        ETHdata = self.web3.fetchEthWalletInfos(self.US.ADDRESS)
        rou.append({
            'tokenAddress': self.web3.WBNB,
            'tokenName': "Binance Coin",
            'tokenSymbol': "BNB",
            'tokenBalance': float(ETHdata[0] / 10**18),
            'tokenPrice': float(ETHdata[1]),
            'tokenBalance_USD': float(ETHdata[0] * ETHdata[1] / 10**18),
            'tokenDecimals': 18
            })

        for tokenAddress in self.US.TOKEN_LIST:
            rou.append({
            'tokenAddress': tokenAddress,
            'tokenName': data[0][i],
            'tokenSymbol': data[1][i],
            'tokenBalance': float(data[2][i] / 10**int(data[4][i])),
            'tokenPrice': float(data[3][i] / 10**18),
            'tokenBalance_USD': float(data[2][i] / 10**int(data[4][i]) * data[3][i] / 10**18),
            'tokenDecimals': data[4][i]
            })
            i += 1
        rou.sort(key=lambda x: x.get('tokenBalance_USD'), reverse=True)
        return rou


    def update_chart_dex(self):
        self.ui.stackedWidget_16.setCurrentWidget(self.ui.chart_isLoading)
        self.ax.reset()
        self.axo.reset()
        worker = AWorker(self.fetchTokenData)
        worker.signals.result.connect(self.refresh_datas)
        self.threadpool.start(worker)


    def update_wallet_balance(self):
        worker = AWorker(self.fetchWalletBalances)
        worker.signals.result.connect(self.editScrollAreaWidget)
        self.threadpool.start(worker)

    def calcMBuyOutput(self):
        InputAmount = self.ui.Input_MB.text()
        try:
            float(InputAmount)
            if float(InputAmount) != float(0):
                status = True
            else:
                status = False
        except:
            status = False  
        if status == True:
            Slippage = (float(InputAmount) / 100 * self.US.SLIPPAGE)
            Amount = int( (float(InputAmount) - float(Slippage)) * 10**18 )
            if self.GS.B_TOKEN == "BNB":
                BaseAddress = self.web3.WBNB
            elif self.GS.B_TOKEN == "BUSD":
                BaseAddress = self.web3.BUSD
            OutputAmount = self.math.FloatToCleanSting(
                self.web3.fetchOutputAmount(
                    Amount, BaseAddress,
                    self.token_address)[0] / 10**self.jsonTokenData["tokenDecimals"]
                    )
            self.ui.Output_MB.textChanged.disconnect()
            self.ui.Output_MB.setText(OutputAmount)
            self.ui.Output_MB.textChanged.connect(self.calcMBuyInput)


    def calcMSellOutput(self):
        InputAmount = self.ui.Input_MS.text()
        try:
            float(InputAmount)
            if float(InputAmount) != float(0):
                status = True
            else:
                status = False
        except:
            status = False  
        if status == True:
            Slippage = (float(InputAmount) / 100 * self.US.SLIPPAGE)
            Amount = int( (float(InputAmount) - float(Slippage)) * 10**self.jsonTokenData['tokenDecimals'] )
            print(Amount)
            if self.GS.B_TOKEN == "BNB":
                BaseAddress = self.web3.WBNB
            elif self.GS.B_TOKEN == "BUSD":
                BaseAddress = self.web3.BUSD
            OutputAmount = self.math.FloatToCleanSting(
                self.web3.fetchOutputAmount(
                    Amount, 
                    self.token_address,
                    BaseAddress
                    )[0] / 10**18)
            self.ui.Output_MS.textChanged.disconnect()
            self.ui.Output_MS.setText(OutputAmount)
            self.ui.Output_MS.textChanged.connect(self.calcMSellInput)


    def calcMSellInput(self):
        OutputAmount = self.ui.Output_MS.text()
        try:
            float(OutputAmount)
            if float(OutputAmount) != float(0):
                status = True
            else:
                status = False
        except:
            status = False  
        if status == True:
            Slippage = (float(OutputAmount) / 100 * self.US.SLIPPAGE)
            Amount = int( (float(OutputAmount) + float(Slippage)) * 10**self.jsonTokenData['tokenDecimals'])
            print(Amount)
            if self.GS.B_TOKEN == "BNB":
                BaseAddress = self.web3.WBNB
            elif self.GS.B_TOKEN == "BUSD":
                BaseAddress = self.web3.BUSD
            InputAmount = self.math.FloatToCleanSting(
                self.web3.fetchOutputAmount(
                    Amount, 
                    BaseAddress,
                    self.token_address
                    )[0] / 10**18)
            self.ui.Input_MS.textChanged.disconnect()
            self.ui.Input_MS.setText(InputAmount )
            self.ui.Input_MS.textChanged.connect(self.calcMSellOutput)


    def calcMBuyInput(self):
        OutputAmount = self.ui.Output_MB.text()
        try:
            float(OutputAmount)
            if float(OutputAmount) != float(0):
                status = True
            else:
                status = False
        except:
            status = False  
        if status == True:
            Slippage = (float(OutputAmount) / 100 * self.US.SLIPPAGE)
            Amount = int( (float(OutputAmount) + float(Slippage)) * 10**self.jsonTokenData['tokenDecimals'] )
            print(Amount)
            if self.GS.B_TOKEN == "BNB":
                BaseAddress = self.web3.WBNB
            elif self.GS.B_TOKEN == "BUSD":
                BaseAddress = self.web3.BUSD
            InputAmount = self.math.FloatToCleanSting(
                self.web3.fetchOutputAmount(
                    Amount, 
                    self.token_address,
                    BaseAddress
                    )[0] / 10**18)
            print(InputAmount)
            self.ui.Input_MB.textChanged.disconnect()
            self.ui.Input_MB.setText(InputAmount)
            self.ui.Input_MB.textChanged.connect(self.calcMBuyOutput)


    def resetInputs(self):
        self.ui.Output_MS.setText(str(0))
        self.ui.Input_MS.setText(str(0))
        self.ui.Output_MB.setText(str(0))
        self.ui.Input_MB.setText(str(0))
        self.ui.Input_LS.setText(str(0))
        self.ui.Price_LS.setText(str(0))
        self.ui.Input_LB.setText(str(0))
        self.ui.Price_LB.setText(str(0))


    def checkSaveSettings(self):
        try:
            self.ui.frame_Settings_error.hide()
        except:pass
        try:
            self.ui.label_Settings_error.show()
        except:pass       
        try:
            self.ui.frame_Settings_success.hide()
        except:pass      
        e = True
        if len(self.ui.Input_Settings_Address.text()) != 0:
            if Web3.isAddress(self.ui.Input_Settings_Address.text()):
                self.US.changeUserSetting("ADDRESS",Web3.toChecksumAddress(self.ui.Input_Settings_Address.text()))
        if len(self.ui.Input_Settings_PrivateKey.text()) != 0:
            try:
                self.US.changeUserSetting("SECRETKEY", self.ui.Input_Settings_PrivateKey.text())
            except Exception as e:
                self.showSettingsError(e)
                print(e)
                e = False
        if len(self.ui.Input_Settings_provider.text()) != 0:
            try:
                providerTest = web3ProviderTester().runTest(self.ui.Input_Settings_provider.text())
                if providerTest:
                    self.US.changeUserSetting("PROVIDER", self.ui.Input_Settings_provider.text())
            except Exception as e:
                self.showSettingsError(e)
                print(e)
                e = False
        if len(self.ui.Input_Settings_Slippage.text()) != 0:
            try:
                float(self.ui.Input_Settings_Slippage.text())
                self.US.changeUserSetting("SLIPPAGE", float(self.ui.Input_Settings_Slippage.text()))
            except Exception as e:
                self.showSettingsError(e)
                print(e)
                e = False
        if len(self.ui.Input_Settings_GAS.text()) != 0:
            try:
                float(self.ui.Input_Settings_GAS.text())
                self.US.changeUserSetting("GAS_GWEI", float(self.ui.Input_Settings_GAS.text()))
            except Exception as e:
                self.showSettingsError(e)
                print(e)
                e = False
        if len(self.ui.Input_Settings_OQI.text()) != 0:
            try:
                float(self.ui.Input_Settings_OQI.text())
                self.US.changeUserSetting("ORDER_QUERY_INTERVAL", float(self.ui.Input_Settings_OQI.text()))
            except Exception as e:
                self.showSettingsError(e)
                print(e)
                e = False
        if len(self.ui.Input_Settings_SQI.text()) != 0:
            try:
                float(self.ui.Input_Settings_SQI.text())
                self.US.changeUserSetting("SNIPER_QUERY_INTERVAL", float(self.ui.Input_Settings_SQI.text()))
            except Exception as e:
                self.showSettingsError(e)
                print(e)
                e = False
        self.US.changeUserSetting("WAIT_TX_STATUS", self.ui.checkBox_WaitTXStatus.isChecked())
        self.US.changeUserSetting("AUTOSTART_ORDERS", self.ui.checkBox_AutoStart_Orders.isChecked())
        self.US.changeUserSetting("AUTOSTART_SNIPER", self.ui.checkBox_AutoStart_Sniper.isChecked())
        if e:
            self.ui.frame_Settings_error.show()
            self.ui.label_Settings_error.hide()

        
    def showSettingsError(self, e):
        try:
            self.ui.label_Settings_error.setText(str(e))
            self.ui.label_Settings_error.show()
        except:
            pass
        
        
    def changeIndicatorSettings(self, SETTING):
        if SETTING == "MA20":
            if self.GS.MA20 == True:
                self.GS.changeGlobalSetting("MA20", False)
            else:
                self.GS.changeGlobalSetting("MA20", True)
        if SETTING == "VOLUME":
            if self.GS.VOLUME == True:
                self.GS.changeGlobalSetting("VOLUME", False)
            else:
                self.GS.changeGlobalSetting("VOLUME", True)
        self.selectIndicatorsButtons()
        self.update_chart_dex()


    def changeCandleTime(self, TIME):
        self.GS.changeGlobalSetting("CandleTimeMin", TIME)
        self.selectCandleTime()
        self.update_chart_dex()

    def changeCandleHistoryTime(self, TIME):
        self.GS.changeGlobalSetting("CandleHistory", TIME)
        self.selectCandleHistoryTime()
        self.update_chart_dex()

    def changeBToken(self, B_TOKEN):
        self.GS.changeGlobalSetting("BASE_TOKEN", B_TOKEN)
        self.selectBaseToken()
        self.resetInputs()
        self.update_TokenAllowance()

    def changeOrderType(self, ORDER_TYPE):
        self.GS.changeGlobalSetting("ORDER_TYPE", ORDER_TYPE)
        self.selectOrderType()

    def changeMenuButton(self, MENU_BUTTON):
        self.GS.changeGlobalSetting("MENU_BUTTON", MENU_BUTTON)
        self.selectMenuButton()

    def initSettingsInputs(self):
        self.ui.Input_Settings_Address.setText(self.US.ADDRESS)
        self.ui.Input_Settings_PrivateKey.setText(self.US.PRIVKEY)
        self.ui.Input_Settings_Slippage.setText(str(self.US.SLIPPAGE))
        self.ui.Input_Settings_provider.setText(self.US.PROVIDER)
        self.ui.Input_Settings_OQI.setText(str(self.US.OQI))
        self.ui.Input_Settings_SQI.setText(str(self.US.SQI))
        self.ui.Input_Settings_GAS.setText(str(self.US.GAS))
        self.ui.checkBox_WaitTXStatus.setChecked(self.US.WAIT_TX_STATUS)
        self.ui.checkBox_AutoStart_Orders.setChecked(self.US.AUTOSTART_ORDERS)
        self.ui.checkBox_AutoStart_Sniper.setChecked(self.US.AUTOSTART_SNIPER)
        try:
            self.ui.pushButton_Save_Settings.clicked.disconnect()
        except:
            pass
        try:
            self.ui.pushButton_Discard_Settings.clicked.disconnect()
        except:
            pass
        self.ui.pushButton_Save_Settings.clicked.connect(self.checkSaveSettings)
        self.ui.pushButton_Discard_Settings.clicked.connect(self.initSettingsInputs)
        

    def initTradeInputs(self):
        self.ui.Input_MB.textChanged.connect(self.calcMBuyOutput)
        self.ui.Input_MS.textChanged.connect(self.calcMSellOutput)
        self.ui.Output_MB.textChanged.connect(self.calcMBuyInput)
        self.ui.Output_MS.textChanged.connect(self.calcMSellInput)
    

    def initTradeSymbols(self):
        self.ui.Input_MB_tokenSymbol.setText(self.GS.B_TOKEN)
        self.ui.Output_MB_tokenSymbol.setText(str(self.jsonTokenData["tokenSymbol"]))
        self.ui.Input_MS_tokenSymbol.setText(str(self.jsonTokenData["tokenSymbol"]))
        self.ui.Output_MS_tokenSymbol.setText(self.GS.B_TOKEN)
        self.ui.Input_LB_tokenSymbol.setText(self.GS.B_TOKEN)

        self.ui.Output_LB_tokenSymbol.setText("$")
        self.ui.Input_LS_tokenSymbol.setText(str(self.jsonTokenData["tokenSymbol"]))
        self.ui.Output_LS_tokenSymbol.setText("$")


    def initChart(self):
        self.movie = QMovie(r'ui/icons/Spinner.gif')
        self.ui.chart_loading.setMovie(self.movie)
        self.ui.chart_loading.setAlignment(Qt.AlignCenter)
        self.movie.setScaledSize(QSize(275, 275))
        self.movie.start()
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")
        area = DockArea()
        dock_0 = Dock("Chart", hideTitle=True, closable = False)
        self.ax = fplt.create_plot_widget(master=area,rows=1, init_zoom_periods=10**10)
        self.axo = self.ax.overlay()
        area.axs = [self.ax]
        dock_0.addWidget(self.ax.ax_widget, 1, 0, 1, 2)
        area.addDock(dock_0)
        self.layChart = QVBoxLayout()
        self.layChart.setContentsMargins(0, 0, 0, 0)
        self.layChart.addWidget(area)
        self.ui.chart_container.setLayout(self.layChart)


    def initOpenOrders(self):
        self.OS.LoadOrders()
        layout = self.ui.scrollArea_ordersWidgetContents.layout()
        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().deleteLater()
        for order in self.OS.ORDERS:
            o = self.uif.createOrderContainer(self, order["ID"], order["INPUT_SYMBOL"], order["OUTPUT_SYMBOL"], order["SIDE"], order["TARGET_PRICE"], order["INPUT_AMOUNT"])
            layout.addWidget(o)


    def initButtonValidators(self):
        NumberValidator = QDoubleValidator(0.0, 5.0, 8)
        self.ui.Input_LB.setValidator(NumberValidator)
        self.ui.Input_LS.setValidator(NumberValidator)
        self.ui.Price_LS.setValidator(NumberValidator)
        self.ui.Price_LB.setValidator(NumberValidator)
        self.ui.Input_MB.setValidator(NumberValidator)
        self.ui.Input_MS.setValidator(NumberValidator)
        self.ui.Output_MB.setValidator(NumberValidator)
        self.ui.Output_MS.setValidator(NumberValidator)

    def initButtonsChart(self):
        self.ui.pushButton_Chart_1m.clicked.connect(lambda: self.changeCandleTime(1))
        self.ui.pushButton_Chart_5m.clicked.connect(lambda: self.changeCandleTime(5))
        self.ui.pushButton_Chart_10m.clicked.connect(lambda: self.changeCandleTime(10))
        self.ui.pushButton_Chart_30m.clicked.connect(lambda: self.changeCandleTime(30))
        self.ui.pushButton_Chart_1h.clicked.connect(lambda: self.changeCandleTime(60))
        self.ui.pushButton_Chart_1d.clicked.connect(lambda: self.changeCandleTime(1440))
        self.ui.pushButton_ChartTime_1h.clicked.connect(lambda: self.changeCandleHistoryTime(1))
        self.ui.pushButton_ChartTime_1d.clicked.connect(lambda: self.changeCandleHistoryTime(24))
        self.ui.pushButton_ChartTime_1w.clicked.connect(lambda: self.changeCandleHistoryTime(168))
        self.ui.pushButton_ChartTime_1m.clicked.connect(lambda: self.changeCandleHistoryTime(672))
        self.ui.pushButton_ChartTime_1y.clicked.connect(lambda: self.changeCandleHistoryTime(8064))

    def initButtonsBToken(self):
        self.ui.Button_Base_BNB_MB.clicked.connect(lambda: self.changeBToken("BNB"))
        self.ui.Button_Base_BNB_MS.clicked.connect(lambda: self.changeBToken("BNB"))
        self.ui.Button_Base_BUSD_MB.clicked.connect(lambda: self.changeBToken("BUSD"))
        self.ui.Button_Base_BUSD_MS.clicked.connect(lambda: self.changeBToken("BUSD"))
        self.ui.Button_Base_BNB_LB.clicked.connect(lambda: self.changeBToken("BNB"))
        self.ui.Button_Base_BNB_LS.clicked.connect(lambda: self.changeBToken("BNB"))
        self.ui.Button_Base_BUSD_LS.clicked.connect(lambda: self.changeBToken("BUSD"))
        self.ui.Button_Base_BUSD_LB.clicked.connect(lambda: self.changeBToken("BUSD"))

    def initButtonsOrderType(self):
        self.ui.Button_Market.clicked.connect(lambda: self.changeOrderType("MARKET"))
        self.ui.Button_Limit.clicked.connect(lambda: self.changeOrderType("LIMIT"))

    def initButtonsMenu(self):
        self.ui.pushButton_Wallet.clicked.connect(lambda: self.changeMenuButton("WALLET"))
        self.ui.pushButton_Orders.clicked.connect(lambda: self.initOpenOrders())
        self.ui.pushButton_Orders.clicked.connect(lambda: self.changeMenuButton("ORDERS"))
        self.ui.pushButton_Settings.clicked.connect(lambda: self.initSettingsInputs())
        self.ui.pushButton_Settings.clicked.connect(lambda: self.changeMenuButton("SETTINGS"))


    def selectCandleTime(self):
        if self.GS.candleTimeMin == 1:
            self.ui.pushButton_Chart_1m.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.pushButton_Chart_1m.setStyleSheet(Ui_Styles.btn_CandelTime)
        if self.GS.candleTimeMin == 5:
            self.ui.pushButton_Chart_5m.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.pushButton_Chart_5m.setStyleSheet(Ui_Styles.btn_CandelTime)
        if self.GS.candleTimeMin == 10:
            self.ui.pushButton_Chart_10m.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.pushButton_Chart_10m.setStyleSheet(Ui_Styles.btn_CandelTime)
        if self.GS.candleTimeMin == 30:
            self.ui.pushButton_Chart_30m.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.pushButton_Chart_30m.setStyleSheet(Ui_Styles.btn_CandelTime)
        if self.GS.candleTimeMin == 60:
            self.ui.pushButton_Chart_1h.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.pushButton_Chart_1h.setStyleSheet(Ui_Styles.btn_CandelTime)
        if self.GS.candleTimeMin == 1440:
            self.ui.pushButton_Chart_1d.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.pushButton_Chart_1d.setStyleSheet(Ui_Styles.btn_CandelTime)


    def selectCandleHistoryTime(self):
        if self.GS.candleHistory == 1:
            self.ui.pushButton_ChartTime_1h.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.pushButton_ChartTime_1h.setStyleSheet(Ui_Styles.btn_CandelTime)
        if self.GS.candleHistory == 24:
            self.ui.pushButton_ChartTime_1d.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.pushButton_ChartTime_1d.setStyleSheet(Ui_Styles.btn_CandelTime)
        if self.GS.candleHistory == 168:
            self.ui.pushButton_ChartTime_1w.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.pushButton_ChartTime_1w.setStyleSheet(Ui_Styles.btn_CandelTime)
        if self.GS.candleHistory == 672:
            self.ui.pushButton_ChartTime_1m.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.pushButton_ChartTime_1m.setStyleSheet(Ui_Styles.btn_CandelTime)
        if self.GS.candleHistory == 8064:
            self.ui.pushButton_ChartTime_1y.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.pushButton_ChartTime_1y.setStyleSheet(Ui_Styles.btn_CandelTime)

    def selectIndicatorsButtons(self):
        if self.GS.MA20 == True:
            self.ui.ButtonchartHelper_MA20.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.ButtonchartHelper_MA20 .setStyleSheet(Ui_Styles.btn_CandelTime)
        if self.GS.VOLUME == True:
            self.ui.ButtonChartHelper_Volume.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
        else:
            self.ui.ButtonChartHelper_Volume.setStyleSheet(Ui_Styles.btn_CandelTime)


    def selectBaseToken(self):
        if self.GS.B_TOKEN == "BNB":
            self.ui.Button_Base_BNB_MB.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.Button_Base_BNB_MS.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.Button_Base_BNB_LB.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.Button_Base_BNB_LS.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.Button_Base_BUSD_MB.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.Button_Base_BUSD_MS.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.Button_Base_BUSD_LB.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.Button_Base_BUSD_LS.setStyleSheet(Ui_Styles.btn_CandelTime)

        elif self.GS.B_TOKEN == "BUSD":
            self.ui.Button_Base_BUSD_MB.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.Button_Base_BUSD_MS.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.Button_Base_BUSD_LB.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.Button_Base_BUSD_LS.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.Button_Base_BNB_MB.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.Button_Base_BNB_MS.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.Button_Base_BNB_LB.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.Button_Base_BNB_LS.setStyleSheet(Ui_Styles.btn_CandelTime)
        try:
            self.initTradeSymbols()
        except:
            pass
    
    def selectOrderType(self):
        if self.GS.OT == "MARKET":
            self.ui.Button_Market.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.Button_Limit.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.stackedWidget_17.setCurrentWidget(self.ui.Trade_Market)
        elif self.GS.OT == "LIMIT":
            self.ui.Button_Limit.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.Button_Market.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.stackedWidget_17.setCurrentWidget(self.ui.Trade_Limit)


    def selectMenuButton(self):
        if self.GS.BM == "WALLET":
            self.ui.pushButton_Wallet.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.pushButton_Orders.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.pushButton_Settings.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.WalletOverview)
        elif self.GS.BM == "ORDERS":
            self.ui.pushButton_Orders.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.pushButton_Settings.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.pushButton_Wallet.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.OrdersOverview)
        elif self.GS.BM == "SETTINGS":
            self.ui.pushButton_Orders.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.pushButton_Settings.setStyleSheet(Ui_Styles.btn_CandelTime_Select)
            self.ui.pushButton_Wallet.setStyleSheet(Ui_Styles.btn_CandelTime)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.SettingsOverview)



    def editScrollAreaWidget(self, status, rou):
        if status == True:
            Balance_all = float()
            layout = self.ui.scrollAreaWidgetContents.layout()
            for i in reversed(range(layout.count())): 
                layout.itemAt(i).widget().deleteLater()
            for info in rou:
                if float(info['tokenBalance']) > 0.0000001:
                    Balance_all += info['tokenBalance_USD']
                    c = self.uif.createWalletTokenContainer(self.ui, info['tokenAddress'], info['tokenSymbol'], info['tokenName'], info['tokenPrice'], info['tokenBalance'], info['tokenBalance_USD'])
                    layout.addWidget(c)
            self.ui.Balance_all.setText("$ " + self.math.FloatToCleanSting(Balance_all))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setWindowIcon(QIcon('ui/icons/favicon.ico'))
    window.setWindowIcon(QIcon('ui/icons/favicon.ico'))
    sys.exit(app.exec_())
