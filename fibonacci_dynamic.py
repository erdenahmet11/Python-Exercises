def fibonacci_seq_generator(number_of_terms):
    fibonacci_seq = [0, 1]

    for i in range(2, number_of_terms + 1):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])
    return fibonacci_seq

number_of_terms = int(input("Type how many terms of the Fibonacci sequence you want to see: "))
fibonacci_seq = fibonacci_seq_generator(number_of_terms)
print(fibonacci_seq)

