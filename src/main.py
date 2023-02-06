import json
import os
import sys

import pytrec_eval
from nltk.corpus import *
from utils.utils import *


def main():
    # fetching nltk
    nltk.download('brown')

    corpora = []
    model_name = 'news'

    # training models
    categories = ['news', 'adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor',
                  'learned', 'lore', 'mystery', 'religion', 'reviews', 'romance', 'science_fiction']

    for corpus in categories:
        if corpus == 'news':
            corpora = [[y.lower() for y in x] for x in brown.sents(categories='news')]
        else:
            corpora.extend([[y.lower() for y in x] for x in brown.sents(categories=corpus)])
            model_name = model_name + '_' + corpus
        print(f'number of sentences: {len(corpora)} ~~~~~~~~~ latest added category: {corpus}')

        #     Generating Models
        for number in [1, 2, 3, 5, 10]:  #
            model = generate_trained_model(number, tokenized_text=corpora)
            save_model(f"../models/{number}-{model_name}.pkl", model)

    # generate results
    data = read_birkbeck('../data/APPLING1DAT.643')
    directory = '../models'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            lang_model = load_model(f)
            f = f.split('.')[-2].split('-')
            number = int(f[0].split('\\')[-1])
            name = f[1]
            results = {}
            for sentence in data:
                prediction = predictions(model=lang_model, n=number, text=sentence[2])
                success_at_1, success_at_5, success_at_10, success_at_all = success_at_k(correct_word=sentence[1],
                                                                                         predictions_list=prediction)
                results[f'{(sentence[0], sentence[1])}'] = {
                    'success_at_1': success_at_1,
                    'success_at_5': success_at_5,
                    'success_at_10': success_at_10,
                    'success_at_all': success_at_all,
                }
            with open('./output.txt', 'a') as file:
                original_stdout = sys.stdout
                sys.stdout = file
                print(f'{number}ary model on {name} categories')
                for measure in sorted(list(results[list(results.keys())[0]].keys())):
                    print(measure, 'average:', pytrec_eval.compute_aggregated_measure(
                        measure, [query_measures[measure] for query_measures in results.values()]))
                print('-' * 40)
                sys.stdout = original_stdout


if __name__ == '__main__':
    main()
