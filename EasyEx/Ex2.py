def giaithua(n):
    if n == 0:
        return 1
    return n*giaithua(n - 1)

if __name__ == "__main__":
    n = int(input("Nhap n: "))
    print(giaithua(n))
      
