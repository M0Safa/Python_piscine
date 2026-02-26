import sys


def main():
    num = len(sys.argv)
    scores = []
    print("=== Player Score Analytics ===")
    if num == 1:
        print("No scores provided. Usage: python3",
              " ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            for score in sys.argv[1:]:
                scores.append(int(score))
            average = sum(scores) / (num - 1)
            print("Scores processed:", scores)
            print("Total players:", num - 1)
            print("Total score:", sum(scores))
            print(f"Average score: {average:.1f}")
            print("High score:", max(scores))
            print("Low score:", min(scores))
            print("Score range:", max(scores) - min(scores))
        except ValueError:
            print(f"oops, you typed {score} instead of an int")


main()
