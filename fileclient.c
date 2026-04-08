#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <string.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int sockfd;
    struct sockaddr_in address;

    address.sin_family = AF_INET;
    inet_pton(AF_INET, "127.0.0.1", &(address.sin_addr));
    address.sin_port = htons(1234);


    sockfd = socket(AF_INET, SOCK_STREAM, 0);

    connect(sockfd, (struct sockaddr *) &address, sizeof(address));

    char buffer[1024] = {0};
    FILE *fout = fopen("clientfile", "wb");

    recv(sockfd, buffer, 1024, 0);
    ssize_t filesize = atol(buffer);
    printf("size of file to receive: %ld\n", filesize);
    memset(buffer, 0, strlen(buffer));
    sprintf(buffer, "send");
    send(sockfd, buffer, strlen(buffer), 0);
    memset(buffer, 0, strlen(buffer));

    char *filebuffer;
    filebuffer = (char*)malloc(filesize);
    recv(sockfd, filebuffer, filesize, 0);

    fwrite(filebuffer, 1, filesize, fout);
    free(filebuffer);
    fclose(fout);

    // read(0, buffer, 1024);
    // send(sockfd, buffer, strlen(buffer), 0);
    // memset(buffer, 0, strlen(buffer));
    // recv(sockfd, buffer, 1024, 0);
    // printf("received from server: %s\n", buffer);
    return 0;
}