import numpy as np

def ParseWeightFile(path, N):
    W = np.zeros((N, N), dtype=np.float32)
    with open(path, mode="r") as input:
        lines = input.read().splitlines()
    for line in lines:
        strings = line.split()
        i, j, w = int(strings[0])-1, int(strings[1])-1, float(strings[2])
        if i < N and j < N:
            W[i,j] = w
            W[j,i] = w
    return W

def ConvertClassToString(cls):
    res = ""
    for c in cls:
        res += "A " if c == cls[0] else "B "
    return res

def SaveOutcome(e, cls, N):
    with open(f"{N}_sol_E.txt", mode="w") as output:
        output.write(str(e) + "\n")
    with open(f"{N}_sol_class.txt", mode="w") as output:
        output.write(ConvertClassToString(cls) + "\n")


class Solution:
    def __init__(self, N, W):
        self.N = N
        self.W = W

    @staticmethod
    def GetEValue(eVector):
        return eVector.sum() / 2

    @staticmethod
    def GetTransferedStudent(eVector):
        return np.argmin(eVector)

    @staticmethod
    def adjust(S, eVector, adjustedNumber):
        sorted_index = np.argsort(eVector)
        for i in range(adjustedNumber):
            S[sorted_index[i]]  *= -1
        return S

    def GetLocalOptimum(self, S):
        ePrevious = -1e6
        E = np.matmul(self.W, S) * S
        eGrand = Solution.GetEValue(E)
        while eGrand > ePrevious:
            ePrevious = eGrand
            transferedStudent = Solution.GetTransferedStudent(E)
            S[transferedStudent] *= -1
            E = np.matmul(self.W, S) * S
            eGrand = Solution.GetEValue(E)
    
        eGrand = ePrevious
        S[transferedStudent] *= -1
        return eGrand, S

    def Solve(self):
        eGrandMax = -1e6
        adjustedNumber = 2
        s0 = np.ones(self.N) # initial guess

        # start iteration
        iteration = 0
        while adjustedNumber < self.N:
            eGrand, s0 = self.GetLocalOptimum(s0)
            if eGrand > eGrandMax:
                S = s0
                E = np.matmul(self.W, S) * S
                eGrandMax = eGrand
                adjustedNumber = 2

            s0 = Solution.adjust(S.copy(), E, adjustedNumber)
            adjustedNumber += 1
            iteration += 1
        
        print(iteration)
        return eGrandMax, S

def test():
    N = 4
    W = ParseWeightFile("w4.txt", N)
    sol = Solution(N, W)
    eGrand, S = sol.Solve()
    print(round(eGrand, ndigits=4), ConvertClassToString(S.tolist()))
    # SaveOutcome(round(eGrand, ndigits=4), S.tolist(), N)

def main():
    N = 101
    W = ParseWeightFile("w101.txt", N)
    sol = Solution(N, W)
    eGrand, S = sol.Solve()
    print(round(eGrand, ndigits=4), ConvertClassToString(S.tolist()))
    # SaveOutcome(round(eGrand, ndigits=4), S.tolist(), N)

if __name__ ==  "__main__":
    # test()
    main()