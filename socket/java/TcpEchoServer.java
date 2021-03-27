package socket.java;

public class TcpEchoServer {
    static int PORT = 9933;

    public static void main(String[] args) {
        ServSock ss = null;
        TcpSock s = null;
        try {
            ss = new ServSock(PORT, true);
            s = ss.accept();

            while (true)
                s.send(s.recvLine() + "\n");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (s != null)
                    s.closeAll();
                if (ss != null)
                    ss.close();
            } catch (Exception e) {}
        }
    }
}
