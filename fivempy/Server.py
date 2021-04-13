import requests

class Server:

    def __init__(self, ip):
        self.ip = ip

        
        self.player_count = 0
        self.player_list = []
        self.player_max = 0
        
        
        self.info = {}
        self.players = {}
        self.dynamic = {}

    def initialize(self):
        self.get_info()
        self.get_players()
        self.get_dynamic()
        
        self.get_player_count()
        self.get_player_list()
        self.get_player_max()

    def get_info(self):
        try:
            r = requests.get(f'http://{self.ip}/info.json')
            r.raise_for_status()
            self.info = r.json()
            return self.info
        except:
            return('Server is offline or incorrect IP')
    
    def get_players(self):
        try:
            r = requests.get(f'http://{self.ip}/players.json')
            r.raise_for_status()
            self.players = r.json()
            return self.players
        except:
            return('Server is offline or incorrect IP')

    def get_dynamic(self):
        try:
            r = requests.get(f'http://{self.ip}/dynamic.json')
            r.raise_for_status()
            self.dynamic = r.json()
            return self.dynamic
        except:
            return('Server is offline or incorrect IP')


    def get_player_count(self):
        try:
            r = requests.get(f'http://{self.ip}/players.json')
            r.raise_for_status()
            self.player_count = len(r.json())
            return self.player_count
        except:
            try:
                r = requests.get(f'http://{self.ip}/dynamic.json')
                r.raise_for_status()
                self.player_count = r.json().get('clients')
                return self.player_count
            except:
                return('Server is offline or incorrect IP')

    def get_player_max(self):
        try:
            r = requests.get(f'http://{self.ip}/info.json')
            r.raise_for_status()
            self.player_max = r.json().get('vars').get('sv_maxClients')
            return self.player_max
        except:
            try:
                r = requests.get(f'http://{self.ip}/dynamic.json')
                r.raise_for_status()
                self.player_max = r.json().get('sv_maxclients')
                return self.player_max
            except:
                return('Server is offline or incorrect IP')
    
    def get_player_list(self):
        try:
            r = requests.get(f'http://{self.ip}/players.json')
            r.raise_for_status()
            player_list = []
            for i in range(0,len(r.json())):
                player_list.append(r.json()[i]['name'])    
            self.player_list = player_list
            return self.player_list
        except:
            return('Server is offline or incorrect IP')