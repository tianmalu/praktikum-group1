# Intel compiler
CC =  icc
CFLAGS = -O0
CFLAGS_O2 = -O2
CFLAGS_O3 = -O3 -fno-alias -xhost

MPICC = mpicc

all: heat_O3


heat_O2 : heat.o input.o misc.o timing.o relax_gauss.o relax_jacobi.o
        $(CC) $(CFLAGS_O2) $(PAPI_INC) -o $@ $+ -lm $(PAPI_LIB)

heat_O3 : heat.o input.o misc.o timing.o relax_gauss.o relax_jacobi.o
        $(CC) $(CFLAGS_O3)  $(PAPI_INC) -o $@ $+ -lm $(PAPI_LIB)


%.o : %.c heat.h timing.h input.h
        $(CC) $(CFLAGS) $(PAPI_INC) -c -o $@ $<  $(PAPI_LIB)

clean:
        rm -f *.o heat heat_O2 heat_O3 *~ *.ppm

remake : clean all