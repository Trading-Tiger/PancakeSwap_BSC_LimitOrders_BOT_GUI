from imports import *




class web3ProviderTester():
    def runTest(self, RPC):
        self.RPC = RPC
        Supported = self.connectToCHAIN()
        if Supported == True:
            currentBlock, chainID = self.W3.eth.blockNumber, self.W3.eth.chain_id
            return True, chainID, currentBlock
        else:
            return False

    def connectToCHAIN(self):
        if "ws" == str(self.RPC[:2]).lower():
            self.W3 = Web3(Web3.WebsocketProvider(self.RPC))
            return True
        elif "http" == str(self.RPC[:4]).lower():
            self.W3 = Web3(Web3.HTTPProvider(self.RPC))
            return True
        else:
            return False




class Web3_UI_Functions():

    def __init__(self) -> None:
        self.ConfigPath = "./configs/user_config.json"
        self.AbisPath = "./abis/"
        self.WBNB ,self.BUSD = Web3.toChecksumAddress("0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"), Web3.toChecksumAddress("0xe9e7cea3dedca5984780bafc599bd69add087d56")
        self.w3 = self.connect()
        self.swapper_address, self.swapper_contract = self.setup_swapper()

    def reinit(self):
        self.w3 = self.connect()
        self.swapper_address, self.swapper_contract = self.setup_swapper()

    def connect(self):
        with open(self.ConfigPath) as f:
            keys = json.load(f)
        if keys["PROVIDER"][:2].lower() == "ws":
            w3 = Web3(Web3.WebsocketProvider(keys["PROVIDER"]))
        else:
            w3 = Web3(Web3.HTTPProvider(keys["PROVIDER"]))
        return w3

    def estimateGas(self, txn):
        gas = self.w3.eth.estimateGas(txn)
        gas = gas + (gas / 10)
        return gas

    def setup_token(self, Token_Address):
        with open(self.AbisPath + "tokens.json") as f:
            contract_abi = json.load(f)
        token_contract = self.w3.eth.contract(address=Web3.toChecksumAddress(Token_Address), abi=contract_abi)
        return token_contract

    def SubmitTransaction(self, Signed_TX):
        tx = self.w3.eth.sendRawTransaction(Signed_TX.rawTransaction)
        return tx

    def awaitTransaction(self, tx):
        try:
            txn_receipt = self.w3.eth.waitForTransactionReceipt(tx)
            return txn_receipt["status"], txn_receipt
        except Exception as e:
            return False, e
            
#Slow way!
    def fetchName(self, Token_Address):
        tc = self.setup_token(Token_Address)
        return tc.functions.name().call()

    def fetchSymbol(self, Token_Address):
        tc = self.setup_token(Token_Address)
        return tc.functions.symbol().call()

    def fetchDecimals(self, Token_Address):
        tc = self.setup_token(Token_Address)
        return tc.functions.decimals().call()
    
    def fetchBalance(self, Token_Address, User):
        tc = self.setup_token(Token_Address)
        return tc.functions.balanceOf(User).call()


    def setup_swapper(self):
        swapper_address = Web3.toChecksumAddress("0x8e82124aF42BB04732128F538117B9937B937A2F") 
        with open(self.AbisPath + "TIGS_Swapper.json") as f:
            contract_abi = json.load(f)
        swapper = self.w3.eth.contract(address=swapper_address, abi=contract_abi)
        return swapper_address, swapper

    def checkIsTokenContract(self, Token_Address):
        try:
            self.fetchSymbol(Token_Address)
            return True
        except:
            return False

    def fetchCurrentPrice(self, Token_Address):
        decimals = self.fetchDecimals(Token_Address)
        return self.swapper_contract.functions.getOutputfromTokentoToken(
            Web3.toChecksumAddress(Token_Address),
            self.BUSD,
            1 *(10**decimals)
            ).call()[0] / (10**18)

#Fast Way!
    def fetchWalletTokenInformations(self, User, Token_Addresses):
        return self.swapper_contract.functions.getWalletTokenInformations(
            User,
            Token_Addresses
        ).call()

    def fetchEthWalletInfos(self, User):
        return self.w3.eth.get_balance(User), self.fetchCurrentPrice(self.WBNB)
    
    def fetchOutputAmount(self, Input_Amount, Input_Address, Output_Address):
        return self.swapper_contract.functions.getOutputfromTokentoToken(
            Web3.toChecksumAddress(Input_Address),
            Web3.toChecksumAddress(Output_Address),
            Input_Amount
        ).call()

    def checkTokenTax(self, Token_Address):
        tokenInfos = self.swapper_contract.functions.getTokenInformations(Token_Address).call()
        buy_tax = round((tokenInfos[0] - tokenInfos[1]) / tokenInfos[0] * 100 ,2) 
        sell_tax = round((tokenInfos[2] - tokenInfos[3]) / tokenInfos[2] * 100 ,2)
        if tokenInfos[4] and tokenInfos[6] == True:
            Successfull = True
        else:
            Successfull = False
        return Successfull, buy_tax, sell_tax


    def checkAlloanceSwapper(self, Token_Address, User):
        tc = self.setup_token(Token_Address)
        return tc.functions.allowance(User, self.swapper_address).call()


    def createSignedTransactionApproveMAX(self, User, Token_Address, gasPrice,  privKey):
        try:
            t = self.setup_token(Token_Address)
            tx = t.functions.approve(
                self.swapper_address,
                int(10**64)
                ).buildTransaction({
                    'from': User, 
                    'gasPrice': int(gasPrice* 10**9),
                    'nonce': self.w3.eth.getTransactionCount(User)
                    })
            gas =  int(self.estimateGas(tx))
            tx.update({ 'gas' : gas })
            Signed_TX = self.w3.eth.account.sign_transaction(tx, privKey)
            fee = int(gas) * int(gasPrice * 10**9)
            Estimate_Fee = Web3.fromWei(int(fee),'ether')
            status = True

        except Exception as e:
            return e , 0, 0

        return status, Estimate_Fee, Signed_TX

    def createSignedTransactionETHtoToken(self, User, Token_Address, Amount,  Slippage,  gasPrice,  privKey):
        try:
            uintAmount = Amount * 10**18 #ETH/BNB/BUSD
            tx = self.swapper_contract.functions.fromETHtoToken(
                User,
                Token_Address,
                int(Slippage)).buildTransaction({
                'from': User, 
                'gasPrice': int(gasPrice* 10**9),
                'nonce': self.w3.eth.getTransactionCount(User), 
                'value': int(uintAmount)
                })
            gas =  int(self.estimateGas(tx))
            tx.update({ 'gas' : gas })
            Signed_TX = self.w3.eth.account.sign_transaction(tx, privKey)
            fee = int(gas) * int(gasPrice * 10**9)
            Estimate_Fee = Web3.fromWei(int(fee),'ether')
            status = True

        except Exception as e:
            return e , 0, 0

        return status, Estimate_Fee, Signed_TX


    def createSignedTransactionTokentoToken(self, User, Token_Address_IN, Token_Address_OUT, Amount, Decimals,  Slippage,  gasPrice,  privKey):
        try:
            uintAmount = Amount * 10**Decimals #ETH/BNB/BUSD
            tx = self.swapper_contract.functions.fromTokentoToken(
                User,
                Token_Address_IN,
                Token_Address_OUT,
                int(uintAmount),
                int(Slippage)).buildTransaction({
                'from': User, 
                'gasPrice': int(gasPrice* 10**9),
                'nonce': self.w3.eth.getTransactionCount(User), 
                })
            gas =  int(self.estimateGas(tx))
            tx.update({ 'gas' : gas })
            Signed_TX = self.w3.eth.account.sign_transaction(tx, privKey)
            fee = int(gas) * int(gasPrice * 10**9)
            Estimate_Fee = Web3.fromWei(int(fee),'ether')
            status = True

        except Exception as e:
            return e , 0, 0
        return status, Estimate_Fee, Signed_TX


    def createSignedTransactionTokentoETH(self, User, Token_Address, Amount, Decimals,  Slippage,  gasPrice,  privKey):
        try:
            uintAmount = Amount*10**Decimals #ETH/BNB/BUSD
            tx = self.swapper_contract.functions.fromTokentoETH(
                User,
                Token_Address,
                int(uintAmount),
                int(Slippage)).buildTransaction({
                'from': User, 
                'gasPrice': int(gasPrice* 10**9),
                'nonce': self.w3.eth.getTransactionCount(User), 
                })
            gas =  int(self.estimateGas(tx))
            tx.update({ 'gas' : gas })
            Signed_TX = self.w3.eth.account.sign_transaction(tx, privKey)
            fee = int(gas) * int(gasPrice * 10**9)
            Estimate_Fee = Web3.fromWei(int(fee),'ether')
            status = True
        except Exception as e:
            return e , 0, 0

        return status, Estimate_Fee, Signed_TX