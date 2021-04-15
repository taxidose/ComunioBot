from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from operator import itemgetter
import time
import csv

import Bot
import SecretKeys
import Comunio

FRANKEN = ["Seeeb", "Sebb", "Marco", "chris", "Wolfi", "taxi", "Nico", "Fritzi"]


def get_table_total(data: list) -> str:
    list_sorted = sorted(data, key=lambda row: row["points"], reverse=True)
    return_string = "|{:1s}|{:4s}|{:5s}|{:1s}|{:11s}\n".format("#", "Name", "Punkte", "+", "Teamwert")
    for i, player in enumerate(list_sorted):
        rank = f"{i + 1}."
        name = player["name"]
        points = player["points"]
        plus = player["plus"]
        networth = player["networth"]

        return_string += "{:3s} {:8s} {:5s} {:3s} {:12s}\n".format(rank, name, points, plus, networth)
        # print(rank)
        # print(player)
    return return_string


def get_last_matchday(data):
    list_sorted = sorted(data, key=lambda row: row["plus"], reverse=True)
    return_string = "{:3s} {:8s} {:6s}\n".format("|+", "|Name", "|Gesamtpunkte")
    for player in list_sorted:
        # rank = f"{i+1}."
        name = str(player["name"])
        points = str(player["points"])
        plus = str(player["plus"])
        # networth = str(player["networth"])

        return_string += "+{:3s} {:8s} {:6s}\n".format(plus, name, points)
        # print(rank)
        # print(player)
    return return_string


def franken_vs_jecken(data):
    total_pts_franken = 0
    total_pts_jecken = 0
    franken = 0
    jecken = 0
    best_rank_franken = 0
    best_rank_jecken = 0

    total_player = 0
    for player in data:
        total_player += 1
        if player["name"] in FRANKEN:
            total_pts_franken += player["points"]
            if best_rank_franken == 0:
                best_rank_franken = total_player
            franken += 1
        else:
            total_pts_jecken += player["points"]
            if best_rank_jecken == 0:
                best_rank_jecken = total_player
            jecken += 1

    avg_pts_franken = total_pts_franken / franken
    avg_pts_jecken = total_pts_jecken / jecken
    smiley = ":("
    if avg_pts_jecken < avg_pts_franken:
        smiley = ":)"

    return_string = f"Franken:\n   Ø-Punkte: {avg_pts_franken}\n   bester Platz: {best_rank_franken}\nJecken:\n    Ø-Punkte: {avg_pts_jecken}\n   bester Platz: {best_rank_jecken}\n{smiley}"
    # print(return_string)
    return return_string

def read_csv(file_name="latest.csv"):
    with open(file_name) as f:
        reader = csv.DictReader(f)
        data = list(reader)
        #print(data)
        return data

def main():
    #Comunio.comunio_login()

    #data = read_csv()
    #Comunio.write_csv(data)
    #print(get_table_total(data))
    # print(get_last_matchday(data))
    # franken_vs_jecken(data)
    #print(read_csv())

    Bot.init_bot()


if __name__ == '__main__':
    main()
