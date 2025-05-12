import ran
import time

def sortear_numeros(quantidade=6, intervalo=(1, 60)):
    numeros_sorteados = set()
    print("Sorteando números...")
    while len(numeros_sorteados) < quantidade:
        time.sleep(0.5)  # Simula tempo de espera do sorteio
        num = random.randint(*intervalo)
        if num not in numeros_sorteados:
            numeros_sorteados.add(num)
            print(f"Número sorteado: {num}")
    return sorted(numeros_sorteados)

def main():
    while True:
        print("\n=== Sorteio Mega-Sena ===")
        resultado = sortear_numeros()
        print("\nNúmeros sorteados (em ordem):", resultado)

        repetir = input("\nDeseja fazer outro sorteio? (s/n): ").lower()
        if repetir != 's':
            print("Encerrando sorteios. Boa sorte!")
            break

if __name__ == "__main__":
    main()
