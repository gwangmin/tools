package socket.java;

public class TcpEchoClient {
    static String HOST = "127.0.0.1";
    static int PORT = 9933;
    public static void main(String[] args) {
        TcpSock s = null;
        try {
            s = new TcpSock(HOST, PORT, true);
            while (true) {
                s.send(s.input("input: ") + "\n");
                System.out.println(s.recvLine());
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (s != null)
                    s.closeAll();
            } catch (Exception e) {}
        }
    }
}
