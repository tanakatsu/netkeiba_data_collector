# coding: utf-8

import pandas as pd
from argparse import ArgumentParser
from time import sleep
from util import getSerial, getPageBySerial, checkIfNextPageExists, searchHorse
from netkeiba_parser import getHorseResult


def main():
    parser = ArgumentParser()
    parser.add_argument('--age', action='store', type=int, required=True, help='target age')
    parser.add_argument('-n', action='store', type=int, default=None, help='max sample')
    parser.add_argument('--output', '-o', action='store', type=str, default='horse_ranking.csv', help='output filename')
    args = parser.parse_args()

    target_age = args.age
    max_sample = args.n
    output_filename = args.output
    results = []

    # first page
    html = searchHorse(under_age=target_age, over_age=target_age)
    page_result = getHorseResult(html)
    serial = getSerial(html)
    next_page = checkIfNextPageExists(html)
    results += page_result
    print('get {} ({})'.format(len(page_result), len(results)))
    sleep(1)

    # after first page
    while(True):
        if max_sample and len(results) >= max_sample:
            results = results[:max_sample]
            break
        if not next_page:
            break
        html = getPageBySerial(serial, next_page)
        page_result = getHorseResult(html)
        serial = getSerial(html)
        next_page = checkIfNextPageExists(html)
        results += page_result
        print('get {} ({})'.format(len(page_result), len(results)))
        sleep(1)

    print(len(results))
    df = pd.DataFrame(results)
    reordered_cols = ['id',
                      'name',
                      'sex',
                      'birth_year',
                      'stable',
                      'trainer_id',
                      'sire',
                      'mare',
                      'bms',
                      'owner',
                      'owner_id',
                      'breeder',
                      'breeder_id',
                      'prize']
    df = df[reordered_cols]
    df.to_csv(output_filename)


if __name__ == "__main__":
    main()
