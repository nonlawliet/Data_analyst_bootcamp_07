# Web Scraping from IMDB top 50 movies
!pip install gazpacho

from gazpacho import Soup
from requests import get

url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"

headers = {"Accept-Language": "en-US"}

get(url, headers = headers)

response = get(url)
response.text

imdb = Soup(response.text)
type(imdb)

### <h3 class="lister-item-header">
imdb.find("h3", {"class": "lister-item-header"})[0].strip()

### <span class="certificate">R</span>
imdb.find("span", {"class": "certificate"})[0].strip()

### <span class="runtime">142 min</span>
imdb.find("span", {"class": "runtime"})[0].strip()

### <span class="genre">Drama            </span>
imdb.find("span", {"class": "genre"})[0].strip()

### <div class="inline-block ratings-imdb-rating" name="ir" data-value="9.3">
imdb.find("div", {"class": "inline-block ratings-imdb-rating"})[0].strip()


title_list = imdb.find("h3", {"class": "lister-item-header"})
rating_list = imdb.find("span", {"class": "certificate"})
runtime_list = imdb.find("span", {"class": "runtime"})
genre_list = imdb.find("span", {"class": "genre"})
score_list = imdb.find("div", {"class": "inline-block ratings-imdb-rating"})

titles = [title.strip() for title in title_list]
print(type(titles), titles)

ratings = [rating.strip() for rating in rating_list]
runtimes = [runtime.strip() for runtime in runtime_list]
genres = [genre.strip() for genre in genre_list]
scores = [float(score.strip()) for score in score_list]

# Convert to DataFrame

import pandas as pd

df = pd.DataFrame({
    "title": titles,
    "ratings": ratings,
    "runtime": runtimes,
    "genre": genres,
    "score": scores
})

df.head()

df['year'] = df['title'].str[-5:-1]
df['title'] = df['title'].str.replace(r'^\d+\.\s+', '')
df['runtime'] = df['runtime'].str.replace(r'min', '')
df['title'] = df['title'].str[ :-7]

df['runtime'] = [int(runtime) for runtime in df['runtime']]
df['year'] = [int(year) for year in df['year']]

### Check Na
df.isna().sum()

# Analysis part
## average runtime and score of movie by ratings
round(df.groupby('ratings')[['runtime', 'score']].mean().reset_index(), 2)

## Evolution of movie runtime over years
import matplotlib.pyplot as plt

df_sort = df.sort_values('year');
plt.scatter(x=df_sort['year'], y=df_sort['runtime']);
plt.xlabel("Year");
plt.ylabel("Runtime");
plt.xticks(range(df_sort['year'].min(), df_sort['year'].max(), 20))
plt.show()

## Evolution of movie score over years
plt.scatter(x=df_sort['year'], y=df_sort['score']);
plt.xlabel("Year");
plt.ylabel("Score");
plt.xticks(range(df_sort['year'].min(), df_sort['year'].max(), 20))
plt.show()

## Which genres is the most popular by score
### group by genre, use this df
df_split_genre = df
df_split_genre['new_genre'] = df_split_genre['genre'].str.split(', ')
df_split_genre = df_split_genre.explode('new_genre')

group_new_genre = round(df_split_genre.groupby('new_genre')['score'].mean(), 2).reset_index()

group_new_genre.sort_values('score', ascending=False).head(10)

## Which movie genre has produced the most
df_split_genre['new_genre'].value_counts().reset_index()
