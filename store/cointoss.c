#include <stdio.h>
#include <time.h>
#include <stdlib.h>
/**
 * main - cointoss game.
 * Return: 0
 */

int main(void)
{

	int player_choice, computer_choice, winner, randomNumber;

	/* for random value in C */
	srand(time(NULL)); 
	randomNumber = rand() % 2;//would generate value between 0 and 1.
	

	winner = randomNumber + 1;
	/* printf("The winner is %d \n" ,winner); */
	printf("\t\t\n\n______Enter your choice between Head (1) or Tail (2) _______\n");
	scanf("%d", &player_choice);

	printf("____The cointoss Begins!!!!!_____ \n\n");
	
	if (player_choice == 1)
	{
	
		computer_choice = 2;
		printf(" ___\nYou chose Head____ \n ___computer choose tail then ____\n");

		if (player_choice == winner)
			printf(" \t\tYou won!!! \n");

		else if (player_choice != winner)
		{
		
			printf(" \t\tComputer won \n");

		} 
				}
	else if (player_choice == 2 )
	{
	
		computer_choice = 1;
		printf(" ___\nYou chose Head____ \n ___computer choose tail then ____\n");

		if (player_choice == winner)
			printf(" \t\tYou won!!! \n");
		else if (player_choice != winner)
		{

			printf(" \t\tComputer won \n");

		}

	}
	else {
	printf("Invalid Choice!!! \n\n");
	}
	return (0);

}
