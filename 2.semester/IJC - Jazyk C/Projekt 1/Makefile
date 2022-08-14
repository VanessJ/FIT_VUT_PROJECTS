# Makefile
# Riešenie IJC-DU1, 17.3.2020
# Autor: Vanessa Jóriová, xjorio00, VUT FIT
# Preložené: gcc 7.4.0
# Zostavenie IJC-DU1

LC_ALL=cs_CZ.utf8
CFLAGS= -O2 -std=c11 -pedantic	-Wall -Wextra

all: primes primes-i steg-decode 

run: primes primes-i
	./primes
	./primes-i


primes: primes.o eratosthenes.o error.o
	$(CC) $(CFLAGS) primes.o eratosthenes.o error.o -lm -o $@

primes-i: primes-i.o eratosthenes-i.o error.o
	$(CC) $(CFLAGS) primes-i.o eratosthenes-i.o error.o -lm -o $@

steg-decode: steg-decode.o eratosthenes.o error.o ppm.o
	$(CC) $(CFLAGS) steg-decode.o eratosthenes.o error.o ppm.o -lm -o $@
	

primes.o: primes.c bitset.h eratosthenes.h
	$(CC) $(CFLAGS) -c primes.c -o $@

primes-i.o: primes.c bitset.h eratosthenes.h
	$(CC) $(CFLAGS) -DUSE_INLINE -c primes.c -o $@

eratosthenes.o: eratosthenes.c eratosthenes.h bitset.h 
	$(CC) $(CFLAGS) -c eratosthenes.c -o $@

eratosthenes-i.o: eratosthenes.c eratosthenes.h bitset.h 
	$(CC) $(CFLAGS) -DUSE_INLINE -c eratosthenes.c -o $@


steg-decode.o: steg-decode.c ppm.h eratosthenes.h error.h 
	$(CC) $(CFLAGS) -c steg-decode.c -o $@

bitset.h: error.o

error.o: error.c error.h
	$(CC) $(CFLAGS) -c error.c -o $@

ppm.o: ppm.c ppm.h error.h
	$(CC) $(CFLAGS) -c ppm.c -o $@

clean:
	rm -f *.o primes primes-inline steg-decode