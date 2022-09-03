import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
import spacy
from textstat.textstat import textstatistics #legacy_round

'''In place of calling Get_data_to_analyse fns here we call key,value pair from
mongodb one by one creates a robust pipeline and creates less errors'''
#Data = Get_data_to_analyse()

)

sentimentList = []

def dataToProcess(i):
    article_data = str(Data[article_name[i]])
    return article_data

for i in range(0,len(Data)):
    article = dataToProcess(i)
#print(article)
    def break_sentences(article):
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(article)
        return list(doc.sents)

    def word_count(article):
        sentences = break_sentences(article)
        words = 0
        for sentence in sentences:
            words += len([token for token in sentence])
        return words
    print(word_count(article))


    def sentence_count(article):
        sentences = break_sentences(article)
        return len(sentences)
    print(sentence_count(article))

    def avg_sentence_length(article):
        words = word_count(article)
        sentences = sentence_count(article)
        average_sentence_length = float(words / sentences)
        return average_sentence_length
    print(avg_sentence_length(article))

    def syllables_count(word):
        return textstatistics().syllable_count(word)
    print(syllables_count(word_count(article)))

    # def avg_syllables_per_word(article):
    #     syllable = syllables_count(article)
    #     words = word_count(article)
    #     ASPW = float(syllable) / float(words)
    #     return legacy_round(ASPW, 1)
    # print(avg_syllables_per_word(article))

    def difficult_words(article):

        nlp = spacy.load('en_core_web_sm')
        doc = nlp(article)
        # Find all words in the text
        words = []
        sentences = break_sentences(article)
        for sentence in sentences:
            words += [str(token) for token in sentence]
        diff_words_set = set()

        for word in words:
            syllable_count = syllables_count(word)
            if word not in nlp.Defaults.stop_words and syllable_count >= 2:
                diff_words_set.add(word)

        return len(diff_words_set)
    print(difficult_words(article))

    def poly_syllable_count(article):
        count = 0
        words = []
        sentences = break_sentences(article)
        for sentence in sentences:
            words += [token for token in sentence]

        for word in words:
            syllable_count = syllables_count(word)
            if syllable_count >= 3:
                count += 1
        return count
    print(poly_syllable_count(article))

    def gunning_fog(text):
        per_diff_words = (difficult_words(text) / word_count(text) * 100) + 5
        grade = 0.4 * (avg_sentence_length(text) + per_diff_words)
        return grade
    print(gunning_fog(article))

    def dale_chall_readability_score(text):
        """
            Implements Dale Challe Formula:
            Raw score = 0.1579*(PDW) + 0.0496*(ASL) + 3.6365
            Here,
                PDW = Percentage of difficult words.
                ASL = Average sentence length
        """
        words = word_count(text)
        # Number of words not termed as difficult words
        count = word_count - difficult_words(text)
        if words > 0:
            # Percentage of words not on difficult word list

            per = float(count) / float(words) * 100

        # diff_words stores percentage of difficult words
        diff_words = 100 - per

        raw_score = (0.1579 * diff_words) + \
                    (0.0496 * avg_sentence_length(text))

        # If Percentage of Difficult Words is greater than 5 %, then;
        # Adjusted Score = Raw Score + 3.6365,
        # otherwise Adjusted Score = Raw Score

        if diff_words > 5:
            raw_score += 3.6365

        return legacy_round(score, 2)
    print(dale_chall_readability_score(article))
#nltk analysis
#1 removing stopwords
    def preProcesstext(article):
        stop_words = set(stopwords.words('english'))
        wnl = WordNetLemmatizer()
        tokenizer = RegexpTokenizer(r"\w+")
        word_tokens = tokenizer.tokenize(article)
        filtered_article = [w for w in word_tokens if not w.lower() in stop_words]
        filtered_article = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_article.append(w)
        return filtered_article

    vader_text = preProcesstext(article)
    print(vader_text)

    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    import pandas as pd

    column=['text']
    df_SI = pd.DataFrame(vader_text,columns=column)

    vader = SentimentIntensityAnalyzer()
    neg_score = lambda text: vader.polarity_scores(text)['neg']
    df_SI['neg'] = df_SI['text'].apply(neg_score)
    neu_score = lambda text: vader.polarity_scores(text)['neu']
    df_SI['neu'] = df_SI['text'].apply(neu_score)
    pos_score = lambda text: vader.polarity_scores(text)['pos']
    df_SI['pos'] = df_SI['text'].apply(pos_score)
    comp_score = lambda text: vader.polarity_scores(text)['compound']
    df_SI['compound'] = df_SI['text'].apply(comp_score)

    Negative = df_SI['neg'].sum()
    print(Negative)
    Neutral = df_SI['neu'].sum()
    print(Neutral)
    Positive = df_SI['pos'].sum()
    print(Positive)
    Compound = df_SI['compound'].sum()
    print(Compound)

    # sentimentList.append(sum)
    # print(sentimentList)
    # if sum > 0:
    #     print("this is a positive text")
    # else:
    #     print("this is a negative text")