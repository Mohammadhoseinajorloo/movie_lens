from dataset.reader import Reader

if __name__ == "__main__":
    links = Reader('links.csv').reader()
    print(links.info())
