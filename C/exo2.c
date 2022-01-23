#include <stdio.h>
#include <stdlib.h>



typedef struct Element Element;

typedef struct list list;

struct Element{
 char nom[100];
 Element *suivant;
};

struct list{
 Element *premier;
 Element *dernier;
};

list *init(void);

void insert(list *l, char nom[]);

void affiche(list *l);


int main(int argc, char *argv[]) {
	char nom[50];
 	list *l = init();
 	do{
     	printf("saisir nom: ");
      	scanf("%s", nom);
      	if(nom[0]!='@'){
        	insert(l, nom);
    	}
	}while(nom[0]!='@');  
  printf("affichage de la liste: \n");
  affiche(l);
	
	return 0;
}


list *init(void){//exo 2 a)
  list *l = malloc(sizeof(*l));
  Element *el = malloc(sizeof(*el));
  el->suivant = NULL;
  l->premier = el;
  l->dernier = el;
  return l;
}


void insert(list *l, char nom[]){//exo 2 b)
	Element *elnv = malloc(sizeof(*elnv));
	Element *courant = l->dernier;
	strcpy(elnv->nom, nom);
	elnv->suivant = NULL;
	courant->suivant = elnv;
	l->dernier = elnv;	
}


void affiche(list *l){//exo 2 c)
  Element *courant = l->premier;
  while(courant != NULL){
    printf("nom: %s\n", courant->nom);
    courant = courant->suivant;
  }
}
