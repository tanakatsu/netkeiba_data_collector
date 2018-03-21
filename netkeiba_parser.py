# coding: utf-8

from bs4 import BeautifulSoup
from util import getPage, searchHorse
import requests


def getHorseResult(html, offset=0):
    results = []
    soup = BeautifulSoup(html, "html.parser")
    horse_result_table = soup.select("table.race_table_01 tr")
    for i, row in enumerate(horse_result_table[1:]):
        # print(row)
        data = row.select("td")
        name = str(data[1].string)
        horse_id = data[1].a.get("href").replace("/horse/", "")[:-1]
        sex = str(data[2].string)
        birth_year = int(data[3].string)
        stable = str(data[5].a.string)
        trainer_id = str(data[5].a.get("href").replace('/trainer/', '')[:-1])
        sire = str(data[6].a.string)
        mare = str(data[7].a.string)
        bms = str(data[8].a.string)
        owner = str(data[9].a.string)
        owner_id = str(data[9].a.get("href").replace('/owner/', '')[:-1])
        breeder = str(data[10].a.string)
        breeder_id = str(data[10].a.get("href").replace('/breeder/', '')[:-1])
        prize = float(data[11].string.replace(',', ''))
        result = {'no': i + offset,
                  'id': horse_id,
                  'name': name,
                  'sex': sex,
                  'birth_year': birth_year,
                  'stable': stable,
                  'trainer_id': trainer_id,
                  'sire': sire,
                  'mare': mare,
                  'bms': bms,
                  'owner': owner,
                  'owner_id': owner_id,
                  'breeder': breeder,
                  'breeder_id': breeder_id,
                  'prize': prize}
        results.append(result)
    return results


def getSireResult(html, offset=0):
    results = []
    soup = BeautifulSoup(html, "html.parser")
    sire_leading_table = soup.select("table.race_table_01 tr")
    for i, row in enumerate(sire_leading_table[2:]):
        # print(row)
        data = row.select("td")
        name = str(data[1].string)
        sire_id = data[1].a.get("href").replace("/horse/sire/", "")[:-1]
        race_horse_count = int(data[2].string.replace(',', ''))
        win_horse_count = int(data[3].string.replace(',', ''))
        race_count = int(data[4].string.replace(',', ''))
        win_count = int(data[5].string.replace(',', ''))
        grade_race_count = int(data[6].string.replace(',', ''))
        grade_race_win = int(data[7].string.replace(',', ''))
        stakes_race_count = int(data[8].string.replace(',', ''))
        stakes_race_win = int(data[9].string.replace(',', ''))
        general_race_count = int(data[10].string.replace(',', ''))
        general_race_win = int(data[11].string.replace(',', ''))
        turf_race_count = int(data[12].string.replace(',', ''))
        turf_race_win = int(data[13].string.replace(',', ''))
        dart_race_count = int(data[14].string.replace(',', ''))
        dart_race_win = int(data[15].string.replace(',', ''))
        win_ratio = float(data[16].string)
        earning_index = float(data[17].string)
        prize = float(data[19].string.replace(',', ''))
        avg_turf_distance = float(data[19].string.replace(',', ''))
        avg_dart_distance = float(data[20].string.replace(',', ''))
        result = {'no': i + offset,
                  'id': sire_id,
                  'name': name,
                  'race_horse_count': race_horse_count,
                  'win_horse_count': win_horse_count,
                  'race_count': race_count,
                  'win_count': win_count,
                  'grade_race_count': grade_race_count,
                  'grade_race_win': grade_race_win,
                  'stakes_race_count': stakes_race_count,
                  'stakes_race_win': stakes_race_win,
                  'general_race_count': general_race_count,
                  'general_race_win': general_race_win,
                  'turf_race_count': turf_race_count,
                  'turf_race_win': turf_race_win,
                  'dart_race_count': dart_race_count,
                  'dart_race_win': dart_race_win,
                  'win_ratio': win_ratio,
                  'earning_index': earning_index,
                  'prize': prize,
                  'avg_turf_distance': avg_turf_distance,
                  'avg_dart_distance': avg_dart_distance}
        results.append(result)
    return results


def getBmsResult(html, offset=0):
    results = []
    soup = BeautifulSoup(html, "html.parser")
    sire_leading_table = soup.select("table.race_table_01 tr")
    for i, row in enumerate(sire_leading_table[2:]):
        # print(row)
        data = row.select("td")
        name = str(data[1].string)
        sire_id = data[1].a.get("href").replace("/horse/sire/", "")[:-1]
        race_horse_count = int(data[2].string.replace(',', ''))
        win_horse_count = int(data[3].string)
        race_count = int(data[4].string.replace(',', ''))
        win_count = int(data[5].string.replace(',', ''))
        grade_race_count = int(data[6].string.replace(',', ''))
        grade_race_win = int(data[7].string.replace(',', ''))
        stakes_race_count = int(data[8].string.replace(',', ''))
        stakes_race_win = int(data[9].string.replace(',', ''))
        general_race_count = int(data[10].string.replace(',', ''))
        general_race_win = int(data[11].string.replace(',', ''))
        turf_race_count = int(data[12].string.replace(',', ''))
        turf_race_win = int(data[13].string.replace(',', ''))
        dart_race_count = int(data[14].string.replace(',', ''))
        dart_race_win = int(data[15].string.replace(',', ''))
        win_ratio = float(data[16].string)
        earning_index = float(data[17].string)
        avg_turf_distance = float(data[19].string.replace(',', ''))
        avg_dart_distance = float(data[20].string.replace(',', ''))
        result = {'no': i + offset,
                  'id': sire_id,
                  'name': name,
                  'race_horse_count': race_horse_count,
                  'win_horse_count': win_horse_count,
                  'race_count': race_count,
                  'win_count': win_count,
                  'grade_race_count': grade_race_count,
                  'grade_race_win': grade_race_win,
                  'stakes_race_count': stakes_race_count,
                  'stakes_race_win': stakes_race_win,
                  'general_race_count': general_race_count,
                  'general_race_win': general_race_win,
                  'turf_race_count': turf_race_count,
                  'turf_race_win': turf_race_win,
                  'dart_race_count': dart_race_count,
                  'dart_race_win': dart_race_win,
                  'win_ratio': win_ratio,
                  'earning_index': earning_index,
                  'avg_turf_distance': avg_turf_distance,
                  'avg_dart_distance': avg_dart_distance}
        results.append(result)
    return results


def getBreederResult(html, offset=0):
    results = []
    soup = BeautifulSoup(html, "html.parser")
    sire_leading_table = soup.select("table.race_table_01 tr")
    for i, row in enumerate(sire_leading_table[2:]):
        # print(row)
        data = row.select("td")
        name = str(data[1].string)
        breeder_id = data[1].a.get("href").replace("/breeder/", "")[:-1]
        win_count = int(data[2].string.replace(',', ''))
        second_place_count = int(data[3].string.replace(',', ''))
        third_place_count = int(data[4].string.replace(',', ''))
        unplaced_count = int(data[5].string.replace(',', ''))
        grade_race_count = int(data[6].string.replace(',', ''))
        grade_race_win = int(data[7].string.replace(',', ''))
        stakes_race_count = int(data[8].string.replace(',', ''))
        stakes_race_win = int(data[9].string.replace(',', ''))
        general_race_count = int(data[10].string.replace(',', ''))
        general_race_win = int(data[11].string.replace(',', ''))
        turf_race_count = int(data[12].string.replace(',', ''))
        turf_race_win = int(data[13].string.replace(',', ''))
        dart_race_count = int(data[14].string.replace(',', ''))
        dart_race_win = int(data[15].string.replace(',', ''))
        win_ratio = float(data[16].string)
        in_second_place_ratio = float(data[17].string)
        in_third_place_ratio = float(data[18].string)
        prize = float(data[19].string.replace(',', ''))
        result = {'no': i + offset,
                  'id': breeder_id,
                  'name': name,
                  'win_count': win_count,
                  'second_place_count': second_place_count,
                  'third_place_count': third_place_count,
                  'unplaced_count': unplaced_count,
                  'grade_race_count': grade_race_count,
                  'grade_race_win': grade_race_win,
                  'stakes_race_count': stakes_race_count,
                  'stakes_race_win': stakes_race_win,
                  'general_race_count': general_race_count,
                  'general_race_win': general_race_win,
                  'turf_race_count': turf_race_count,
                  'turf_race_win': turf_race_win,
                  'dart_race_count': dart_race_count,
                  'dart_race_win': dart_race_win,
                  'win_ratio': win_ratio,
                  'in_second_place_ratio': in_second_place_ratio,
                  'in_third_place_ratio': in_third_place_ratio,
                  'prize': prize}
        results.append(result)
    return results


def getOwnerResult(html, offset=0):
    results = []
    soup = BeautifulSoup(html, "html.parser")
    sire_leading_table = soup.select("table.race_table_01 tr")
    for i, row in enumerate(sire_leading_table[2:]):
        # print(row)
        data = row.select("td")
        name = str(data[1].string)
        owner_id = data[1].a.get("href").replace("/owner/", "")[:-1]
        win_count = int(data[2].string.replace(',', ''))
        second_place_count = int(data[3].string.replace(',', ''))
        third_place_count = int(data[4].string.replace(',', ''))
        unplaced_count = int(data[5].string.replace(',', ''))
        grade_race_count = int(data[6].string.replace(',', ''))
        grade_race_win = int(data[7].string.replace(',', ''))
        stakes_race_count = int(data[8].string.replace(',', ''))
        stakes_race_win = int(data[9].string.replace(',', ''))
        general_race_count = int(data[10].string.replace(',', ''))
        general_race_win = int(data[11].string.replace(',', ''))
        turf_race_count = int(data[12].string.replace(',', ''))
        turf_race_win = int(data[13].string.replace(',', ''))
        dart_race_count = int(data[14].string.replace(',', ''))
        dart_race_win = int(data[15].string.replace(',', ''))
        win_ratio = float(data[16].string)
        in_second_place_ratio = float(data[17].string)
        in_third_place_ratio = float(data[18].string)
        prize = float(data[19].string.replace(',', ''))
        result = {'no': i + offset,
                  'id': owner_id,
                  'name': name,
                  'win_count': win_count,
                  'second_place_count': second_place_count,
                  'third_place_count': third_place_count,
                  'unplaced_count': unplaced_count,
                  'grade_race_count': grade_race_count,
                  'grade_race_win': grade_race_win,
                  'stakes_race_count': stakes_race_count,
                  'stakes_race_win': stakes_race_win,
                  'general_race_count': general_race_count,
                  'general_race_win': general_race_win,
                  'turf_race_count': turf_race_count,
                  'turf_race_win': turf_race_win,
                  'dart_race_count': dart_race_count,
                  'dart_race_win': dart_race_win,
                  'win_ratio': win_ratio,
                  'in_second_place_ratio': in_second_place_ratio,
                  'in_third_place_ratio': in_third_place_ratio,
                  'prize': prize}
        results.append(result)
    return results


def getTrainerResult(html, offset=0):
    results = []
    soup = BeautifulSoup(html, "html.parser")
    trainer_leading_table = soup.select("table.race_table_01 tr")
    for i, row in enumerate(trainer_leading_table[2:]):
        # print row
        data = row.select("td")
        name = str(data[1].string)
        trainer_id = data[1].a.get("href").replace("/trainer/", "")[:-1]
        stable = str(data[2].string)
        win_count = int(data[4].string.replace(',', ''))
        second_place_count = int(data[5].string.replace(',', ''))
        third_place_count = int(data[6].string.replace(',', ''))
        unplaced_count = int(data[7].string.replace(',', ''))
        grade_race_count = int(data[8].string.replace(',', ''))
        grade_race_win = int(data[9].string.replace(',', ''))
        stakes_race_count = int(data[10].string.replace(',', ''))
        stakes_race_win = int(data[11].string.replace(',', ''))
        general_race_count = int(data[12].string.replace(',', ''))
        general_race_win = int(data[13].string.replace(',', ''))
        turf_race_count = int(data[14].string.replace(',', ''))
        turf_race_win = int(data[15].string.replace(',', ''))
        dart_race_count = int(data[16].string.replace(',', ''))
        dart_race_win = int(data[17].string.replace(',', ''))
        win_ratio = float(data[18].string)
        in_second_place_ratio = float(data[19].string)
        in_third_place_ratio = float(data[20].string)
        prize = float(data[21].string.replace(',', ''))
        if stable != '栗東' and stable != '美浦':
            continue
        result = {'no': i + offset,
                  'id': trainer_id,
                  'name': name,
                  'stable': stable,
                  'win_count': win_count,
                  'second_place_count': second_place_count,
                  'third_place_count': third_place_count,
                  'unplaced_count': unplaced_count,
                  'grade_race_count': grade_race_count,
                  'grade_race_win': grade_race_win,
                  'stakes_race_count': stakes_race_count,
                  'stakes_race_win': stakes_race_win,
                  'general_race_count': general_race_count,
                  'general_race_win': general_race_win,
                  'turf_race_count': turf_race_count,
                  'turf_race_win': turf_race_win,
                  'dart_race_count': dart_race_count,
                  'dart_race_win': dart_race_win,
                  'win_ratio': win_ratio,
                  'in_second_place_ratio': in_second_place_ratio,
                  'in_third_place_ratio': in_third_place_ratio,
                  'prize': prize}
        results.append(result)
    return results


def getJockeyResult(html, offset=0):
    results = []
    soup = BeautifulSoup(html, "html.parser")
    trainer_leading_table = soup.select("table.race_table_01 tr")
    for i, row in enumerate(trainer_leading_table[2:]):
        # print row
        data = row.select("td")
        name = str(data[1].string)
        jockey_id = data[1].a.get("href").replace("/jockey/", "")[:-1]
        stable = str(data[2].string)
        win_count = int(data[4].string.replace(',', ''))
        second_place_count = int(data[5].string.replace(',', ''))
        third_place_count = int(data[6].string.replace(',', ''))
        unplaced_count = int(data[7].string.replace(',', ''))
        grade_race_count = int(data[8].string.replace(',', ''))
        grade_race_win = int(data[9].string.replace(',', ''))
        stakes_race_count = int(data[10].string.replace(',', ''))
        stakes_race_win = int(data[11].string.replace(',', ''))
        general_race_count = int(data[12].string.replace(',', ''))
        general_race_win = int(data[13].string.replace(',', ''))
        turf_race_count = int(data[14].string.replace(',', ''))
        turf_race_win = int(data[15].string.replace(',', ''))
        dart_race_count = int(data[16].string.replace(',', ''))
        dart_race_win = int(data[17].string.replace(',', ''))
        win_ratio = float(data[18].string)
        in_second_place_ratio = float(data[19].string)
        in_third_place_ratio = float(data[20].string)
        prize = float(data[21].string.replace(',', ''))
        result = {'no': i + offset,
                  'id': jockey_id,
                  'name': name,
                  'stable': stable,
                  'win_count': win_count,
                  'second_place_count': second_place_count,
                  'third_place_count': third_place_count,
                  'unplaced_count': unplaced_count,
                  'grade_race_count': grade_race_count,
                  'grade_race_win': grade_race_win,
                  'stakes_race_count': stakes_race_count,
                  'stakes_race_win': stakes_race_win,
                  'general_race_count': general_race_count,
                  'general_race_win': general_race_win,
                  'turf_race_count': turf_race_count,
                  'turf_race_win': turf_race_win,
                  'dart_race_count': dart_race_count,
                  'dart_race_win': dart_race_win,
                  'win_ratio': win_ratio,
                  'in_second_place_ratio': in_second_place_ratio,
                  'in_third_place_ratio': in_third_place_ratio,
                  'prize': prize}
        results.append(result)
    return results


def getHorseAdditionalInfo(html, offset=0):
    soup = BeautifulSoup(html, "html.parser")

    # name = soup.select("div.horse_title h1")[0].string.strip()
    name = soup.select('table[class="tekisei_table"]')[0].get("summary").split('の')[0]

    horse_id = soup.select("div.db_head_regist ul.db_detail_menu li")[1].select("a")[0].get("href").replace('/horse/', '')[:-1]

    prof_table = soup.select("table.db_prof_table")[0]
    rows = prof_table.select("tr")

    birth_date = rows[0].select('td')[0].string.replace('年', '/').replace('月', '/').replace('日', '')

    if rows[3].find('th').string == '募集情報':
        ofs = 1
    else:
        ofs = 0

    if '円' in rows[5 + ofs].select('td')[0].get_text():
        sales_price = rows[5 + ofs].select("td")[0].get_text().split('円')[0].replace('億', '').replace('万', '').replace(',', '')
    else:
        sales_price = None

    race_result = rows[7 + ofs].select("td a")[0].string

    result = {'id': horse_id,
              'name': name,
              'birth_date': birth_date,
              'race_result': race_result,
              'sales_price': sales_price}
    return result


def getMareCropsResult(html, offset=0):
    soup = BeautifulSoup(html, "html.parser")

    # name = soup.select("div.horse_title h1")[0].string.strip()
    name = soup.select('table[class="tekisei_table"]')[0].get("summary").split('の')[0]

    horse_id = soup.select("div.db_head_regist ul.db_detail_menu li")[1].select("a")[0].get("href").replace('/horse/', '')[:-1]

    table = soup.select('table[summary="産駒成績"]')
    if len(table) > 0:
        rows = table[0].select("td")
        crop_count = rows[0].string.replace('頭', '')
        crop_grade_win_count = rows[1].a.string.replace('勝', '')
        crop_grade_horse_count = rows[1].select('a')[1].string.replace('頭', '')
        crop_win_count = rows[2].string.replace('勝', '')
    else:
        crop_count = None
        crop_grade_win_count = None
        crop_grade_horse_count = None
        crop_win_count = None

    result = {'id': horse_id,
              'name': name,
              'crop_count': crop_count,
              'crop_grade_win_count': crop_grade_win_count,
              'crop_grade_horse_count': crop_grade_horse_count,
              'crop_win_count': crop_win_count}
    return result


def getHorseIdByName(name):
    html = searchHorse(word=name, match=1, sort='birthyear')

    soup = BeautifulSoup(html, "html.parser")
    if len(soup.select("link[rel='canonical']")) > 0:
        horse_id = soup.select("link[rel='canonical']")[0].get("href").split('/')[-2]
    else:
        horse_id = soup.select("td.xml a")[0].get("href").split('/')[-2]
    return horse_id


if __name__ == "__main__":
    # html = getPage("http://db.netkeiba.com/horse/2014102565/")
    # html = getPage("http://db.netkeiba.com/horse/2014106083/")
    # result = getHorseAdditionalInfo(html)

    # html = getPage("http://db.netkeiba.com/horse/2004104258/")
    # html = getPage("http://db.netkeiba.com/horse/1992108561/")
    # result = getMareCropsResult(html)

    # result = getHorseIdByName('オルフェーヴル')
    result = getHorseIdByName('スティンガー')
    print(result)
