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


def save_model(path: str, model):
    file = open(path, "wb")
    dill.dump(model, file)
    file.close()
    print("model saved successfully at " + path)


def load_model(path):
    file = open(path, 'rb')
    model = dill.load(file)
    file.close()
    print("model loaded successfully from " + path)
    return model


def predictions(model, n, text):
    sentence = text.split(' ')
    sentence = pad_both_ends(sentence, n=n)
    results = []
    for item in model.counts[sentence[sentence.index('*') - n:sentence.index('*')]]:
        results.append(item)

    return results

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
