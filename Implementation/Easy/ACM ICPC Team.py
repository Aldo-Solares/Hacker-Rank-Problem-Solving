
#LINK https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true

def acmTeam(topic):
    max_topics = 0
    team_count = 0

    n = len(topic)
    m = len(topic[0])

    for i in range(n):
        for j in range(i + 1, n):
            combined = bin(int(topic[i], 2) | int(topic[j], 2))
            known_topics = combined.count('1')

            if known_topics > max_topics:
                max_topics = known_topics
                team_count = 1
            elif known_topics == max_topics:
                team_count += 1

    return [max_topics, team_count]

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print("\n".join(map(str, result)))