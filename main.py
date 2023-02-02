import json

from utils.utils import *


def main():
    # fetching nltk
    nltk.download('brown')
    b_news_sents = [[y.lower() for y in x] for x in brown.sents(categories='news')]

    # training models
    models = []
    for number in [10]:  # [1, 2, 3, 4, 5]
        models.append((number, generate_trained_model(number, tokenized_text=b_news_sents)))

    # generate results
    data = read_birkbeck('./data/APPLING1DAT.643')
    results = {}
    for model in models:
        model_results = []
        for sentence in data:
            prediction = predictions(model=model[1], n=number, text=sentence[2])
            success_at_1, success_at_5, success_at_10 = success_at_k(correct_word=sentence[1],
                                                                     predictions_list=prediction)
            if success_at_1 or success_at_5 or success_at_10:
                print(sentence)

if __name__ == '__main__':
    main()
