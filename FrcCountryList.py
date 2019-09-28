import requests

class FrcCountryList:

    baseURL = "https://www.thebluealliance.com/api/v3/"
    header = {'X-TBA-Auth-Key': 'BRa4UYcX7J2Q4YK8cUHYprsXQAWk8hd9WKUleE1ADEwka3lCujsuWo9KwFKCuQRl'}

    @classmethod
    def getTBA(self, url):
        headers = self.header
        request = requests.get(self.baseURL + url, headers).json()
        return request

    @classmethod
    def getTeams(self):
        teams = []
        currentPage = 0
        currentTeams = self.getTBA("teams/" + str(currentPage) + "")
        for team in currentTeams:
            teams.append(team)
        while currentTeams != []:
            print('Page: ' + str(currentPage))
            currentPage += 1
            currentTeams = self.getTBA("teams/" + str(currentPage) + "")
            for team in currentTeams:
                teams.append(team)
        print('The amount of teams are ' + str(len(teams)))
        return teams

    @classmethod
    def getAliveTeams(self):
        allAliveTeams = []
        count = 0
        allTeams = self.getTeams()
        # print('The amount of allTeams are ' + str(len(allTeams)))
        for team in allTeams:
            try:
                if self.getTBA("team/" + team['key'] + "/years_participated")[-1] == 2019 or 2020:
                    allAliveTeams.append(team)
                    print(team['key'] + ' Team ---> ' + team['country'])
                    count += 1
                # update the result structure

            except:
            #    print('ERROR!')
                pass
        print('The List of teams is ' + str(len(allAliveTeams)) + ' teams long')
        # print('The Count of teams is ' + str(otalTeams))
        return allAliveTeams

    @classmethod
    def constructCountryCount(self, totalTeams):
        w, h = 2, 51;
        countryCountArray = [[0 for x in range(w)] for y in range(h)]
        storedArrayLine = -1
        print(countryCountArray)
        for team in totalTeams:
            found = False
            for i in range(0, 50):
                # print('len1) >' + str(team['country']) + '##len2) >' + str(countryCountArray[i][0]))
                # print(team['country'] + 'is at ' + str(countryCountArray[i][0]))
                if team['country'] == countryCountArray[i][0]:
                    countryCountArray[i][1] += 1
                    found = True
                    break
                # print('inside.Else) >')
            if found == False:
                storedArrayLine += 1
                countryCountArray[storedArrayLine][0] = team['country']
                countryCountArray[storedArrayLine][1] = 1

        return countryCountArray

        # Look at country in array list and look for existing

    @classmethod
    def printArray(self, array):
        print(array)
        for i in range(0, 48):
            print(str(array[i][0]) + '    ' + str(array[i][1]))


temp = FrcCountryList
teamList = temp.getAliveTeams()
results = temp.constructCountryCount(teamList)
temp.printArray(results)
print('exist gracefully')