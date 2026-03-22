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


# sort는 디폴트가 오름차순이다.


# 장르는 dict로 스트리밍 횟수 기억
# 각 노래들에 대한 dict: list = [고유번호, 스트리밍횟수] 도 생성.

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
# 22분


"""
def solution(genres, plays):
    streaming_genre = {}
    genre_songs = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        streaming_genre[genre] = streaming_genre.get(genre, 0) + play
        genre_songs.setdefault(genre, []).append((i, play))

    sorted_genre = sorted(streaming_genre.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for genre, _ in sorted_genre:
        genre_songs[genre].sort(key=lambda x: (-x[1], x[0]))
        for song in genre_songs[genre][:2]:
            answer.append(song[0])

    return answer
"""
