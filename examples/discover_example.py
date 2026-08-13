from pattern_engine.discovery.search import Discovery

if __name__ == '__main__':
    seq = [1,4,9,16,25,36]
    d = Discovery()
    print(d.discover(seq))
