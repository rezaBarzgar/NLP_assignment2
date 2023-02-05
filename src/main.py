import json

from nltk.corpus import nps_chat
from utils.utils import *


def main():
    # fetching nltk
    # nltk.download('nps_chat')

    b_news_sents = [[y.lower() for y in x] for x in brown.sents()]

    # training models
    models = []
    for number in [2, 3]:  # [1, 2, 3, 4, 5]
        model = generate_trained_model(number, tokenized_text=b_news_sents)
        models.append((number, model))
        save_model(f"../models/{number}ary-brown.pkl", model)
    # for number in [2, 3, 4]:  # [1, 2, 3, 4, 5]
    #     models.append((number, load_model(f'../models/{number}ary.pkl')))

    # generate results
    data = read_birkbeck('../data/APPLING1DAT.643')
    results = {}
    for number, model in models:
        model_results = []
        for sentence in data:
            prediction = predictions(model=model, n=number, text=sentence[2])
            success_at_1, success_at_5, success_at_10 = success_at_k(correct_word=sentence[1],
                                                                     predictions_list=prediction)
            # print(sentence[1])
            if success_at_1 or success_at_5 or success_at_10:
                print(sentence)
        print(model)
        print(20 * '-/-')


if __name__ == '__main__':
    main()
