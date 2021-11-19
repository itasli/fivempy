import requests

class Server:

    def __init__(self, ip):
        self.ip = ip

    def get_info(self):
        try:
            r = requests.get(f'http://{self.ip}/info.json')
            r.raise_for_status()
            return r.json()
        except:
            return('Server is offline or incorrect IP')
    
    def get_players(self):
        try:
            r = requests.get(f'http://{self.ip}/players.json')
            r.raise_for_status()
            return r.json()
        except:
            return('Server is offline or incorrect IP')

    def get_dynamic(self):
        try:
            r = requests.get(f'http://{self.ip}/dynamic.json')
            r.raise_for_status()
            return r.json()
        except:
            return('Server is offline or incorrect IP')


    def get_player_count(self):
        try:
            r = requests.get(f'http://{self.ip}/players.json')
            r.raise_for_status()
            return len(r.json())
        except:
            try:
                r = requests.get(f'http://{self.ip}/dynamic.json')
                r.raise_for_status()
                return r.json().get('clients')
            except:
                return('Server is offline or incorrect IP')

    def get_max_player(self):
        try:
            r = requests.get(f'http://{self.ip}/info.json')
            r.raise_for_status()
            return r.json().get('vars').get('sv_maxClients')
        except:
            try:
                r = requests.get(f'http://{self.ip}/dynamic.json')
                r.raise_for_status()
                return r.json().get('sv_maxclients')
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
    
    def get_hostname(self):
        try:
            r = requests.get(f'http://{self.ip}/dynamic.json')
            r.raise_for_status()
            return r.json().get('hostname')
        except:
            try:
                r = requests.get(f'http://{self.ip}/info.json')
                r.raise_for_status()
                return r.json().get('vars').get('sv_projectName')
            except:
                return('Server is offline or incorrect IP')
    
    def get_ressource_list(self):
        try:
            r = requests.get(f'http://{self.ip}/info.json')
            r.raise_for_status()
            return r.json().get('resources')
        except:
            return('Server is offline or incorrect IP')

class Fivem:

    def __init__(self):
        try:
            r = requests.get('https://status.cfx.re/api/v2/summary.json')
            r.raise_for_status()
            r = r.json()

            self.status = r['status']

            # Game services
            self.cnl_status = r['components'][1]
            self.policy_status = r['components'][3]
            self.keymaster_status = r['components'][6]

            # Web services
            self.forum_status = r['components'][0]
            self.serverlist_status = r['components'][4]
            self.runtime_status = r['components'][7]
            return('Fetched all data')
        except:
            return('FiveM status page is offline !')

    def update(self):
        try:
            r = requests.get('https://status.cfx.re/api/v2/summary.json')
            r.raise_for_status()
            r = r.json()

            if r['status']['indicator'] != "none":
                self.initialize()
            return('Successfully updated')
        except:
            return('FiveM status page is offline !')