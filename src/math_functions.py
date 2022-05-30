class Math_UI_Functions():
    def formatAndRound(self, flo):
        i, f = divmod(flo, 1)
        if i >= 1:
            return round(flo, 2)
        elif i < 1:
            l = 1
            sf = str(0.01)
            while True:
                if float(f) < float(sf):
                    l += 1
                    sf = str(sf[:-1]) + str("01")
                else:
                    return round(flo, l +3)

    def getDecimals(self, flo):
        i, f = divmod(flo, 1)
        if i >= 1:
            return 2
        elif i < 1:
            l = 1
            sf = str(0.01)
            while True:
                if float(f) < float(sf):
                    l += 1
                    sf = str(sf[:-1]) + str("01")
                else:
                    return l +3

    def FloatToCleanSting(self, flo):
        Decimals = self.getDecimals(flo)
        clean = "{" + f":.{Decimals}f" + "}"
        str_flo = str(clean).format(flo)
        if float(str(str_flo)) == float(0):
            return str(0.00)
        else:
            return str_flo

    def get_change(self, current, previous):
        if current == previous:
            return 0
        if current > previous:
            try:
                return +(abs(current - previous) / previous) * 100.0 
            except ZeroDivisionError:
                return float('inf')
        elif current < previous:
            try:
                return -(abs(current - previous) / previous) * 100.0 
            except ZeroDivisionError:
                return float('inf')



