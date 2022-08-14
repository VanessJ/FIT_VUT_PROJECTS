#// # Makefile
#// # Riešenie IJC-DU2, 15.4.2020
#// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
#// # Preloženie: gcc 7.4.0
#// # Zostavenie: IJC-DU2

CC =gcc
CFLAGS=-std=c99 -pedantic -Wall -Wextra -g

all:tail  libhtab.a libhtab.so wordcount-dynamic wordcount

wordcount-dynamic: wordcount.o io.o libhtab.so
	$(CC) $(CFLAGS) $^ -o $@

wordcount: wordcount.o io.o libhtab.a
	$(CC) $(CFLAGS) $^ -o $@
wordcount.o: wordcount.c
	$(CC) $(CFLAGS) -c $<
io.o: io.c io.h
	$(CC) $(CFLAGS) -c $<

############  TAIL  ############ 

tail:tail.o
	$(CC) $(CFLAGS) tail.o -o tail
tail.o:tail.c
	$(CC) $(CFLAGS) -c tail.c -o tail.o

############  LIBRARIES  ############ 

libhtab.a: htab_begin.o htab_bucket_count.o htab_clear.o htab_end.o  htab_erase.o htab_find.o htab_free.o htab_hash_fun.o htab_init.o htab_iterator_get_key.o htab_iterator_get_value.o iterator_set.o htab_iterator_next.o htab_iterator_set_value.o htab_lookup_add.o  htab_size.o 
	ar rcs $@ $^

libhtab.so: htab_begin.o htab_bucket_count.o htab_clear.o htab_end.o htab_erase.o htab_find.o htab_free.o htab_hash_fun.o htab_init.o htab_iterator_get_key.o htab_iterator_get_value.o iterator_set.o htab_iterator_next.o htab_iterator_set_value.o htab_lookup_add.o htab_size.o
	$(CC) $(CFLAGS) -fPIC -shared $^ -o $@

htab_begin.o: htab_begin.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_bucket_count.o: htab_bucket_count.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_clear.o: htab_clear.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_end.o: htab_end.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_erase.o: htab_erase.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_find.o: htab_find.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_free.o: htab_free.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_hash_fun.o: htab_hash_fun.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_init.o: htab_init.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_iterator_get_key.o: htab_iterator_get_key.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_iterator_get_value.o: htab_iterator_get_value.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

iterator_set.o: iterator_set.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_iterator_next.o: htab_iterator_next.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_iterator_set_value.o: htab_iterator_set_value.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_lookup_add.o: htab_lookup_add.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

htab_size.o: htab_size.c htab.h hstruct.h
	$(CC) $(CFLAGS) -fPIC -c $<

.PHONY: clean
clean:
	rm -f *.o tail wordcount wordcount-dynamic 