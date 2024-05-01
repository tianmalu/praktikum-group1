# Intel compiler
CC =  icc
CFLAGS = -O0

CFLAGS_O2 = -O2
CFLAGS_O3 = -O3 -fno-alias -xhost

MPICC = mpicc

all: heat_O2 heat_O3

heat_O2 : CFLAGS = $(CFLAGS_O2)
heat_O2 : heat

heat_O3 : CFLAGS = $(CFLAGS_O3)
heat_O3 : heat

heat : heat.o input.o misc.o timing.o relax_gauss.o relax_jacobi.o
	$(CC) $(CFLAGS) -o $@ $+ -lm 

%.o : %.c heat.h timing.h input.h
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f *.o heat_O2 heat_O3 *~ *.ppm

remake : clean all
