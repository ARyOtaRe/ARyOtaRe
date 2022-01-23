#include <stdio.h>
#include <stdlib.h>



typedef struct Element Element;

typedef struct list list;

struct Element{
 int donnee;
 Element *suivant;
};

struct list{
 Element *debut;
 Element *fin;
 int taille;
};
