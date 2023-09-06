#include <stdio.h>
#include <string.h>
/**
 * main - Confirm login credentials
 * Return: 0
 */
int main (void)
{

	char username[20], password_first[6], password_next[6];

	printf("Enter your Desireed Username: \n");
	scanf("%s", username);

	printf("Enter your Password (4): \n");
	scanf("%s", password_first);

	printf("Confirm Your Password (4): \n");
	scanf("%s", password_next);

	if (strcmp(password_first, password_next) == 0)
		printf("Sign-up Successful!!! \n");

	else if (strcmp(password_first, password_next) != 0)
		printf("Password miss-match \n");


}
