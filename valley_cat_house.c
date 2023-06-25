// fitnessAndWellness.c 
#include <stdio.h>

// Enumeration representing the different class types
typedef enum {
    YOGA,
    PILATES,
    TAI_CHI,
    RESISTANCE,
    ZUMBA,
    CORE
} ClassType;

// Structure representing a class
typedef struct {
    ClassType type;
    int duration;
    int difficulty;
    char *instructor;
} FitnessClass;

// Define static classes array
static FitnessClass classes[2000];

// Function to add a new FitnessClass
void addClass(FitnessClass class) {
    static int index = 0;

    // Add class to classes array
    classes[index] = class;
    index++;
}

// Function to remove a FitnessClass
void removeClass(int classIndex) {
    int i;
   
    // Starting at classIndex, shift each class forward one index
    for (i = classIndex; i < 2000; i++) {
        classes[i] = classes[i+1];
    }
}

// Function to search for a FitnessClass
FitnessClass searchClass(ClassType type) {
    int i;
    
    // Iterate through all classes
    for (i = 0; i < 2000; i++) {
        if (classes[i].type == type) {
            // Found matching class type
            return classes[i];
        }
    }
    
    // Return zeroed FitnessClass if no match is found
    FitnessClass emptyClass = { 0 };
    return emptyClass;
}

// Function to print details for a FitnessClass
void printClassDetails(ClassType type) {
    int i;
    
    // Iterate through all classes
    for (i = 0; i < 2000; i++) {
        if (classes[i].type == type) {
            // Found matching class type
            printf("Class Type: %s\n", type);
            printf("Duration: %d minutes\n", classes[i].duration);
            printf("Difficulty: %d\n", classes[i].difficulty);
            printf("Instructor: %s\n", classes[i].instructor);
            break;
        }
    }
}

int main()
{
    // Create a new Yoga class
    FitnessClass yogaClass = {
        YOGA,
        75,
        2,
        "John Doe"
    };

    // Add class to classes array
    addClass(yogaClass);

    // Print details for yoga class
    printClassDetails(YOGA);

    return 0;
}