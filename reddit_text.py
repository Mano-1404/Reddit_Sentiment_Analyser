{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'praw'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpraw\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mvaderSentiment\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mvaderSentiment\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m SentimentIntensityAnalyzer\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmatplotlib\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpyplot\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mplt\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'praw'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import praw\n",
    "from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Initialize Reddit API\n",
    "reddit = praw.Reddit(client_id='8QWHora2LrjLtsSVMGXt4g',\n",
    "                     client_secret='OjbA9HvEsgNeSs8jciHBBKjoo5Foig',\n",
    "                     user_agent='praw_scraper_1.0')\n",
    "\n",
    "# Function to perform sentiment analysis using VADER\n",
    "def analyze_sentiment(comment):\n",
    "    analyzer = SentimentIntensityAnalyzer()\n",
    "    score = analyzer.polarity_scores(comment)\n",
    "    compound_score = score['compound']\n",
    "    if compound_score >= 0.05:\n",
    "        return 'Positive'\n",
    "    elif compound_score <= -0.05:\n",
    "        return 'Negative'\n",
    "    else:\n",
    "        return 'Neutral'\n",
    "\n",
    "# Streamlit app\n",
    "def main():\n",
    "    st.title(\"Reddit Comments Sentiment Analyzer\")\n",
    "    st.write(\"made by - Harry & Harika\")\n",
    "\n",
    "    # Input field for Reddit post URL\n",
    "    reddit_post_url = st.text_input(\"Enter Reddit Post URL:\")\n",
    "\n",
    "    if reddit_post_url:\n",
    "        try:\n",
    "            # Get Reddit post and comments\n",
    "            submission = reddit.submission(url=reddit_post_url)\n",
    "            submission.comments.replace_more(limit=None)\n",
    "            all_comments = submission.comments.list()\n",
    "            \n",
    "            comments = all_comments[-20:]\n",
    "\n",
    "            # Perform sentiment analysis and store results\n",
    "            sentiments = [analyze_sentiment(comment.body) for comment in comments]\n",
    "\n",
    "            # Generate pie chart\n",
    "            sentiment_counts = {\n",
    "                'Positive': sentiments.count('Positive'),\n",
    "                'Negative': sentiments.count('Negative'),\n",
    "                'Neutral': sentiments.count('Neutral')\n",
    "            }\n",
    "\n",
    "            # Plot pie chart\n",
    "            labels = sentiment_counts.keys()\n",
    "            sizes = sentiment_counts.values()\n",
    "            fig, ax = plt.subplots()\n",
    "            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)\n",
    "            ax.axis('equal')\n",
    "            st.pyplot(fig)\n",
    "\n",
    "            # Display sentiment analysis results\n",
    "            st.subheader(\"Sentiment Analysis Results:\")\n",
    "            st.write(sentiment_counts)\n",
    "\n",
    "            # Display last 10 comments\n",
    "            st.subheader(\"Last 10 Comments:\")\n",
    "            for i, comment in enumerate(comments[:10]):\n",
    "                st.write(f\"Comment {i+1}: {comment.body}\")\n",
    "                st.write(f\"Sentiment: {analyze_sentiment(comment.body)}\")\n",
    "\n",
    "        except Exception as e:\n",
    "            st.error(f\"Error: {str(e)}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "bdaenv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
