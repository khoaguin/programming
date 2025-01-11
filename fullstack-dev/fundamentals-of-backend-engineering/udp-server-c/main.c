//https://github.com/nikhilroxtomar/UDP-Client-Server-Program-in-C

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(int argc, char **argv){

  int port = 5501;  // listen at this fixed port
  int sockfd;
  struct sockaddr_in myaddr, remoteAddr;
  char buffer[1024];
  socklen_t addr_size;

  // create socket ("AF_INET" specifies IPv4, "SOCK_DGRAM" specifies UDP)
  sockfd = socket(AF_INET, SOCK_DGRAM, 0);

  memset(&myaddr, '\0', sizeof(myaddr));  // set the size of myaddr
  myaddr.sin_family = AF_INET;
  myaddr.sin_port = htons(port);
  myaddr.sin_addr.s_addr = inet_addr("127.0.0.1");

  bind(sockfd, (struct sockaddr*)&myaddr, sizeof(myaddr));  // let's listen at myaddr
  addr_size = sizeof(remoteAddr);
  // receive data from `sockfd` and store in `buffer`
  // whoever sent the datagram, place their addr in `remoteAddr`
  recvfrom(sockfd, buffer, 1024, 0, (struct sockaddr*)& remoteAddr, &addr_size);
  printf("got data from %s ", buffer);
  return 0;
}