//https://github.com/nikhilroxtomar/tcp-client-server-in-C

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 8801

int main(){

	int sockfd;
	struct sockaddr_in serverAddr;  // destination

	int newSocket;
	struct sockaddr_in newAddr;  // source

	socklen_t addr_size;
	char buffer[1024];

    // create socket ("AF_INET" specifies IPv4, "SOCK_STREAM" specifies TCP)
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	printf("Server Socket Created Sucessfully.\n");
	memset(&serverAddr, '\0', sizeof(serverAddr));

	serverAddr.sin_family = AF_INET;
	serverAddr.sin_port = htons(PORT);
	serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");

    // in UDP, we only bind to the port we want to listen to
    // in TCP, we bind and then listen to incoming connection requests
	bind(sockfd, (struct sockaddr*)&serverAddr, sizeof(serverAddr));
	printf("[+]Bind to Port number %d.\n", PORT);

    // there can be at most 5 connection requests in the queue
    // if there are more than 5, the 6th request will be rejected
    // That's how you do threading and multithreading
    // just to accept as fast as possible and make the
    // queue obviously bigger to accept these connections fast enough
	listen(sockfd, 5);
	printf("[+]Listening...\n");

    // accept incoming connection requests
    // when we accept the connection, we're going to get the new address 
    // from the remote address, which has the source port & the source address
	newSocket = accept(sockfd, (struct sockaddr*)&newAddr, &addr_size);

    //  prints a copies a string "hello" to the buffer,
    // then send that buffer object using the newSocket
	strcpy(buffer, "Hello");
	send(newSocket, buffer, strlen(buffer), 0);
	printf("[+]Closing the connection.\n");

    return 0;

}