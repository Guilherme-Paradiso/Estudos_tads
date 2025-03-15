import pandas as pd #DATABASE FROM MOVIE

def create_movie():

    movie_df = pd.DataFrame({

        'movie_id': [18259, 24179, 35346, 41342, 56786, 62084, 42423],
        'Movies': ['Avengers', 'Avatar', 'Smurf', 'Orphan',
                     'Attack on Titan: The Last Attack', 'Love, Rosie','Senna'],
        'Genre': ['Action', 'Sci-Fi', 'Comedy', 'Thriller', 'Animation', 'Romance', 'Documentary'],
        'Director': ['Joss Whedon', 'James Cameron', 'Raja Gosnell', 'Jaume Collet-Serra', 'Yûichirô Hayashi', 'Christian Ditter', 'Asif Kapadia'],
        'Duraction (Minutes)': [143, 162, 104, 
                               123, 145, 102, 104],
        'release_date': ['2012-04-27', '2009-12-18', '2011-08-05', '2009-09-04', '2025-02-25',
                         '2015-03-05', '2010-11-12']

    })

    return movie_df

def create_user():

    user_df = pd.DataFrame({

        'user_id': [123, 635, 657, 867, 967, 823, 396],
        'Username': ['Guilherme', 'Mariana', 'Izabelle', 'Julia', 'Paulo', 'Fabio', 'Kilma'],
        'Email': ['ggg@gmail.com', 'mmm@gmail.com', 'iii@gmail.com', 'jjj@gmail.com', 'ppp@gmail.com', 'ppp@gmail.com', 'kkk@gmail.com'],
        'birth_date': pd.to_datetime(['2019-05-11', '2022-12-17', '2022-03-30', '2024-07-14', '2023-11-01', '2019-09-29', '2025-10-10'])

    })

    return user_df

def create_reviews():
    # Criando os dados para a tabela de reviews (comentários e avaliações)
    reviews_df = pd.DataFrame({

        'review_id': [1, 2, 3, 4, 5, 6, 7],
        'movie_id': [18259, 24179, 35346, 41342, 56786, 62084, 42423],
        'user_id': [123, 635, 657, 867, 967, 23, 396],
        'comment': ['Excellent movie!', 'Wonderful', 'Very funny', 'Tense and scary', 'Loved the plot', 'Romantic and fun', 'Must-see documentary'],
        'rating': [5, 4, 5, 4, 5, 4, 5]  # Notas de 1 a 5

    })

    return reviews_df