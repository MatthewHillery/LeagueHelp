#!/usr/bin/env python

import sys
import webbrowser

# file_name = "champion_list.txt"
# champion_list = getChampionList(file_name)

champion_list = ['aatrox', 'ahri', 'akali', 'alistar', 'amumu', 'anivia', 'annie', 'aphelios', 'ashe', 'aurelionsol', 'azir', 'bard', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'cassiopeia', "cho'gath", 'corki', 'darius', 'diana', 'dr.mundo', 'draven', 'ekko', 'elise', 'evelynn', 'ezreal', 'fiddlesticks', 'fiora', 'fizz', 'galio', 'gangplank', 'garen', 'gnar', 'gragas', 'graves', 'hecarim', 'heimerdinger', 'illaoi', 'irelia', 'ivern', 'janna', 'jarvaniv', 'jax', 'jayce', 'jhin', 'jinx', "kai'sa", 'kalista', 'karma', 'karthus', 'kassadin', 'katarina', 'kayle', 'kayn', 'kennen', "kha'zix", 'kindred', 'kled', "kog'maw", 'leblanc', 'leesin', 'leona', 'lissandra', 'lucian', 'lulu', 'lux', 'malphite', 'malzahar', 'maokai', 'masteryi',
                 'missfortune', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'neeko', 'nidalee', 'nocturne', 'nunuandwillump', 'olaf', 'orianna', 'ornn', 'pantheon', 'poppy', 'pyke', 'qiyana', 'quinn', 'rakan', 'rammus', "rek'sai", 'renekton', 'rengar', 'riven', 'rumble', 'ryze', 'sejuani', 'senna', 'sett', 'shaco', 'shen', 'shyvana', 'singed', 'sion', 'sivir', 'skarner', 'sona', 'soraka', 'swain', 'sylas', 'syndra', 'tahmkench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twistedfate', 'twitch', 'udyr', 'urgot', 'varus', 'vayne', 'veigar', "vel'koz", 'vi', 'viktor', 'vladimir', 'volibear', 'warwick', 'wukong', 'xayah', 'xerath', 'xinzhao', 'yasuo', 'yorick', 'yuumi', 'zac', 'zed', 'ziggs', 'zilean', 'zoe', 'zyra']

u_gg_url = "https://u.gg/lol/champions/champ1/build"
counter_url = "https://lolcounter.com/champions/champ1"
counter_vs_url = "https://lolcounter.com/tips/champ2/champ1"


def main():
    openSites(constructUrls())


def constructUrls():
    url_list = []
    champion1 = str(sys.argv[1]).lower()
    if len(sys.argv) == 4:
        champion2 = str(sys.argv[3]).lower()

        if champion2 in champion_list:
            url_list.append(counter_vs_url.replace("champ1", champion1))
            url_list.append(counter_vs_url.replace("champ2", champion2))
            url_list.append(counter_url.replace("champ1", champion2))
        else:
            print("Cannot find champ -> " + champion2)

    if champion1 in champion_list:
        url_list.append(u_gg_url.replace("champ1", champion1))
        url_list.append(counter_url.replace("champ1", champion1))
    else:
        print("Cannot find champ -> " + champion1)

    return url_list


def openSites(url_list):
    for url in url_list:
        webbrowser.open(url)


def getChampionList(file):
    champion_list_file = open(file, "r")
    champions = champion_list_file.read().split(",")
    champion_list_file.close()
    return champions


if __name__ == "__main__":
    main()
