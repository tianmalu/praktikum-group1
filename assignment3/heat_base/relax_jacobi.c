/*
 * relax_jacobi.c
 *
 * Jacobi Relaxation
 *
 */

#include "heat.h"

#define min(a,b) ((a) < (b) ? (a) : (b))
/*
 * Residual (length of error vector)
 * between current solution and next after a Jacobi step
 */
double residual_jacobi(double *u, unsigned sizex, unsigned sizey) {
	unsigned i, j;
	double unew, diff, sum = 0.0;

	for (j = 1; j < sizex - 1; j++) {
		for (i = 1; i < sizey - 1; i++) {
			unew = 0.25 * (u[i * sizex + (j - 1)] +  // left
						u[i * sizex + (j + 1)] +  // right
						u[(i - 1) * sizex + j] +  // top
						u[(i + 1) * sizex + j]); // bottom

			diff = unew - u[i * sizex + j];
			sum += diff * diff;
		}
	}

	return sum;
}

/*
 * One Jacobi iteration step
 */
void relax_jacobi(double *u, double *utmp, unsigned sizex, unsigned sizey) {
	int i, j;

	for (j = 1; j < sizex - 1; j++) {
		for (i = 1; i < sizey - 1; i++) {
			utmp[i * sizex + j] = 0.25 * (u[i * sizex + (j - 1)] +  // left
						u[i * sizex + (j + 1)] +  // right
						u[(i - 1) * sizex + j] +  // top
						u[(i + 1) * sizex + j]); // bottom
		}
	}

	// copy from utmp to u

	// for (j = 1; j < sizex - 1; j++) {
	// 	for (i = 1; i < sizey - 1; i++) {
	// 		u[i * sizex + j] = utmp[i * sizex + j];
	// 	}
	// }
}

double relax_jacobi_mix(double *u, double *utmp, unsigned sizex, unsigned sizey)
{
    double diff, sum = 0.0;

    for (int i = 1; i < sizey - 1; i++) {
        for (int j = 1; j < sizex - 1; j++) {
            utmp[i * sizex + j] = 0.25 * (u[i * sizex + (j - 1)] +  // left
                                          u[i * sizex + (j + 1)] +  // right
                                          u[(i - 1) * sizex + j] +  // top
                                          u[(i + 1) * sizex + j]); // bottom

            diff = utmp[i * sizex + j] - u[i * sizex + j];
            sum += diff * diff;
        }
    }

    return sum;
}

double relax_jacobi_mix_blocking(double *u, double *utmp, unsigned sizex, unsigned sizey, unsigned blocksize)
{
    double diff, sum = 0.0;

    for (int bi = 1; bi < sizey - 1; bi += blocksize) {
        for (int bj = 1; bj < sizex - 1; bj += blocksize) {
            for (int i = bi; i < min(bi + blocksize, sizey - 1); i++) {
                for (int j = bj; j < min(bj + blocksize, sizex - 1); j++) {
                    utmp[i * sizex + j] = 0.25 * (u[i * sizex + (j - 1)] +  // left
                                                  u[i * sizex + (j + 1)] +  // right
                                                  u[(i - 1) * sizex + j] +  // top
                                                  u[(i + 1) * sizex + j]); // bottom

                    diff = utmp[i * sizex + j] - u[i * sizex + j];
                    sum += diff * diff;
                }
            }
        }
    }

    return sum;
}