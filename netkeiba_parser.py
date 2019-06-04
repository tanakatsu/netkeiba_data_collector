# coding: utf-8

from bs4 import BeautifulSoup
from netkeiba_util import getPage, searchHorse


def getHorseResult(html, offset=0):
    results = []
    soup = BeautifulSoup(html, "html.parser")
    horse_result_table = soup.select("table.race_table_01 tr")
    for i, row in enumerate(horse_result_table[1:]):
        # print(row)
        data = row.select("td")
        name = str(data[1].string)
        horse_id = data[1].a.get("href").replace("/horse/", "")[:-1]
        # print(horse_id)
        sex = str(data[2].string)
        birth_year = int(data[3].string)
        if data[5].a:
            stable = str(data[5].a.string)
            trainer_id = str(data[5].a.get("href").replace('/trainer/', '')[:-1])
            if "[西]" in data[5].text:
                stable_loc = "栗東"
            elif "[東]" in data[5].text:
                stable_loc = "美浦"
            elif "[地]" in data[5].text:
                stable_loc = "地方"
            else:
                stable_loc = None
        else:
            stable = None
            trainer_id = None
            stable_loc = None
        sire = str(data[6].a.string)
        mare = str(data[7].a.string)
        bms = str(data[8].a.string)
        if data[9].a:
            owner = str(data[9].a.string)
            owner_id = str(data[9].a.get("href").replace('/owner/', '')[:-1])
        else:
            owner = None
            owner_id = None
        if data[10].a:
            breeder = str(data[10].a.string)
            breeder_id = str(data[10].a.get("href").replace('/breeder/', '')[:-1])
        else:
            breeder = None
            breeder_id = None
        prize = float(data[11].string.replace(',', ''))
        result = {'no': i + offset,
                  'id': horse_id,
                  'name': name,
                  'sex': sex,
                  'birth_year': birth_year,
                  'stable': stable,
                  'stable_loc': stable_loc,
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
    hair = soup.select("div.horse_title p.txt_01")[0].string.split('　')[-1]
    if "□地" in soup.select("div.horse_title h1")[0].text:
        kakuchi = True
    else:
        kakuchi = False
    if "○地" in soup.select("div.horse_title h1")[0].text:
        maruchi = True
    else:
        maruchi = False
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
    relatives = '、'.join([a.string for a in rows[9 + ofs].select("td a") if a.string])

    debut_weight = None
    races = soup.select('div.db_main_deta table tbody tr')
    if len(races) > 0:
        first_race = races[-1]
        first_race_data = first_race.select('td')
        weight = first_race_data[23].string
        if not weight == '計不':
            debut_weight = int(weight.replace('(0)', ''))

    blood = soup.select('table.blood_table tr td')
    sire_id = blood[0].find('a').get('href').split('/')[3]
    mare_id = blood[3].find('a').get('href').split('/')[3]

    result = {'id': horse_id,
              'name': name,
              'sire_id': sire_id,
              'mare_id': mare_id,
              'hair': hair,
              'birth_date': birth_date,
              'race_result': race_result,
              'sales_price': sales_price,
              'relatives': relatives,
              'debut_weight': debut_weight,
              'kakuchi': kakuchi,
              'maruchi': maruchi}
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

    profile_rows = soup.select("div.db_prof_area_02 table tr")
    birth_date = None
    race_result = None
    for row in profile_rows:
        if row.find("th"):
            if row.find("th").string == '生年月日':
                birth_date = row.find("td").string.replace('年', '/').replace('月', '/').replace('日', '')
                birth_date = birth_date.rstrip('/')
            elif row.find("th").string == '通算成績':
                race_result = row.select("td a")[0].string

    result = {'id': horse_id,
              'name': name,
              'birth_date': birth_date,
              'race_result': race_result,
              'crop_count': crop_count,
              'crop_grade_win_count': crop_grade_win_count,
              'crop_grade_horse_count': crop_grade_horse_count,
              'crop_win_count': crop_win_count}
    return result


def getHorseIdByName(name, **kwargs):
    # print(name)
    html = searchHorse(word=name, match=1, sort='birthyear', **kwargs)
    if html == '':  # something is wrong at server...
        return None

    soup = BeautifulSoup(html, "html.parser")
    if len(soup.select("link[rel='canonical']")) > 0:
        horse_id = soup.select("link[rel='canonical']")[0].get("href").split('/')[-2]
    elif len(soup.select('table[summary="競走馬検索結果"] td a[title="' + name + '"]')) > 0:
        horse_id = soup.select('table[summary="競走馬検索結果"] td a[title="' + name + '"]')[0].get("href").split('/')[-2]
    else:
        horse_id = None

    return horse_id


def getHorseIdByName2(name, **kwargs):
    if name.endswith('ＩＩ'):
        search_name = name[:-2]
    elif ' ' in name:
        search_name = ' '.join(name.split(' ')[:-1])
    else:
        search_name = name

    # print(name, search_name)
    html = searchHorse(word=search_name, sort='birthyear', **kwargs)

    soup = BeautifulSoup(html, "html.parser")

    if len(soup.select("link[rel='canonical']")) > 0:
        horse_id = soup.select("link[rel='canonical']")[0].get("href").split('/')[-2]
        return horse_id

    name_tags = soup.select("td.xml.txt_l a")
    for tag in name_tags:
        if tag.get("title") == name:
            horse_id = tag.get("href").split('/')[-2]
            return horse_id

    name_tags2 = soup.select("td.bml.txt_l a")
    for tag in name_tags2:
        if tag.get("title") == name:
            horse_id = tag.get("href").split('/')[-2]
            return horse_id
    return None


def getBreederId(html, offset=0):
    soup = BeautifulSoup(html, "html.parser")

    link = soup.select("ul.db_detail_menu li a")[0]
    breeder_id = link.get("href").split('/')[-2]
    name = link.get("title").replace('の近走成績', '')

    result = {'alt_id': breeder_id,
              'name': name}
    return result


def getHorseRaceResults(html):
    soup = BeautifulSoup(html, "html.parser")
    races = soup.select('table[class="db_h_race_results nk_tb_common"] tbody tr')
    results = []
    for race in races:
        race_data = {}
        race_info_items = race.select("td")
        race_data['date'] = race_info_items[0].find("a").text
        if race_info_items[27].text == '\xa0':
            race_data['prize'] = 0
        else:
            race_data['prize'] = float(race_info_items[27].text.replace(",", ""))
        try:
            race_data['place'] = int(race_info_items[11].text)
        except ValueError:
            race_data['place'] = None
        race_data['name'] = race_info_items[4].text
        try:
            race_data['weight'] = int(race_info_items[23].text.split('(')[0])
        except ValueError:
            race_data['weight'] = None
        results.append(race_data)

    return results[::-1]


def getMareCrops(html):
    soup = BeautifulSoup(html, "html.parser")
    tr_elms = soup.select('table[class="nk_tb_common race_table_01"] tr')
    crops = []
    for tr_elm in tr_elms[1:]:
        td_elms = tr_elm.select("td")
        year = int(td_elms[0].text)
        name = td_elms[1].text
        horse_id = td_elms[1].find('a').get('href').split('/')[2]
        sex = td_elms[2].text
        sire = td_elms[3].text.strip()
        crops.append({'year': year,
                      'name': name,
                      'horse_id': horse_id,
                      'sex': sex,
                      'sire': sire})
    return crops[::-1]


if __name__ == "__main__":
    # html = getPage("https://db.netkeiba.com/horse/2014102565/")
    # html = getPage("https://db.netkeiba.com/horse/2015102894/")
    # html = getPage("https://db.netkeiba.com/horse/2014106083/")
    # html = getPage("https://db.netkeiba.com/horse/2016100893/")
    # html = getPage("https://db.netkeiba.com/horse/2016103387/")
    # html = getPage("https://db.netkeiba.com/horse/2016104532/")
    # result = getHorseAdditionalInfo(html)

    # html = getPage("https://db.netkeiba.com/horse/2004104258/")
    # html = getPage("https://db.netkeiba.com/horse/1992108561/")
    # html = getPage("https://db.netkeiba.com/horse/2000106445/")
    # html = getPage("https://db.netkeiba.com/horse/2004102429/")
    # html = getPage("https://db.netkeiba.com/horse/000a013c70")
    # html = getPage("https://db.netkeiba.com/horse/000a011df8/")
    # result = getMareCropsResult(html)

    # result = getHorseIdByName('オルフェーヴル')
    # result = getHorseIdByName('スティンガー')
    # result = getHorseIdByName('トリプレックス')
    # result = getHorseIdByName('ラッキーライラック', sex=[2])

    # result = getHorseIdByName2('ベラドーラＩＩ')
    # result = getHorseIdByName2('Debit Or Credit')

    # html = getPage("https://db.netkeiba.com/breeder/373126/")
    # result = getBreederId(html)

    html = getPage("https://db.netkeiba.com/horse/2014106083/")
    result = getHorseRaceResults(html)

    # html = getPage("https://db.netkeiba.com/horse/mare/2002100844/")
    # result = getMareCrops(html)

    print(result)
