def bruteforce_pin():
    for pin in range(1000, 10000):
        if pin % 13 == 0:
            return pin

def divide_and_conquer():
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    pin = int(f"{a}{b}{c}{d}")
                    if pin % 13 == 0:
                        return pin

def heuristic_approach():
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    for pin in range(1000, 10000):
        if pin % 13 == 0 and is_prime(pin):
            return pin

def main():
    print("Hledání PINu pomocí hrubé síly...")
    brute_force_pin = bruteforce_pin()
    print("PIN nalezen pomocí hrubé síly:", brute_force_pin)

    print("\nHledání PINu pomocí rozděl a panuj...")
    divide_and_conquer_pin = divide_and_conquer()
    print("PIN nalezen pomocí rozděl a panuj:", divide_and_conquer_pin)

    print("\nHledání PINu pomocí heuristického přístupu...")
    heuristic_pin = heuristic_approach()
    print("PIN nalezen pomocí heuristického přístupu:", heuristic_pin)

if __name__ == "__main__":
    main()
