import pandas as pd
from encoder import coder
import pickle
import getpass

class PasswordVault():
    def __init__(self):
        self.encoder = coder()
        f = open('./lib/pass.pkl', 'rb')
        try:
            self.pframe = pickle.load(f)
            if not self.__authenticate():
                raise Exception('You must authenticate')
        except (pickle.UnpicklingError, EOFError) as e:
            self.pframe = pd.DataFrame(columns = ['site', 'username', 'password'])
            if not self.__authenticate():
                raise Exception('You must authenticate')

    def __authenticate(self):
        m = self.encoder.encode('MASTER')
        try:
            r = self.pframe.loc[self.pframe['site'] == m]
            p = self.encoder.decode(r['password'][0])
        except IndexError:
            self.newPassword('MASTER', 'admin', input('Enter a new master password: '))

        if getpass.getpass('Enter the master password: ') != p:
            return False
        else:
            return True


    def newPassword(self, site, user, password):
        site = self.encoder.encode(site)
        user = self.encoder.encode(user)
        password = self.encoder.encode(password)
        d = {'site': site, 'username': user, 'password': password}
        if site not in self.pframe['site']:
            self.pframe= self.pframe.append(d, ignore_index = True)
        print('Added new password.')
        self.saveFrame()

    def updatePassword(self, site):
        #find password for site and update it
        user = input(f"Enter your username for {site}: ")
        password = input(f"Enter your new password: ")
        site = self.encoder.encode(site)
        user = self.encoder.encode(user)
        password = self.encoder.encode(password)
        try:
            self.pframe.loc[self.pframe['site'] == site, 'username'] = user
            self.pframe.loc[self.pframe['site'] == site, 'password'] = password
        except:
            print(f'Could not find login info for {site}.')
            return
        print("Updated password.")
        self.saveFrame()

    def findPassword(self, site):
        site = self.encoder.encode(site)
        r = self.pframe.loc[self.pframe['site'] == site]
        if len(r) ==0:
            print(f'Could not find login info for {site}.')
            return
        print('SITE: ' + self.encoder.decode(list(r['site'])[0]))
        print('USER: ' + self.encoder.decode(list(r['username'])[0]))
        print('PASS: ' + self.encoder.decode(list(r['password'])[0]))

    def saveFrame(self):
        f = open('./lib/pass.pkl', 'wb')
        pickle.dump(self.pframe, f)

    def listAll(self):
        for i in range(len(self.pframe)):
            print(self.encoder.decode(self.pframe['site'][i]), self.encoder.decode(self.pframe['username'][i]), self.encoder.decode(self.pframe['password'][i]))

    def deleteAll(self):
        m = self.encoder.encode('MASTER')
        self.pframe = self.pframe.loc[self.pframe['site'] == m]
        self.saveFrame()

        
p = PasswordVault()
accept = ['newPass', 'updateP', 'findPas', 'listAll', 'deleteA']
while True:
    print('-'*20)
    print('''Enter one of the following commands:\n
    newPassword(website, username, password)\n
    updatePassword(website)\n
    findPassword(website)\n
    listAll()\n
    deleteAll()''')
    s = input(': ')
    if s[:7] in accept:
        s = f"p.{s}"
        eval(s)
    else:
        print(s[:7])
        print('Enter a valid command...')
