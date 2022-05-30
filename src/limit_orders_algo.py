from imports import *

class LimitOrders_Algo():
    def reinit(self):
        self.GS = Global_Settings() 
        self.US = User_Settings()
        self.LO = LimitOrders_Settings()
        self.web3 = Web3_UI_Functions()

    def initAccountBalances(self):
        self.ETHBalance = float(self.web3.fetchEthWalletInfos(self.US.ADDRESS)[0] / 10**18)
        self.BUSDBalance = float(self.web3.fetchBalance(
            self.web3.BUSD, self.US.ADDRESS) / 10**18)
        self.tokenDecimals = self.web3.fetchDecimals(self.Order["TOKEN_ADDRESS"])
        self.tokenBalance = float(self.web3.fetchBalance(
            self.Order["TOKEN_ADDRESS"], self.US.ADDRESS) / 10**self.tokenDecimals)

    def start(self):
        self.reinit()
        if self.GS.O_ONLINE:
            for Order in self.LO.ORDERS:
                self.checkOrder(Order)

    def checkOrder(self,Order):
        self.Order = Order
        self.initAccountBalances()
        if self.Order["SIDE"] == "BUY":
            self.checkBuyOrder()
        elif self.Order["SIDE"] == "SELL":
            self.checkSellOrder()
        del self.Order


    def checkBuyOrder(self):
        if str(self.Order["INPUT_SYMBOL"]) == str("BNB"):
            if float(self.Order["INPUT_AMOUNT"]) <= float(self.ETHBalance):
                if self.checkBuyPrice():
                    self.ExecuteBuyETH()
            else:
                print("Not Enought Balance to Execute, Delete Order ID:", self.Order["ID"])
                self.LO.deleteOrder(self.Order["ID"])
                self.LO.addFailTX(self.Order, "Not Enought Balance to Execute, Delete Order ID:" + str(self.Order["ID"]))
        elif str(self.Order["INPUT_SYMBOL"]) == str("BUSD"):
            if float(self.Order["INPUT_AMOUNT"]) <= float(self.BUSDBalance):
                if self.checkBuyPrice():
                    self.ExecuteBuyBUSD()
            else:
                print("Not Enought Balance to Execute, Delete Order ID:", self.Order["ID"])
                self.LO.deleteOrder(self.Order["ID"])
                self.LO.addFailTX(self.Order, "Not Enought Balance to Execute, Delete Order ID:" + str(self.Order["ID"]))




    def checkSellOrder(self):
        if str(self.Order["OUTPUT_SYMBOL"]) == str("BNB"):
            if float(self.Order["INPUT_AMOUNT"]) <= float(self.tokenBalance):
                if self.checkSellPrice():
                    self.ExecuteSellETH()
            else:
                print("Not Enought Balance to Execute, Delete Order ID:", self.Order["ID"])
                self.LO.deleteOrder(self.Order["ID"])
                self.LO.addFailTX(self.Order, "Not Enought Balance to Execute, Delete Order ID:" + str(self.Order["ID"]))
        elif str(self.Order["OUTPUT_SYMBOL"]) == str("BUSD"):
            if float(self.Order["INPUT_AMOUNT"]) <= float(self.tokenBalance):
                if self.checkSellPrice():
                    self.ExecuteSellBUSD()
            else:
                print("Not Enought Balance to Execute, Delete Order ID:", self.Order["ID"])
                self.LO.addFailTX(self.Order, "")
                self.LO.addFailTX(self.Order, "Not Enought Balance to Execute, Delete Order ID:" + str(self.Order["ID"]))



    def checkBuyPrice(self):
        self.currentPrice = Math_UI_Functions().FloatToCleanSting(self.web3.fetchCurrentPrice(self.Order["TOKEN_ADDRESS"]))
        if float(self.currentPrice) < self.Order["TARGET_PRICE"]:
            return True
        else:
            return False

    def checkSellPrice(self):
        self.currentPrice = Math_UI_Functions().FloatToCleanSting(self.web3.fetchCurrentPrice(self.Order["TOKEN_ADDRESS"]))

        if float(self.Order["TARGET_PRICE"]) < float(self.currentPrice):
            return True
        else:
            return False


    def ExecuteBuyBUSD(self):
        status, Estimate_Fee, Signed_TX = self.web3.createSignedTransactionTokentoToken(self, self.US.ADDRESS,
            self.web3.BUSD, self.Order["TOKEN_ADDRESS"], self.Order["INPUT_AMOUNT"], self.tokenDecimals,
            self.US.SLIPPAGE,  self.US.GAS,  self.US.PRIVKEY)
        if status:
            self.submitTX(Signed_TX)


    def ExecuteBuyETH(self):
        print("EXECUTE NOW BUY WITH ETH")   
        status, Estimate_Fee, Signed_TX = self.web3.createSignedTransactionETHtoToken(self.US.ADDRESS,
            self.Order["TOKEN_ADDRESS"], self.Order["INPUT_AMOUNT"],
            self.US.SLIPPAGE,  self.US.GAS,  self.US.PRIVKEY) 
        if status:
            self.submitTX(Signed_TX)


    def ExecuteSellBUSD(self):
        print("EXECUTE NOW SELL TO BUSD")
        status, Estimate_Fee, Signed_TX = self.web3.createSignedTransactionTokentoToken(self, self.US.ADDRESS,
            self.Order["TOKEN_ADDRESS"], self.web3.BUSD, self.Order["INPUT_AMOUNT"], self.tokenDecimals,
            self.US.SLIPPAGE,  self.US.GAS,  self.US.PRIVKEY) 
        if status:
            self.submitTX(Signed_TX)


    def ExecuteSellETH(self):
        status, Estimate_Fee, Signed_TX = self.web3.createSignedTransactionTokentoETH(self.US.ADDRESS,
            self.Order["TOKEN_ADDRESS"], self.Order["INPUT_AMOUNT"], self.tokenDecimals,
            self.US.SLIPPAGE,  self.US.GAS,  self.US.PRIVKEY) 
        if status:
            self.submitTX(Signed_TX)




    def submitTX(self, Signed_TX):
        tx = self.web3.SubmitTransaction(Signed_TX)
        status, data = self.web3.awaitTransaction(tx)
        if status:
            print("Execute Order Successfully, Delete Order now!")
            self.LO.deleteOrder(self.Order["ID"])
            self.LO.addSuccessTX(self.Order, tx.hex())
        else:
            print("Execute Order Fail, Delete Order now!")
            self.LO.deleteOrder(self.Order["ID"])
            self.LO.addFailTX(self.Order, tx.hex())
            



        