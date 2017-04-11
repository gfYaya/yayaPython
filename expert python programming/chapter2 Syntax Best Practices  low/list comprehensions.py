# coding = utf-8

# some exercise about enumerate
if __name__ == '__main__':
    seq=["one","two","three"]

    i = 0
    for element in seq:
        seq[i] = '%d: %s' % (i, seq[i])
        i += 1
    print(seq)

    seq = ["one", "two", "three"]
    for i,element in enumerate(seq):
        seq[i] = '%d: %s' % (i, seq[i])
    print(seq)

    def _treatment(pos, element) :
        return '%d: %s' % (pos, element)
    seq = ["one", "two", "three"]
    # print([ _treatment(i,seq[i]) for i,seq[i] in enumerate(seq)]) # ['0: three', '1: three', '2: three']
    print([_treatment(i,el)  for i,el in enumerate(seq)])


