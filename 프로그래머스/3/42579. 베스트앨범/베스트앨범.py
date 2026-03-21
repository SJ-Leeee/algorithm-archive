def solution(genres, plays):
    streaming_genre = {}
    genre_songs = {}

    for i in range(len(genres)):
        genre = genres[i]
        stream_cnt = plays[i]
        if genre in streaming_genre:  # 장르에 이미 들어온게 있다는 뜻
            streaming_genre[genre] += stream_cnt
            genre_songs[genre].append((i, stream_cnt))  # 장르에 곡추가
        else:
            streaming_genre[genre] = stream_cnt
            genre_songs[genre] = [(i, stream_cnt)]

    sorted_genre = sorted(streaming_genre.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for i in sorted_genre:
        genre = i[0]
        genre_songs[genre].sort(key=lambda x: x[1], reverse=True)
        if len(genre_songs[genre]) < 2:
            for i in genre_songs[genre]:  # (0,500, 2,150)
                answer.append(i[0])
        else:
            for i in range(2):  # (0,500, 2,150)
                answer.append(genre_songs[genre][i][0])

    return answer