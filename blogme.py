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

# Calculate the average negative and positive sentiment scores
avg_negative_sentiment = title_neg_sentiment.mean()
avg_positive_sentiment = title_pos_sentiment.mean()

# Print the average sentiment scores
print("Average Negative Sentiment Score:", avg_negative_sentiment)
print("Average Positive Sentiment Score:", avg_positive_sentiment)

# Create empty lists to store sentiment scores
title_sentiments = []

# Loop through each title in the dataset
for i in range(len(data)):
    try:
        # Get the title text
        text = data['title'][i]
        
        # Analyze the sentiment of the title
        sent = sent_int.polarity_scores(text)
        
        # Append the sentiment scores to the list
        title_sentiments.append(sent)
        
    except:
        # Handle exceptions (e.g., if the text is empty)
        title_sentiments.append({'neg': 0, 'neu': 0, 'pos': 0, 'compound': 0})

# Convert the list of sentiment scores to a DataFrame
sentiments_df = pd.DataFrame(title_sentiments)

# Calculate the overall positive, negative, and neutral sentiments in percentages
total_titles = len(data)
positive_score = sentiments_df['pos'].sum()
negative_score = sentiments_df['neg'].sum()
neutral_score = sentiments_df['neu'].sum()

# Print the percentages
print("Overall Positive Sentiment:", positive_score)
print("Overall Negative Sentiment:", negative_score)
print("Overall Neutral Sentiment:", neutral_score)

# Save the updated DataFrame to a new Excel file
data.to_excel('blogme_cleaned_with_sentiment.xlsx', sheet_name='blogmedata', index=False)
















