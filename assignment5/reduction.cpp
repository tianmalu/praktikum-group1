
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "mpi.h"

int main(int argc, char const *argv[])
{
    int myid, commSize, ierr, lnbr, rnbr, sum;
    int *values;
    MPI_Status status;

    // Initialization of MPI communications
    ierr = MPI_Init(&argc, &argv);
    if (ierr != MPI_SUCCESS) {
        printf("MPI is not initialized, return code %d\n", ierr);
        return -1;
    }
    MPI_Comm_size(MPI_COMM_WORLD, &commSize);
    MPI_Comm_rank(MPI_COMM_WORLD, &myid);

    // Distributing data over ranks
    int arraySize = atoi(argv[1]);
    int arraySizePerRank = ceil(arraySize / commSize);

    sum = 0;
    
    // Data initialization on local memory
    if (myid != (commSize - 1)) {
        values = (int *) malloc(arraySizePerRank * sizeof(int));
        for (int i = 0; i < arraySizePerRank; i++) {
            values[i] = (arraySizePerRank * myid) + i;
            // sum += values[i];
            // Debug print
            // printf("Node %d inside for loop value assigned: values[%d] = %d\n", myid, i, values[i]);
        }
        // Debug print
        // printf("Node %d: Array Size %d, Array Size Per Node %d\n", myid, arraySize, arraySizePerRank);
    }
    else {
        int arraySizeForLastRank = arraySize - (arraySizePerRank * myid);
        values = (int *) malloc(arraySizeForLastRank * sizeof(int));
        for (int i = 0; i < arraySizeForLastRank; i++) {
            values[i] = (arraySizePerRank * myid) + i;
            // sum += values[i];
            // Debug print
            // printf("Node %d inside for loop value assigned: values[%d] = %d\n", myid, i, values[i]);
        }
        // Debug print
        // printf("Node %d: Array Size %d, Array Size Per Node %d\n", myid, arraySize, arraySizeForLastRank);
    }

    // Summing up the data of the local array
    
    if (myid != (commSize - 1)) {
        for (int i = 0; i < arraySizePerRank; i++) {
            sum += values[i];
        }
    }
    else {
        int arraySizeForLastRank = arraySize - (arraySizePerRank * myid);
        for (int i = 0; i < arraySizeForLastRank; i++) {
            sum += values[i];
        }
    }


    // Building tree structure according to the rank and the MPI world size
    int parent = ((myid + 1) / 2) - 1;
    int isRoot = (parent == -1);
    int isLeaf = ((myid + 1) * 2) > commSize;
    int numOfChildNodes = !isLeaf ? (((myid + 1) * 2) > (commSize - 1) ? 1 : 2) : 0;
    int child1 = ((myid + 1) * 2) - 1;
    int child2 = ((myid + 1) * 2);
    int resultBufferFromChild[2];

    // Debug print
    // printf("Node %d: Parent %d, ChildNum %d, Child1 %d, Child2 %d, Sum %d\n", myid, parent, numOfChildNodes, child1, child2, sum);

    if (isLeaf) {
        MPI_Send(&sum, 1, MPI_INTEGER, parent, 0, MPI_COMM_WORLD);
        // printf("Node: %d, sum: %d\n", myid, sum);
    }
    else if (!isRoot) {
        MPI_Recv(&(resultBufferFromChild[0]), 1, MPI_INTEGER, child1, 0, MPI_COMM_WORLD, &status);
        if (numOfChildNodes == 2) MPI_Recv(&(resultBufferFromChild[1]), 1, MPI_INTEGER, child2, 0, MPI_COMM_WORLD, &status);
        // printf("Node: %d, sum: %d\n", myid, sum);
        for (int i = 0; i < numOfChildNodes; i++) {
            sum += resultBufferFromChild[i];
        }
        // printf("Node: %d, sum: %d\n", myid, sum);
        MPI_Send(&sum, 1, MPI_INTEGER, parent, 0, MPI_COMM_WORLD);
    }
    else {
        MPI_Recv(&(resultBufferFromChild[0]), 1, MPI_INTEGER, child1, 0, MPI_COMM_WORLD, &status);
        if (numOfChildNodes == 2) MPI_Recv(&(resultBufferFromChild[1]), 1, MPI_INTEGER, child2, 0, MPI_COMM_WORLD, &status);
        // printf("Node: %d, sum: %d\n", myid, sum);
        for (int i = 0; i < numOfChildNodes; i++) {
            sum += resultBufferFromChild[i];
        }
        // printf("Node: %d, sum: %d\n", myid, sum);
    }

    if (myid == 0) printf("%d\n", sum);

    return 0;
}
