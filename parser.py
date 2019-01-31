from lxml import html
import re

class Parser():
    
    def __init__(self, rawhtml):
        '''
        Ctor
        '''
        self.htmltree = html.fromstring(rawhtml)
        
    def get_headers(self):
        '''
        Method to extract the table headers
        '''
        results = self.htmltree.xpath("//td[@class='carta-table-header']/text()")
        headers = []
        for r in results:
            if not r in headers:
                headers.append(r)
        return headers

    def get_datatable_inputslevels(self):
        '''
        Method to extract values inside the whole table data
        '''
        return self.htmltree.xpath("//table[@class='carta-table']/tr[@class='carta-table-row']/td/b/text() | \
                                    //table[@class='carta-table']/tr[@class='carta-table-row tablesorter-childRow']/td/text() | \
                                    //table[@class='carta-table']/tr[@class='carta-table-row tablesorter-childRow']/td/img/@alt")

    def get_datatable_advantages(self):
        '''
        Method to extract values inside the whole table data
        '''
        return self.htmltree.xpath("//table[@class='carta-table']/tr[@class='carta-table-row']/td/b/text() | \
                                    //table[@class='carta-table']/tr[@class='carta-table-row']/td/text() | \
                                    //table[@class='carta-table']/tr[@class='carta-table-row']/td/img/@alt")

    def get_datatable_movenames(self):
        '''
        '''
        return self.htmltree.xpath("//table[@class='carta-table']/tr[@class='carta-table-row']/td/b/text()")

    def get_advantages(self):
        '''
        Return advantages values
        '''
        movenames = self.get_datatable_movenames()
        raw_advantages = self.get_datatable_advantages()
        raw_advantages.pop(0)

        res = []
        infos = []

        while len(raw_advantages) > 0:
            value = raw_advantages.pop(0)
            if value not in movenames:
                value = re.sub(' + ', '', value) # Formatting
                value = re.sub('\n', ' ', value) # Formatting
                infos.append(value)
            else:
                res.append(infos.copy())
                infos.clear()
        
        res.append(infos.copy())
        return res

    def get_inputslevels(self):
        '''
        Return inputs levels values
        '''
        movenames = self.get_datatable_movenames()
        raw_inputslevels = self.get_datatable_inputslevels()
        raw_inputslevels.pop(0)

        res = []
        infos = []

        while len(raw_inputslevels) > 0:
            value = raw_inputslevels.pop(0)
            if value not in movenames:
                value = re.sub(' + ', '', value) # Formatting
                value = re.sub('\n', ' ', value) # Formatting
                infos.append(value)
            else:
                res.append(infos.copy())
                infos.clear()
        
        res.append(infos.copy())
        return res
    
    def print_framedata(self):
        '''
        Prints the whole framedata
        '''
        movenames = self.get_datatable_movenames()
        advantages = self.get_advantages()
        inputslevels = self.get_inputslevels()

        print("{")
        print("\"Name\": \"Ivy\",")
        print("\"Attacks\": [")


        for i in range(len(movenames)):
            print("{")
            print("\"Name\": \"" + movenames[i] + "\",")
            print("\"Input\": \""+''.join(inputslevels[i])+"\",")
            print("\"Levels\": [],")
            print("\"Properties\": [],")
            
            try:
                print("\"Impact\":" + advantages[i][0] + ",")
            except:
                print("\"Impact\": 0,")

            try:
                print("\"Damage\":" + advantages[i][1] + ",")
            except:
                print("\"Damage\": 0,")

            print("\"Chip\": 0,")

            try:
                print("\"AdvOnGuard\":" + advantages[i][2] + ",")
            except:
                print("\"AdvOnGuard\": 0,")

            try:
                print("\"AdvOnHit\":" + advantages[i][3] + ",")
            except:
                print("\"AdvOnHit\": 0,")

            try:
                print("\"AdvOnCounterHit\":" + advantages[i][4] + ",")
            except:
                print("\"AdvOnCounterHit\": 0,")

            print("\"GuardBreak\": 0,")
            print("\"Info\": \"\"")
            print("},")

        print("]")
        print("}")

        # '''
        # Method to extract the whole frame data
        # '''
        # tabledata = self.get_datatable_advantages()
        # headers = self.get_headers()
        # framedata = []

        # while len(tabledata) >= len(headers):
        #     command = []
        #     for h in headers:
        #         value = tabledata.pop(0)
        #         value = re.sub(' + ', '', value) # Formatting
        #         value = re.sub('\n', ' ', value) # Formatting
        #         command.append(value)
        #     print(command)
        #     framedata.append(command)

        # return framedata
