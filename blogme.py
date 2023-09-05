import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
data = pd.read_excel('articles.xlsx')

#summary of data
data.describe()

#column summary
data.info()

#counting the no of articles per source
#format to groupby: df.groupby(['column_to_group])['column_to_count'].count()
data.groupby(['source_id'])['article_id'].count()

#no.of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping a column
data = data.drop('engagement_comment_plugin_count' , axis=1)

#creating a keyword flag
keyword = 'crash'

#creating for loop for isolating each title row
# length = len(data)
# keyword_flag = []
# for x in range(0,length):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)
    
#Creating a function

def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag = keywordflag("support")

data['keyword_flag'] = pd.Series(keywordflag)

#sentiment intensity analyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg  = sent['neg']
pos  = sent['pos']
neu  = sent['neu']

#adding for loop to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)
for i in range (0,length):
    try:
        text = data['title'][i]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg  = sent['neg']
        pos  = sent['pos']
        neu  = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment
#writinng the data

data.to_excel('blogme_cleaned.xlsx' , sheet_name = 'blogmedata', index = False)







