package chp_1;

import java.lang.Math;
public class ChapterOne{
    /**
     * log2 N = loge N / loge 2
     *      Java doesn't have a native log2. To calculate log2 of N one must do this indirectly.
     *      Natural Log N divided by natural log 2.
     * */
    public static void compareInsertionSortWithMerge(){
        /* Suppose that for inputs of size n on a particular computer, insertion sort runs in 8n^2 steps and merge sort
            runs in 64 nlg n steps. For which value n does insertion sort beat merge sort.
        * */
        double n = 2;
        boolean insertLessThanMerge = true;
        double insertSortN = 0;
        double mergeSortN = 0;
        while(insertLessThanMerge){

        insertSortN = calculateInsertSort(n);
        mergeSortN = calculateMergeSort(n);
            insertLessThanMerge= insertSortN < mergeSortN;
            n++;
        }

        System.out.println("Insert Sort takes "+ insertSortN +" many steps to execute on " + n + " many inputs.");
        System.out.println("Merge Sort takes "+ mergeSortN +" many steps to execute " + n + " many inputs.");
    // 45
    }

    private static double calculateInsertSort(double n){
        return 8 * Math.pow(n,2);
    }
    private static double calculateMergeSort(double n){
        return 64 * n * (Math.log(n)/Math.log(2));
    }

    public static void smallestValueOfN(){
        // Smallest value of n such at an algorithm whose running time is 100n2 runs faster than an algorithm whose
        //  running time is 2n

        boolean nSquaredLessThanTwoN = false;
        int n = 1;
        double nSquareRunTime = 0;
        double twoPowerNRunTime = 0;
        while(!nSquaredLessThanTwoN){

            nSquareRunTime = 100 * Math.pow(n, 2);
            twoPowerNRunTime = Math.pow(2, n);
            if(nSquareRunTime < twoPowerNRunTime){break;}
            ++n;
        }
        System.out.println(nSquareRunTime);
        System.out.println(twoPowerNRunTime);
        System.out.println("The smallest n where nSquared runtime is faster than 2PowerN is: " + n);

    }
}