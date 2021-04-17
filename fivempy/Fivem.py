import requests


class Fivem:

    def __init__(self):
        self.status = {}

        # Game services
        self.cnl_status = {}
        self.policy_status = {}
        self.keymaster_status = {}

        # Web services
        self.forum_status = {}
        self.serverlist_status = {}
        self.runtime_status = {}

        self.initialize()

    def initialize(self):
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
