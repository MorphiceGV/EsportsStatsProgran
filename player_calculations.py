import requests
import simplejson as json
import json

apikey = 'API KEY WILL NOT BE UPLOADED TO GITHUB'
Selected = ["",False]
TeamA = []
TeamB = []
PlayerPool = []

'''def PlayerInfo(a):
    global apikey

    ########################################################################################################################################
    ##get request for pulling the general user info
    UserRequest = requests.get(
        "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(a, apikey))

    # sets request output as text and to the json_object_string
    json_object_string = UserRequest.text

    # this sets the request output as text and to the json_object_string
    json_object = json.loads(json_object_string)

    # lets you call value from above, pick a certain value and assign it to a new var
    SummonerNum = (json_object["id"])

    ######################################################################################################################################
    ## Ranked request for summoner
    UserRankedRequest = requests.get(
        "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}".format(SummonerNum, apikey))

    json_object_string2 = UserRankedRequest.text
    json_object2 = json.loads(json_object_string2)

    if json_object2[0]["queueType"] == "RANKED_FLEX_SR":
        s = 1
    else:
        s = 0
        ######################################################################################################################################
    if json_object2[s]["summonerId"] == SummonerNum:
        print(
            "{} is ranked as {} " "{} in {} with {} LP".format(json_object2[s]["summonerName"], json_object2[s]["tier"],
                                                               json_object2[s]["rank"], json_object2[s]["queueType"],
                                                               json_object2[s]["leaguePoints"]))
        print("{} has {} wins and {} losses".format(json_object2[s]["summonerName"], json_object2[s]["wins"],
                                                    json_object2[s]["losses"]))'''
'''
def createNull(a):
    test = [0]
    test[0] = {"summonerName": a,"tier":"UNRANKED","rank":"UNRANKED","queueType":"UNRANKED","leaguePoints":0,"wins":0,"losses":0}
    return test[0]
'''
def createNull(a):
    test = {"summonerName": a,"tier":"UNRANKED","rank":"UNRANKED","queueType":"UNRANKED","leaguePoints":0,"wins":0,"losses":0}
    return test

'''
def createPlayer(a):
    global apikey
    UserRequest = requests.get(
        "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(a, apikey))
    json_object_string = UserRequest.text
    json_object = json.loads(json_object_string)
    SummonerNum = (json_object["id"])
    UserRankedRequest = requests.get(
        "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}".format(SummonerNum, apikey))

    json_object_string2 = UserRankedRequest.text
    json_object2 = json.loads(json_object_string2)

    try:
        if json_object2[1]["queueType"] == "RANKED_FLEX_SR":
            s = 0
        else:
            s = 1
    except IndexError:
        try:
            if json_object2[0]["queueType"] == "RANKED_FLEX_SR":
                s = 0
            else:
                s = 0
        except IndexError:
            return createNull(a)


    return json_object2[s]
'''
def createPlayer(a):
    global apikey
    UserRequest = requests.get(
        "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(a, apikey))
    json_object_string = UserRequest.text
    json_object = json.loads(json_object_string)
    SummonerNum = (json_object["id"])
    UserRankedRequest = requests.get(
        "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}".format(SummonerNum, apikey))

    json_object_string2 = UserRankedRequest.text
    json_object2 = json.loads(json_object_string2)
    output = {}
    try:
        if json_object2[1]["queueType"] == "RANKED_FLEX_SR":
            output = json_object2[0]
        else:
            output = json_object2[1]
    except IndexError:
        try:
            if json_object2[0]["queueType"] == "RANKED_FLEX_SR":
                output = json_object2[0]
            else:
                output = json_object2[0]
        except IndexError:
            return createNull(a)


    return output

def GetType(json_object2):
    return json_object2["queueType"]

def PlayerInfo(json_object2):

    return [json_object2["summonerName"], json_object2["tier"], json_object2["rank"], json_object2["leaguePoints"],
            json_object2["wins"], json_object2["losses"]]
    '''
    return {"summonerName": json_object2["summonerName"], "tier": json_object2["tier"], "rank": json_object2["rank"],
     "queueType": json_object2["queueType"], "leaguePoints": json_object2["leaguePoints"], "wins": json_object2["wins"],
     "losses": json_object2["losses"]}
    '''

    '''
    print("{} is ranked as {} " "{} in {} with {} LP".format(json_object2["summonerName"], json_object2["tier"],
                                                               json_object2["rank"], json_object2["queueType"],
                                                               json_object2["leaguePoints"]))
    print("{} has {} wins and {} losses".format(json_object2["summonerName"], json_object2["wins"],
                                                    json_object2["losses"]))
    '''
def playerRank(json_object2):

    return json_object2["tier"]+" "+json_object2["rank"]

def tierNumber(i):
    switcher = {
        "UNRANKED UNRANKED": int(0),
        "IRON I": int(-65),
        "IRON II": int(-80),
        "IRON III": int(-90),
        "IRON IV": int(-100),
        "BRONZE I": int(-22),
        "BRONZE II": int(-30),
        "BRONZE III": int(-36),
        "BRONZE IV": int(-45),
        "SILVER I": int(-1),
        "SILVER II": int(-6),
        "SILVER III": int(-11),
        "SILVER IV": int(-17),
        "GOLD I": int(10),
        "GOLD II": int(6),
        "GOLD III": int(3),
        "GOLD IV": int(1),
        "PLATINUM I": int(24),
        "PLATINUM II": int(20),
        "PLATINUM III": int(18),
        "PLATINUM IV": int(12),
        "DIAMOND I": int(60),
        "DIAMOND II": int(52),
        "DIAMOND III": int(43),
        "DIAMOND IV": int(33),
        "MASTER I": int(80),
        "GRAND MASTER I": int(90),
        "CHALLENGER I": int(100),
    }
    return switcher.get(i, "Invalid rank")

def get_emblem_image(tier):
    if tier == 'BRONZE':
        return 'imgs/ranked-emblems/Emblem_Bronze.png'
    elif tier == 'CHALLENGER':
        return 'imgs/ranked-emblems/Emblem_Challenger.png'
    elif tier == 'DIAMOND':
        return 'imgs/ranked-emblems/Emblem_Diamond.png'
    elif tier == 'GOLD':
        return 'imgs/ranked-emblems/Emblem_Gold.png'
    elif tier == 'GRANDMASTER':
        return 'imgs/ranked-emblems/Emblem_Grandmaster.png'
    elif tier == 'IRON':
        return 'imgs/ranked-emblems/Emblem_Iron.png'
    elif tier == 'MASTER':
        return 'imgs/ranked-emblems/Emblem_Master.png'
    elif tier == 'PLATINUM':
        return 'imgs/ranked-emblems/Emblem_Platinum.png'
    elif tier == 'SILVER':
        return 'imgs/ranked-emblems/Emblem_Silver.png'
    else:
        return 'imgs/esportslogo.jpg'

def getName(json_object2):
    a = json_object2['summonerName']
    return a

def FetchPlayerNumericle(json_object2):
    '''if json_object2[s]["summonerId"] == SummonerNum:
            print(
                "{} is ranked as {} " "{} with {} LP".format(json_object2[s]["summonerName"], json_object2[s]["tier"],
                                                                   json_object2[s]["rank"],
                                                                   json_object2[s]["leaguePoints"]))
            print("{} has {} wins and {} losses".format(json_object2[s]["summonerName"], json_object2[s]["wins"],
                                                        json_object2[s]["losses"]))'''

    return tierNumber(json_object2["tier"] + " " + json_object2["rank"])

def teamOverAll(a):
    overallpoints = 0
    for i in range(len(a)):
        overallpoints = tierNumber(playerRank(a[i]))+overallpoints
    return overallpoints

def teamAndRank(a):
    for i in range(len(a)):
        PlayerInfo(a[i])
    print("Over All team Rank is "+str(teamOverAll(a)))

def comparePlayers(a, b):
    if GetType(a) == GetType(b):
        aFetch = FetchPlayerNumericle(a)
        bFetch = FetchPlayerNumericle(b)
        if aFetch < bFetch:
            print(getName(a) + " is weaker then " + getName(b) + " as " + str(aFetch) + " < " + str(bFetch))
        else:
            if aFetch > bFetch:
                print(getName(a) + " is Stronger then " + getName(b) + " as " + str(aFetch) + " > " + str(bFetch))
            else:
                if aFetch == bFetch:
                    print("player " + getName(a) + " and player " + getName(b) + " are equal to eachother")
                else:
                    print("This sudo code did not work")
                    ##player1 = input("type the first players name here")
    else:
        print("Both Players Are not being compared Equally. Please try comparing Different Players")


def RecommendPlayer(a, b, c, team):
    if len(a) < 5:
        a = teamOverAll(a)
        b = teamOverAll(b)
        if len(c) >= 1:
            if a == b:
                return getName(c[0]) + " " + playerRank(c[0]) + " is recommended for " + team + " team."
            if a > b:
                reference = -9999
                referencei = 0
                for i in range(len(c)):
                    if tierNumber(playerRank(c[i])) + a <= b:
                        if tierNumber(playerRank(c[i])) + a >= reference:
                            reference = tierNumber(playerRank(c[i])) + a
                            referencei = i
                        if tierNumber(playerRank(c[i])) + a == b:
                            referencei = i
                            return getName(c[i]) + " " + playerRank(c[i]) + " is recommended for " + team + " team."
                if tierNumber(playerRank(c[referencei])) + a > b:
                    pass
                else:
                    return getName(c[referencei])+" "+playerRank(c[referencei])+" is recommended for " + team + " team."
            if a < b:
                reference = 9999
                referencei = 0
                for i in range(len(c)):
                    if tierNumber(playerRank(c[i])) + a >= b:
                        if tierNumber(playerRank(c[i])) + a <= reference:
                            reference = tierNumber(playerRank(c[i])) + a
                            referencei = i
                        if tierNumber(playerRank(c[i])) + a == b:
                            referencei = i
                            return getName(c[i])+" "+playerRank(c[i])+" is recommended for " + team + " team."
                if tierNumber(playerRank(c[referencei])) + a < b:
                    pass
                else:
                    return getName(c[referencei])+" "+playerRank(c[referencei])+" is recommended for " + team + " team."

            reference1 = a
            reference2 = b

            referenceLower = -9999
            referenceUpper = 9999
            referencei1 = 0
            referencei2 = 0
            average = (a + b) / 2
            if a > b:
                averageArange = (reference2 + average) / 2
                averageBrange = (reference1 + average) / 2
            if b > a:
                averageArange = (reference1 + average) / 2
                averageBrange = (reference2 + average) / 2
            for i in range(len(c)):
                if reference1 + tierNumber(playerRank(c[i])) >= averageArange and tierNumber(playerRank(c[i])) + reference1 <= averageBrange:
                    if averageArange <= tierNumber(playerRank(c[i])) + reference1 <= average and tierNumber(playerRank(c[
                        i])) + reference1 > referenceLower:
                        referenceLower = tierNumber(playerRank(c[i])) + reference1
                        referencei1 = i

                    if averageBrange >= tierNumber(playerRank(c[i])) + reference1 >= average and tierNumber(playerRank(c[
                        i])) + reference1 < referenceUpper:
                        referenceUpper = tierNumber(playerRank(c[i])) + reference1
                        referencei2 = i

                    if tierNumber(playerRank(c[i])) + reference1 == average:
                        return getName(c[i])+" "+playerRank(c[i])+" is recommended for " + team + " team."

            if referenceLower == -9999:
                referenceLower = 0
            if referenceUpper == 9999:
                referenceUpper = average * 2

            referenceLower = average - referenceLower
            referenceUpper = referenceUpper - average
            referencei = referencei1
            if referenceLower < referenceUpper:
                referencei = referencei1
            if referenceLower > referenceUpper:
                referencei = referencei2
            if referenceLower == average and referenceUpper == average:
                return getName(c[0])+" "+playerRank(c[0])+" is recommended for " + team + " team."

            return getName(c[referencei])+" "+playerRank(c[referencei])+" is recommended for " + team + " team."
        else:
            return "There are no players in the queue currently."
    else:
        return "Team is already full."

def PlaceRecommend(a, b, c, team):
    a = teamOverAll(a)
    b = teamOverAll(b)
    if a == b:
        return c[0]
    if a > b:
        reference = -9999
        referencei = 0
        for i in range(len(c)):
            if tierNumber(playerRank(c[i])) + a <= b:
                if tierNumber(playerRank(c[i])) + a >= reference:
                    reference = tierNumber(playerRank(c[i])) + a
                    referencei = i
                if tierNumber(playerRank(c[i])) + a == b:
                    referencei = i
                    return c[i]
        if tierNumber(playerRank(c[referencei])) + a > b:
            pass
        else:
            return c[referencei]
    if a < b:
        reference = 9999
        referencei = 0
        for i in range(len(c)):
            if tierNumber(playerRank(c[i])) + a >= b:
                if tierNumber(playerRank(c[i])) + a <= reference:
                    reference = tierNumber(playerRank(c[i])) + a
                    referencei = i
                if tierNumber(playerRank(c[i])) + a == b:
                    referencei = i
                    return c[i]
        if tierNumber(playerRank(c[referencei])) + a < b:
            pass
        else:
            return c[referencei]

    reference1 = a
    reference2 = b

    referenceLower = -9999
    referenceUpper = 9999
    referencei1 = 0
    referencei2 = 0
    average = (a + b) / 2
    if a > b:
        averageArange = (reference2 + average) / 2
        averageBrange = (reference1 + average) / 2
    if b > a:
        averageArange = (reference1 + average) / 2
        averageBrange = (reference2 + average) / 2
    for i in range(len(c)):
        if reference1 + tierNumber(playerRank(c[i])) >= averageArange and tierNumber(playerRank(c[i])) + reference1 <= averageBrange:
            if averageArange <= tierNumber(playerRank(c[i])) + reference1 <= average and tierNumber(playerRank(c[
                i])) + reference1 > referenceLower:
                referenceLower = tierNumber(playerRank(c[i])) + reference1
                referencei1 = i

            if averageBrange >= tierNumber(playerRank(c[i])) + reference1 >= average and tierNumber(playerRank(c[
                i])) + reference1 < referenceUpper:
                referenceUpper = tierNumber(playerRank(c[i])) + reference1
                referencei2 = i

            if tierNumber(playerRank(c[i])) + reference1 == average:
                return c[i]

    if referenceLower == -9999:
        referenceLower = 0
    if referenceUpper == 9999:
        referenceUpper = average * 2

    referenceLower = average - referenceLower
    referenceUpper = referenceUpper - average
    referencei = referencei1
    if referenceLower < referenceUpper:
        referencei = referencei1
    if referenceLower > referenceUpper:
        referencei = referencei2
    if referenceLower == average and referenceUpper == average:
        return c[0]

    return c[referencei]

def Select(a,b):
    global Selected
    Selected[0] = a
    Selected[1] = b
def removeTeam(a,team):
    for i in team:
        if getName(a) == getName(i):
            team.remove(i)
def movetoTeam(a):
    #global Selected
    global TeamA
    global TeamB
    global PlayerPool

    if a == "P":
        PlayerPool.append(Selected[0])
        if Selected[1]:
            removeTeam(Selected[0], Selected[1])
        Select(Selected[0], PlayerPool)
    if a == "A":
        if len(TeamA) == 5:
            print("Team A is full")
            return "Team A is full"
        else:
            TeamA.append(Selected[0])
            removeTeam(Selected[0],Selected[1])
            Select(Selected[0],TeamA)
    if a == "B":
        if len(TeamB) == 5:
            print("Team B is full")
            return "Team B is full"
        else:
            TeamB.append(Selected[0])
            removeTeam(Selected[0], Selected[1])
            Select(Selected[0], TeamB)

def FullTB():
    if len(TeamA)+len(TeamB)+len(PlayerPool) >= 10:
        while len(TeamA)!= 5 or len(TeamB)!=5:
            if len(TeamA)>len(TeamB):
                a = PlaceRecommend(TeamB,TeamA,PlayerPool)
                Select(a,PlayerPool)
                movetoTeam("B")
            if len(TeamA)<len(TeamB):
                a = PlaceRecommend(TeamA,TeamB,PlayerPool)
                Select(a,PlayerPool)
                movetoTeam("A")
            if len(TeamA)==len(TeamB):
                a = PlaceRecommend(TeamB,TeamA,PlayerPool)
                Select(a,PlayerPool)
                movetoTeam("B")
    else:
        #print("Not Enough People Available to balance teams")
        return "Not Enough People Available to balance teams"

def ClearTeam():
    while len(TeamA)!=0:
        Select(TeamA[0],TeamA)
        movetoTeam("P")
    while len(TeamB)!=0:
        Select(TeamB[0],TeamB)
        movetoTeam("P")
'''
PlayerPool = [createPlayer("Morphice"), createPlayer("boxxybabee"), createPlayer("Christi"),
              createPlayer("CocoCookieDough"), createPlayer("Dog WITH A Blog"), createPlayer("Gamer183"),
              createPlayer("LT Pancakes") , createPlayer("MorningBacon"), createPlayer("OrdinaryGuyRyu")]
FullTB()
PlayerPool.append(createPlayer('mortem de caelo'))
PlayerPool.append(createPlayer('Kaybun'))
PlayerPool.append(createPlayer('killjoyyy28'))
FullTB()

teamAndRank(PlayerPool)
print("")
teamAndRank(TeamA)
print("")
teamAndRank(TeamB)
print("")
print("")

ClearTeam()
teamAndRank(PlayerPool)

print("")
teamAndRank(TeamA)
print("")
teamAndRank(TeamB)
print("")
print("")

Select(PlayerPool[0],PlayerPool)
movetoTeam("A")
Select(PlayerPool[0],PlayerPool)
movetoTeam("A")
Select(PlayerPool[0],PlayerPool)
movetoTeam("A")
Select(PlayerPool[0],PlayerPool)
movetoTeam("B")
Select(PlayerPool[0],PlayerPool)
movetoTeam("B")

teamAndRank(PlayerPool)
print("")
teamAndRank(TeamA)
print("")
teamAndRank(TeamB)
print("")
print("")
FullTB()
teamAndRank(PlayerPool)
print("")
teamAndRank(TeamA)
print("")
teamAndRank(TeamB)
print("")
print("")
playerPoolAverage = [playerPool[0] , createPlayer("Jaetro"), playerPool[2],createPlayer("kaybun"),createPlayer("Rush Fan Boi")]
teamA1 = [playerPoolAverage[1], createPlayer("Jakamin")]
teamB1 = [playerPoolAverage[3], createPlayer("Morphice")]
teamA2 = [createPlayer("LT Pancakes") , createPlayer("MorningBacon"), createPlayer("OrdinaryGuyRyu")]
teamB2 = [createPlayer("The Midget Cow") , createPlayer("Yoshi McCloud"), createPlayer("ZombieWaffle218")]
c = teamB1[1]
PlayerInfo(c)
d = teamB1[0]
PlayerInfo(d)
comparePlayers(c,d)

print(RecommendPlayer(teamA1,teamA2,playerPool))

print(teamOverAll(teamB2))
teamAndRank(teamB2)
a = createPlayer('mortem de caelo')
b = createPlayer("killjoyyy28")
c= createPlayer("morphice")
PlayerInfo(b)'''






