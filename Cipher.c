#include<stdio.h>
#include<string.h>
#include<stdlib.h>
void encrypt(char *str,int key)
{
    while(*str!='\0')
    {
        *str=*str+key;
        str++;
    }

}
void decrypt(char *str,int key)
{
    while(*str!='\0')
    {
        *str=*str-key;
        str++;
    }

}
int main()
{
    char st[100];
    int key;
    int count=0;
    int length;
    int c,d;
    char *password;
    char s[100];
    do
    {
        printf("1.Create a new password\n2.Login\n3.Exit\n");
        scanf("%d",&c);
        switch(c)
        {
            case 1:
            printf("Enter the desired password length: ");
            scanf("%d",&length);
            password=(char*)malloc(length+1);
            printf("Enter the password: ");
            scanf("%s",password);
            break;

            case 2:
            initial:
            if(count==3)
            {
                printf("You have entered the wrong password 3 times. Exiting...\n");
                exit(0);
            }
            printf("Enter the password: ");
            scanf("%s",s);
            if(strcmp(s,password)==0)
            {
                printf("1.Encrypt\n2.Decrypt\n3.Back to Main Menu.\n");
                scanf("%d",&d);
                switch(d)
                {
                    case 1:
                    printf("Enter the string to be encrypted: ");
                    scanf("%s",st);
                    printf("Enter the key: ");
                    scanf("%d",&key);
                    encrypt(st,key);
                    printf("Encrypted string: %s\n",st);
                    break;

                    case 2:
                    printf("Enter the string to be decrypted: ");
                    scanf("%s",st);
                    printf("Enter the key: ");
                    scanf("%d",&key);
                    decrypt(st,key);
                    printf("Decrypted string: %s\n",st);
                    break;

                    case 3:
                    break;

                    default:
                    printf("Invalid choice\n");
                    break;
                }
            }
            else
            {
                printf("Invalid password\n");
                count++;
                goto initial;
            }

        }
    }while (c!=3);
}