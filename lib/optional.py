class Optional:
    def ask_use(self, component):
        res = input("\n\nWould you like to add {} ? (y/n) [n] ".format( component ))
        return True if res == "y" else False