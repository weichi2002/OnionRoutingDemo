#include <iostream>
#include <vector>
#include <string>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

// Define Node structure
struct Node {
    std::string address;
    int port;
    int socket_fd;

    Node(std::string addr, int p) : address(std::move(addr)), port(p) {
        // Initialize socket
        socket_fd = socket(AF_INET, SOCK_STREAM, 0);
        if (socket_fd == -1) {
            std::cerr << "Error: Failed to create socket" << std::endl;
            exit(EXIT_FAILURE);
        }
    }

    void connectTo(Node& node) {
        struct sockaddr_in server_addr;
        server_addr.sin_family = AF_INET;
        server_addr.sin_port = htons(node.port);
        inet_pton(AF_INET, node.address.c_str(), &server_addr.sin_addr);

        if (connect(socket_fd, reinterpret_cast<struct sockaddr*>(&server_addr), sizeof(server_addr)) == -1) {
            std::cerr << "Error: Connection failed" << std::endl;
            exit(EXIT_FAILURE);
        }
    }

    void sendData(const std::string& data) {
        send(socket_fd, data.c_str(), data.length(), 0);
    }

    std::string receiveData() {
        char buffer[1024] = {0};
        read(socket_fd, buffer, 1024);
        return std::string(buffer);
    }
    
    ~Node() {
        close(socket_fd);
    }
};

// Define Onion Packet structure
struct OnionPacket {
    std::vector<std::string> layers;
    std::string finalDestination;
};

// Simulate node operations
void simulateNode(Node& node, OnionPacket& packet) {
    // If not the final destination, forward packet
    if (node.address != packet.finalDestination) {
        std::cout << "Forwarding to the next node..." << std::endl;
        // Simulate sending packet to the next node
        // (In a real implementation, you would send it over a network)
        std::cout << "Packet contents: " << packet.layers.back() << std::endl;
        packet.layers.pop_back(); // Remove layer after forwarding

        // Forward packet to the next node
        node.sendData(packet.layers.back());
        packet.layers.pop_back(); // Remove layer after forwarding

        // Receive acknowledgment from the next node
        std::string acknowledgment = node.receiveData();
        std::cout << "Acknowledgment received: " << acknowledgment << std::endl;
    } else {
        std::cout << "Packet reached the final destination!" << std::endl;
        std::cout << "Original data: " << packet.layers.back() << std::endl;
    }
}

int main() {
    // Create nodes
    Node nodeA("127.0.0.1", 8080);
    Node nodeB("127.0.0.1", 8081);
    Node nodeC("127.0.0.1", 8082);

    // Connect nodes
    nodeA.connectTo(nodeB);
    nodeB.connectTo(nodeC);

    // Create onion packet
    OnionPacket packet;
    packet.layers.push_back("Data Layer");
    packet.layers.push_back("Layer 2");
    packet.layers.push_back("Layer 1");
    packet.finalDestination = "127.0.0.1"; // Final destination (loopback address of nodeC)

    // Simulate routing
    simulateNode(nodeA, packet);

    return 0;
}
