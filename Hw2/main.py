# created by Hen Shiryon

# written by Bar Zada and Hen Shiryon



# ex1 A:
class Ex1:
    def __init__(self, x):
        self.current = 2
        self.x = x

    def PrimeCheck(self):

        return len([num for num in range(2, self.current) if self.current % num == 0]) == 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.x:
            raise StopIteration
        else:
            while not self.PrimeCheck():
                if self.current + 1 > self.x:
                    raise StopIteration
                self.current += 1
            else:
                self.current += 1

            return self.current - 1


# exB:
def PrimeCheck(n):
    return len([num for num in range(2, n) if n % num == 0]) == 0


def Ex1B(n):
    x = 2
    while x < n + 1:
        if PrimeCheck(x):
            yield x
        x += 1


# ex2
def Ex2(n):
    print([x for x in range(2, n) if n % x == 0])


# ex3
def primeNumbers(m, n):
    print(["prime" if len([x for x in range(2, item) if item % x == 0]) == 0 else "not prime" for item in
           range(m, n + 1)])


# ex4
def check(number):
    digit1 = number % 10
    digit2 = number // 10 % 10

    return digit1 % digit2 == 0 and number % 2 == 0


def numbers(m, n):
    while m < n + 1:
        if check(m):
            yield m
        m += 1


# ex5
def letters(word):
    return {ch: word.count(ch) for ch in word}


# ex6A
def checkLenStringsGenerator(word1, word2):
    if len(word1) > len(word2):
        word1 = word1[:len(word2)]
    elif len(word1) < len(word2):
        word2 = word2[:len(word1)]
    for i, j in zip(word1, word2):
        if i == j:
            yield i


# ex6B
class stringsCheckIter:

    def __init__(self, word1, word2):
        self.current = 0
        self.word1 = word1[:len(word1)]
        self.word2 = word2[:len(word2)]

    def __iter__(self):
        return self

    def __next__(self):

        if self.current >= len(self.word1) or self.current >= len(self.word2):
            raise StopIteration
        else:
            while self.word1[self.current] != self.word2[self.current]:
                if self.current >= len(self.word1) or self.current >= len(self.word2):
                    raise StopIteration
                self.current += 1
            else:
                self.current += 1

            return self.word1[self.current - 1]


# ex7

def stringBuild(numbers, chars):
    return " ".join([chars[i - 1] for i in numbers])


if __name__ == '__main__':
    # Ex1A
    # c = Ex1(30)
    # for i in c:
    #     print(i, end=" ")

    # Ex1B
    # prime_generator = Ex1B(20)
    #
    # for item in prime_generator:
    #     print(item, end=" ")
    #
    # print()

    # Ex2(30)

   # ex3
   #  primeNumbers(20, 30)

    # ex4

    # for item in numbers(30, 40):
    #     print(item, end=" ")
    # print()

    # ex5
    # x = letters("abcdefghijklmno")
    # for key, value in x.items():
    #     print(key, value)

    # ex6A
    # for i in checkLenStringsGenerator("tik","kit"):
    #     print(i, end=" ")

    # ex6B
    # for i in stringsCheckIter("123", "321"):
    #     print(i, end=" ")
    #     print()

    # ex7
    # print(stringBuild([1, 5, 3, 6, 2, 4], ['a', 'h', 'f', 'e', 'y', 'u']))
