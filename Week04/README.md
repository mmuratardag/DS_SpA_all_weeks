# Week 4 Project:

## Text Classification with Song Lyrics

- Learned to implement basic web-scraping applications using different Python libraries like requests, re, BeautifulSoup & scrapy
- Learned to implement basic bag-of-words approaches
- Learned to implement basic corpus-prep / text pre-processing
- Learned to implement basic CLI applications using argparse library
- Working on improving writing Python functions making Python code modular

### For the weekly project

- Scraped 2146 song lyrics (1049 indie & 1097 punk) by 25 artists
- Prepped corpus by
  - lemmatizing with spaCy
  - removing stopwords, using regex to strip off numbers, symbols etc.
  - trimming the corpus
- Relied on tf-idf for getting the dfm
- Trained a model with RandomForestClassifier

See the project folder <a href="" target="_blank">here</a> to get the trained model and use it for prediction with CLI.

![](CLI_screen-shot.png)

### TO-DO

- Maybe collect more data and turn the project into a little fun web-application in the long run.
