#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <sys/wait.h>

#define    LINE_SIZE    1024
char buf[LINE_SIZE];

int
main(int argc, char *argv[])
{
    if(argc != 2){
        printf("usage: %s IP message\n", argv[0]);
        exit(-1);
    }

    int cfd;
    struct sockaddr_in my_addr, peer_addr;
    memset(&my_addr, 0, sizeof(my_addr));
    memset(&peer_addr, 0, sizeof(peer_addr));

    cfd = socket(AF_INET, SOCK_STREAM, 0);
    if(cfd == -1){
        perror("socket error");
        exit(-1);
    }

    peer_addr.sin_family = AF_INET;
    peer_addr.sin_port = htons(2000);
    peer_addr.sin_addr.s_addr = htonl(atoi(argv[1]));
    socklen_t sock_len = sizeof(struct sockaddr_in);
    if(connect(cfd, (struct sockaddr*)&peer_addr, sock_len) == -1){
        perror("connect error");
        exit(-1);
    }

    int len;
    for(;;){
        if(gets(buf) == NULL){
            break;
        }
        len = strlen(buf);

        if(send(cfd, buf, len, 0) != len){
            perror("send error");
            continue;
        }

        len = recv(cfd, buf, LINE_SIZE, 0);
        if(len == -1){
            perror("recv error");
            continue;
        }

        if(write(STDOUT_FILENO, buf, len) != len){
            perror("write error");
            continue;
        }
        write(STDOUT_FILENO, "\n", 1);
    }

    close(cfd);
    return 0;
}
