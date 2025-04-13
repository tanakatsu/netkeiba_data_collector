# coding: utf-8

import pandas as pd
from argparse import ArgumentParser
from time import sleep
from netkeiba_util import getSerial, getPageBySerial, checkIfNextPageExists, searchHorse
from netkeiba_parser import getHorseResult


def main():
    parser = ArgumentParser()
    parser.add_argument('--age', action='store', type=int, required=True, help='target age')
    parser.add_argument('-n', action='store', type=int, default=None, help='max sample')
    parser.add_argument('--output', '-o', action='store', type=str, default='horse_ranking.csv', help='output filename')
    parser.add_argument('--include_no_debut', action='store_true', default=False, help='include no debut horses')
    args = parser.parse_args()

    target_age = args.age
    max_sample = args.n
    output_filename = args.output
    include_no_debut = args.include_no_debut
    results = []
    next_page = 1

    # first page
    if include_no_debut:
        html = searchHorse(under_age=target_age, over_age=target_age)
    else:
        html = searchHorse(under_age=target_age, over_age=target_age, grade=[4, 3, 2, 1])  # debut horse only
    page_result = getHorseResult(html)
    serial = getSerial(html)
    has_next_page = checkIfNextPageExists(html)
    results += page_result
    print('get {} ({})'.format(len(page_result), len(results)))
    sleep(1)

    # after first page
    while(True):
        if max_sample and len(results) >= max_sample:
            results = results[:max_sample]
            break
        if not has_next_page:
            break
        next_page = next_page + 1
        html = getPageBySerial(serial, next_page)
        page_result = getHorseResult(html)
        serial = getSerial(html)
        has_next_page = checkIfNextPageExists(html)
        results += page_result
        print('get {} ({})'.format(len(page_result), len(results)))
        sleep(1)

    print(len(results))
    cols = ['id',
            'name',
            'sex',
            'birth_year',
            'stable',
            'stable_loc',
            'trainer_id',
            'sire',
            'mare',
            'bms',
            'owner',
            'owner_id',
            'breeder',
            'breeder_id',
            'prize']
    df = pd.DataFrame(results, columns=cols)
    df.to_csv(output_filename)


if __name__ == "__main__":
    main()
