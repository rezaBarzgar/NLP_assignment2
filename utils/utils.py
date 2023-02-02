from nltk.lm.preprocessing import pad_both_ends, padded_everygram_pipeline
from nltk.lm import MLE
from nltk.corpus import brown
import nltk
import dill


def generate_trained_model(n, tokenized_text):
    train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)
    model = MLE(n)
    model.fit(train_data, padded_sents)
    return model


def save_model(path: str, model: nltk.lm.MLE):
    file = open(path, "wb")
    dill.dump(model, file)
    file.close()
    print("model saved successfully at " + path)


def load_model(path: str):
    file = open(path, 'rb')
    model = dill.load(file)
    file.close()
    print("model loaded successfully from " + path)
    return model


def predictions(model: nltk.lm.MLE, n, text: str):
    sentence = list(pad_both_ends(text, n=n))
    results = []
    start = sentence.index('*') - n if n<sentence.index('*') else 0
    end = sentence.index('*')
    for item in model.counts[sentence[start:end]]:
        results.append(item)

    return results


def read_birkbeck(path: str):
    with open(path, 'r') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            if line[0] == '$':
                continue
            temp = line.lower().split()
            data.append((temp[0], temp[1], temp[2:]))  # Tuple consist of Misspelled word, Correct word, sentence
        return data


def success_at_k(correct_word: str, predictions_list: list):
    success_at_1 = 0
    success_at_5 = 0
    success_at_10 = 0
    if len(predictions_list) == 0:
        return success_at_1, success_at_5, success_at_10
    if predictions_list[0] == correct_word:
        success_at_1 = 1
        success_at_5 = 1
        success_at_10 = 1
        return success_at_1, success_at_5, success_at_10
    for word in predictions_list[1:5]:
        if word == correct_word:
            success_at_5 = 1
            success_at_10 = 1
            return success_at_1, success_at_5, success_at_10
    for word in predictions_list[5:]:
        if word == correct_word:
            success_at_10 = 1
            return success_at_1, success_at_5, success_at_10

    return success_at_1, success_at_5, success_at_10


if __name__ == '__main__':
    # nltk.download('brown')
    print(brown.sents(categories='news')[1])
    # b_news_sents = [[y.lower() for y in x] for x in brown.sents(categories='news')]
    # my_model = generate_trained_model(n=3, tokenized_text=b_news_sents)
    # save_model('./mdl.pkl', my_model)
    model = load_model('./mdl.pkl')
    results = []
    for item in model.counts[['<s>']]:
        print(item)
    print(results)
