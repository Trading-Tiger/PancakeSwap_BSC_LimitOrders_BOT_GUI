from imports import *


class Global_Settings():
    def __init__(self):
        self.config_Path = "./configs/global_config.json"
        self.LoadSettings()
        

    def Loadglobal_config(self):
        with open(self.config_Path) as gc:
            gcj = json.load(gc)
        return gcj


    def LoadSettings(self):
        current_config = self.Loadglobal_config()
        self.candleTimeMin = current_config["CandleTimeMin"]
        self.candleHistory = current_config["CandleHistory"]
        self.MA20 = current_config["MA20"]
        self.VOLUME = current_config["VOLUME"]
        self.B_TOKEN = current_config["BASE_TOKEN"]
        self.OT = current_config["ORDER_TYPE"]
        self.BM = current_config["MENU_BUTTON"]
        self.O_ONLINE = current_config["ORDERS_ONLINE"]
    

    def changeGlobalSetting(self, settings, newValue):
        with open(self.config_Path, 'r+') as f:
            data = json.load(f)
            data[settings] = newValue
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 
        self.LoadSettings()    


class User_Settings():
    def __init__(self):
        self.config_Path = "./configs/user_config.json"
        self.LoadSettings()
        

    def Loadglobal_config(self):
        with open(self.config_Path) as gc:
            gcj = json.load(gc)
        return gcj


    def LoadSettings(self):
        current_config = self.Loadglobal_config()
        self.PROVIDER = current_config["PROVIDER"]
        self.SLIPPAGE = current_config["SLIPPAGE"]
        self.OQI = current_config["ORDER_QUERY_INTERVAL"]
        self.SQI = current_config["SNIPER_QUERY_INTERVAL"]
        self.AUTOSTART_ORDERS = current_config["AUTOSTART_ORDERS"]
        self.AUTOSTART_SNIPER = current_config["AUTOSTART_SNIPER"]
        self.WAIT_TX_STATUS = current_config["WAIT_TX_STATUS"]
        self.ADDRESS = Web3.toChecksumAddress(current_config["ADDRESS"])
        self.GAS = current_config["GAS_GWEI"]
        self.TOKEN_LIST = []
        self.PRIVKEY = current_config['SECRETKEY']
        for i in current_config["TOKEN_LIST"]:
            self.TOKEN_LIST.append(self.SafeAddress(i))

    def SafeAddress(self, address):
        return Web3.toChecksumAddress(address)

    def changeUserSetting(self, settings, newValue):
        with open(self.config_Path, 'r+') as f:
            data = json.load(f)
            data[settings] = newValue
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 
        self.LoadSettings()




class LimitOrders_Settings():
    def __init__(self):
        self.config_Path = "./orders/open_orders.json"
        self.FailTX_Path =  "./orders/fail_orders.json"
        self.SuccessTX_Path =  "./orders/success_orders.json"
        self.LoadOrders()
        
    def Loadglobal_config(self):
        with open(self.config_Path) as gc:
            gcj = json.load(gc)
        return gcj


    def LoadOrders(self):
        self.ORDERS = self.Loadglobal_config()


    def addNewOrder(self, newOrder):
        with open(self.config_Path, 'r+') as f:
            data = json.load(f)
            data.append(newOrder) 
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 
        self.LoadOrders() 


    def deleteOrder(self, OrderID):
        with open(self.config_Path, 'r+') as f:
            data = json.load(f)
            for i in range(len(data)):
                i -= 1
                if str(data[i]["ID"]) == str(OrderID):
                    del data[i]
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                else:
                    pass
        self.LoadOrders()


    def addFailTX(self, Order, tx):
        with open(self.FailTX_Path, 'r+') as f:
            data = json.load(f)
            Order.update({"TRANSACTION_HASH": tx})
            data.append(Order)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()


    def addSuccessTX(self, Order, tx):
        with open(self.SuccessTX_Path, 'r+') as f:
            data = json.load(f)
            Order.update({"TRANSACTION_HASH": tx})
            data.append(Order)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

