class Solution:
    def myPow(self, x: float, n: int) -> float:
        p=abs(n)
        if p==0:
            return 1
        half=self.myPow(x,p//2)
        if p%2==0:
            if n>0:
                return half*half
            else:
                return 1/(half*half)
        else:
            if n>0:
                return half*half*x
            else:
                return 1/(half*half*x)
        

        