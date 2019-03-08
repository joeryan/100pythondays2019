class RecordScore():
    def __init__(self):
        self.max_score = 0

    def __call__(self, new_score):
        if new_score > self.max_score:
            self.max_score = new_score
        return self.max_score


def main():
    pass


if __name__ == '__main__':
    main()
