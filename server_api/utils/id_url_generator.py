# id_url_generator.py created by sylvi at 2021/4/30 11:39 AM
import math

class UrlID():
    ALPHABET = "bcdfghjklmnpqrstvwxyz0123456789BCDFGHJKLMNPQRSTVWXYZ"
    BASE = len(ALPHABET)
    MAXLEN = 6

    def encode_id(self, n):

        pad = self.MAXLEN - 1
        n = int(n + pow(self.BASE, pad))

        s = []
        t = int(math.log(n, self.BASE))
        while True:
            bcp = int(pow(self.BASE, t))
            a = int(n / bcp) % self.BASE
            s.append(self.ALPHABET[a:a+1])
            n = n - (a * bcp)
            t -= 1
            if t < 0: break

        return "".join(reversed(s))

    def decode_id(self, n):

        n = "".join(reversed(n))
        s = 0
        l = len(n) - 1
        t = 0
        while True:
            bcpow = int(pow(self.BASE, l - t))
            s = s + self.ALPHABET.index(n[t:t+1]) * bcpow
            t += 1
            if t > l: break

        pad = self.MAXLEN - 1
        s = int(s - pow(self.BASE, pad))

        return int(s)

if __name__=="__main__":
    print(alphaID(1))