package socket.java;

public class UdpEchoClient {
    static String HOST = "127.0.0.1";
    static int PORT = 8322;
    public static void main(String[] args) {
        UdpSock s = null;
        try {
            s = new UdpSock(true);
            while (true) {
                s.send(s.input("input: "), HOST, PORT);
                s.recv();
            }
        } catch (Exception e) { e.printStackTrace(); }
        finally {
            if (s != null)
                s.close();
        }
    }
}
