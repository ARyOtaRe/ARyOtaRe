#include <stdio.h>
#include <stdlib.h>



typedef struct Element Element;

typedef struct list list;

struct Element{
int x;
Element *suivant;
Element *precedent;
};

struct list{
Element *premier;
Element *dernier;
};

int count(list *l);

void insertq(list *l, int x);

void insert(list *l, int x);

list *init(void);

void affiche(list *l);

void search(list *l, int x);


int main(int argc, char *argv[]) {
	int x, cpt;
	list *l = malloc(sizeof(*l));
	l = init();
	do{
		printf("saisir un entier :");
		scanf("%d", &x);
		if(x>0)
			insertq(l, x);
	}while(x>0);
	affiche(l);
	cpt = count(l);
	printf("nombre de valeurs : %d\n", cpt);
	insert(l, 100);
	affiche(l);
	printf("nombre de valeurs : %d\n", count(l));
	printf("saisir valeur de lelement a supprimer : ");
	scanf("%d", &x);
	search(l, x);
	affiche(l);
	return 0;
}


void search(list *l, int x){//exo 1 d)
	Element *courant = l->premier;
	while(courant != NULL){
		if(courant->x == x){
			Element *suppr = courant;
			courant = courant->suivant;
			Element *precedent = suppr->precedent;
			Element *suivant = suppr->suivant;
			precedent->suivant = suivant;
			suivant->precedent = precedent;
			free(suppr);
		}
		courant = courant->suivant;
	}	
}


void insert(list *l, int x){//exo 1 c)
	Element *elnv = malloc(sizeof(*elnv));
	Element *pr = l->premier;
	elnv->precedent = NULL;
	elnv->suivant = pr;
	elnv->x = x;
	pr->precedent = elnv;
	l->premier = elnv;
}


void insertq(list *l, int x){//exo 1 b)
	Element *elnv = malloc(sizeof(*elnv));
	Element *dr = l->dernier;
	dr->suivant = elnv;
	elnv->precedent = dr;
	elnv->suivant = NULL;
	elnv->x = x;
	l->dernier = elnv;
}


int count(list *l){//exo 1 a)
	int cpt=0;
	Element *courant = l->premier;
	while(courant != NULL){
		cpt=cpt+1;
		courant = courant->suivant;
	}
	return cpt;
}


list *init(void){
  list *l = malloc(sizeof(*l));
  Element *el = malloc(sizeof(*el));
  el->suivant = NULL;
  el->precedent = NULL;
  el->x = 0;
  l->premier = el;
  l->dernier = el;
  return l;
}


void affiche(list *l){
	Element *courant = l->premier;
	while(courant!= NULL){
		printf("%d\n", courant->x);
		courant = courant->suivant;
	}
}
